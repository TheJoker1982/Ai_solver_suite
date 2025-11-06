/**
 * SQUAD MULTIPLAYER SYSTEM
 * 
 * Collaborative puzzle solving and rescue missions
 * - Create/join squads
 * - Squad missions with shared rewards
 * - Squad chat and coordination
 * - Squad leaderboards
 */

class SquadSystem {
    constructor(dbPool, io) {
        this.pool = dbPool;
        this.io = io; // Socket.IO instance
        this.activeSquads = new Map();
    }

    /**
     * Create a new squad
     */
    async createSquad(leaderUserId, squadName, maxMembers = 5) {
        try {
            const result = await this.pool.query(
                `INSERT INTO squads (name, leader_id, max_members, created_at)
                 VALUES ($1, $2, $3, NOW())
                 RETURNING *`,
                [squadName, leaderUserId, maxMembers]
            );

            const squad = result.rows[0];

            // Add leader as first member
            await this.pool.query(
                `INSERT INTO squad_members (squad_id, user_id, role, joined_at)
                 VALUES ($1, $2, 'leader', NOW())`,
                [squad.id, leaderUserId]
            );

            // Initialize squad in memory
            this.activeSquads.set(squad.id, {
                id: squad.id,
                name: squadName,
                leaderId: leaderUserId,
                members: [leaderUserId],
                maxMembers,
                currentMission: null
            });

            return {
                success: true,
                squad: {
                    id: squad.id,
                    name: squadName,
                    leader: leaderUserId,
                    members: 1,
                    maxMembers
                }
            };
        } catch (error) {
            return {
                success: false,
                error: error.message
            };
        }
    }

    /**
     * Join a squad
     */
    async joinSquad(userId, squadId) {
        try {
            // Check if squad exists and has space
            const squadResult = await this.pool.query(
                `SELECT * FROM squads WHERE id = $1`,
                [squadId]
            );

            if (squadResult.rows.length === 0) {
                return { success: false, error: 'Squad not found' };
            }

            const squad = squadResult.rows[0];

            // Check current member count
            const memberCount = await this.pool.query(
                `SELECT COUNT(*) FROM squad_members WHERE squad_id = $1`,
                [squadId]
            );

            if (parseInt(memberCount.rows[0].count) >= squad.max_members) {
                return { success: false, error: 'Squad is full' };
            }

            // Add member
            await this.pool.query(
                `INSERT INTO squad_members (squad_id, user_id, role, joined_at)
                 VALUES ($1, $2, 'member', NOW())`,
                [squadId, userId]
            );

            // Update active squad
            if (this.activeSquads.has(squadId)) {
                this.activeSquads.get(squadId).members.push(userId);
            }

            // Notify squad members
            if (this.io) {
                this.io.to(`squad_${squadId}`).emit('member_joined', {
                    userId,
                    timestamp: new Date()
                });
            }

            return {
                success: true,
                message: `Joined squad: ${squad.name}`
            };
        } catch (error) {
            return {
                success: false,
                error: error.message
            };
        }
    }

    /**
     * Leave a squad
     */
    async leaveSquad(userId, squadId) {
        try {
            await this.pool.query(
                `DELETE FROM squad_members 
                 WHERE squad_id = $1 AND user_id = $2`,
                [squadId, userId]
            );

            // Update active squad
            if (this.activeSquads.has(squadId)) {
                const squad = this.activeSquads.get(squadId);
                squad.members = squad.members.filter(id => id !== userId);

                // If leader left, delete squad
                if (userId === squad.leaderId) {
                    await this.deleteSquad(squadId);
                }
            }

            // Notify squad
            if (this.io) {
                this.io.to(`squad_${squadId}`).emit('member_left', {
                    userId,
                    timestamp: new Date()
                });
            }

            return {
                success: true,
                message: 'Left squad'
            };
        } catch (error) {
            return {
                success: false,
                error: error.message
            };
        }
    }

    /**
     * Delete squad
     */
    async deleteSquad(squadId) {
        try {
            await this.pool.query(
                `DELETE FROM squad_members WHERE squad_id = $1`,
                [squadId]
            );

            await this.pool.query(
                `DELETE FROM squads WHERE id = $1`,
                [squadId]
            );

            this.activeSquads.delete(squadId);

            return { success: true };
        } catch (error) {
            return {
                success: false,
                error: error.message
            };
        }
    }

    /**
     * Start squad mission
     */
    async startSquadMission(squadId, missionType) {
        try {
            const squad = this.activeSquads.get(squadId);
            if (!squad) {
                return { success: false, error: 'Squad not active' };
            }

            // Create squad mission
            const missionResult = await this.pool.query(
                `INSERT INTO squad_missions 
                 (squad_id, mission_type, started_at, status)
                 VALUES ($1, $2, NOW(), 'active')
                 RETURNING *`,
                [squadId, missionType]
            );

            const mission = missionResult.rows[0];
            squad.currentMission = mission.id;

            // Notify squad members
            if (this.io) {
                this.io.to(`squad_${squadId}`).emit('mission_started', {
                    missionId: mission.id,
                    missionType,
                    timestamp: new Date()
                });
            }

            return {
                success: true,
                mission: {
                    id: mission.id,
                    type: missionType,
                    squadSize: squad.members.length
                }
            };
        } catch (error) {
            return {
                success: false,
                error: error.message
            };
        }
    }

    /**
     * Complete squad mission
     */
    async completeSquadMission(squadId, missionId, success = true) {
        try {
            const squad = this.activeSquads.get(squadId);
            if (!squad) {
                return { success: false, error: 'Squad not active' };
            }

            // Update mission status
            await this.pool.query(
                `UPDATE squad_missions 
                 SET status = $1, completed_at = NOW()
                 WHERE id = $2`,
                [success ? 'completed' : 'failed', missionId]
            );

            squad.currentMission = null;

            if (success) {
                // Award rewards to all members
                const rewards = this.calculateSquadRewards(squad.members.length);

                for (const memberId of squad.members) {
                    await this.awardSquadRewards(memberId, rewards);
                }

                // Notify success
                if (this.io) {
                    this.io.to(`squad_${squadId}`).emit('mission_completed', {
                        missionId,
                        success: true,
                        rewards,
                        timestamp: new Date()
                    });
                }

                return {
                    success: true,
                    rewards,
                    message: 'Squad mission completed!'
                };
            } else {
                // Notify failure
                if (this.io) {
                    this.io.to(`squad_${squadId}`).emit('mission_failed', {
                        missionId,
                        timestamp: new Date()
                    });
                }

                return {
                    success: false,
                    message: 'Squad mission failed'
                };
            }
        } catch (error) {
            return {
                success: false,
                error: error.message
            };
        }
    }

    /**
     * Calculate squad rewards (bonus for teamwork)
     */
    calculateSquadRewards(squadSize) {
        const baseXP = 500;
        const baseBTC = 0.0005;

        // Teamwork bonus: +20% per additional member
        const teamworkBonus = 1 + (squadSize - 1) * 0.2;

        return {
            xp: Math.floor(baseXP * teamworkBonus),
            btc: baseBTC * teamworkBonus,
            squadBonus: `+${((teamworkBonus - 1) * 100).toFixed(0)}%`
        };
    }

    /**
     * Award rewards to squad member
     */
    async awardSquadRewards(userId, rewards) {
        try {
            await this.pool.query(
                `UPDATE user_profiles 
                 SET xp = COALESCE(xp, 0) + $1,
                     btc_earned = COALESCE(btc_earned, 0) + $2
                 WHERE user_id = $3`,
                [rewards.xp, rewards.btc, userId]
            );
        } catch (error) {
            console.error('Error awarding squad rewards:', error);
        }
    }

    /**
     * Get squad details
     */
    async getSquad(squadId) {
        try {
            const squadResult = await this.pool.query(
                `SELECT s.*, u.username as leader_name
                 FROM squads s
                 JOIN users u ON s.leader_id = u.id
                 WHERE s.id = $1`,
                [squadId]
            );

            if (squadResult.rows.length === 0) {
                return null;
            }

            const squad = squadResult.rows[0];

            // Get members
            const membersResult = await this.pool.query(
                `SELECT u.id, u.username, u.profile_image_url, sm.role
                 FROM squad_members sm
                 JOIN users u ON sm.user_id = u.id
                 WHERE sm.squad_id = $1`,
                [squadId]
            );

            return {
                id: squad.id,
                name: squad.name,
                leaderId: squad.leader_id,
                leaderName: squad.leader_name,
                maxMembers: squad.max_members,
                members: membersResult.rows,
                currentMission: this.activeSquads.get(squadId)?.currentMission || null
            };
        } catch (error) {
            console.error('Error getting squad:', error);
            return null;
        }
    }

    /**
     * Get all squads
     */
    async getAllSquads(limit = 50) {
        try {
            const result = await this.pool.query(
                `SELECT 
                    s.id,
                    s.name,
                    s.max_members,
                    u.username as leader_name,
                    COUNT(sm.user_id) as member_count
                 FROM squads s
                 JOIN users u ON s.leader_id = u.id
                 LEFT JOIN squad_members sm ON s.id = sm.squad_id
                 GROUP BY s.id, s.name, s.max_members, u.username
                 ORDER BY member_count DESC
                 LIMIT $1`,
                [limit]
            );

            return result.rows.map(row => ({
                id: row.id,
                name: row.name,
                leaderName: row.leader_name,
                members: parseInt(row.member_count),
                maxMembers: row.max_members,
                available: parseInt(row.member_count) < row.max_members
            }));
        } catch (error) {
            console.error('Error getting all squads:', error);
            return [];
        }
    }

    /**
     * Get squad leaderboard
     */
    async getSquadLeaderboard(limit = 20) {
        try {
            const result = await this.pool.query(
                `SELECT 
                    s.id,
                    s.name,
                    COUNT(DISTINCT sm.mission_id) as missions_completed,
                    SUM(up.xp) as total_xp
                 FROM squads s
                 LEFT JOIN squad_missions sm ON s.id = sm.squad_id AND sm.status = 'completed'
                 LEFT JOIN squad_members smem ON s.id = smem.squad_id
                 LEFT JOIN user_profiles up ON smem.user_id = up.user_id
                 GROUP BY s.id, s.name
                 ORDER BY missions_completed DESC, total_xp DESC
                 LIMIT $1`,
                [limit]
            );

            return result.rows.map((row, index) => ({
                position: index + 1,
                squadName: row.name,
                missionsCompleted: parseInt(row.missions_completed) || 0,
                totalXP: parseInt(row.total_xp) || 0
            }));
        } catch (error) {
            console.error('Error getting squad leaderboard:', error);
            return [];
        }
    }
}

module.exports = { SquadSystem };
