/**
 * MISSION REWARD SYSTEM
 * 
 * Handles crypto rewards, XP, and rank progression
 * Geek Squad → Script Kiddie → Code Hustler → Crypto Runner → Blockchain Boss → Crypto Kingpin
 */

class MissionRewards {
    constructor(dbPool) {
        this.pool = dbPool;
        
        this.ranks = [
            { name: 'Geek Squad', minXP: 0, color: '#00ff88' },
            { name: 'Script Kiddie', minXP: 100, color: '#00c8ff' },
            { name: 'Code Hustler', minXP: 500, color: '#ffa500' },
            { name: 'Crypto Runner', minXP: 2000, color: '#ff00ff' },
            { name: 'Blockchain Boss', minXP: 10000, color: '#ffd700' },
            { name: 'Crypto Kingpin', minXP: 50000, color: '#ff0066' }
        ];

        this.rewardRates = {
            streetFight: { xp: 50, btc: 0.00001 },
            gangFight: { xp: 200, btc: 0.0001 },
            traffickingRescue: { xp: 1000, btc: 0.001, humanity: 100 },
            buildingFire: { xp: 500, btc: 0.0005, humanity: 50 },
            kidnappingRescue: { xp: 750, btc: 0.00075, humanity: 75 },
            theftPrevention: { xp: 100, btc: 0.00005 },
            puzzleSolve: { xp: 5000, btc: 0.01 }
        };
    }

    /**
     * Award mission completion rewards
     */
    async awardMissionRewards(userId, missionType, difficulty = 'medium') {
        const baseReward = this.rewardRates[missionType];
        if (!baseReward) {
            throw new Error(`Unknown mission type: ${missionType}`);
        }

        // Apply difficulty multiplier
        const multiplier = {
            easy: 1,
            medium: 2,
            hard: 5,
            extreme: 10
        }[difficulty] || 1;

        const rewards = {
            xp: Math.floor(baseReward.xp * multiplier),
            btc: baseReward.btc * multiplier,
            humanity: baseReward.humanity ? baseReward.humanity * multiplier : 0
        };

        // Award XP and check for rank up
        const rankUp = await this.awardXP(userId, rewards.xp, missionType);

        // Award BTC
        await this.awardBTC(userId, rewards.btc);

        // Award humanity points if applicable
        if (rewards.humanity > 0) {
            await this.awardHumanity(userId, rewards.humanity);
        }

        // Log the reward
        await this.logReward(userId, missionType, rewards);

        return {
            success: true,
            rewards,
            rankUp,
            message: this.getRewardMessage(missionType, rewards, rankUp)
        };
    }

    /**
     * Award XP and check for rank up
     */
    async awardXP(userId, amount, reason) {
        try {
            // Get current user stats
            const userResult = await this.pool.query(
                'SELECT xp, rank FROM user_profiles WHERE user_id = $1',
                [userId]
            );

            if (userResult.rows.length === 0) {
                throw new Error('User not found');
            }

            const currentXP = userResult.rows[0].xp || 0;
            const currentRank = userResult.rows[0].rank || 'Geek Squad';
            const newXP = currentXP + amount;

            // Calculate new rank
            const newRank = this.calculateRank(newXP);
            const rankedUp = newRank !== currentRank;

            // Update user
            await this.pool.query(
                'UPDATE user_profiles SET xp = $1, rank = $2 WHERE user_id = $3',
                [newXP, newRank, userId]
            );

            return {
                rankedUp,
                oldRank: currentRank,
                newRank,
                totalXP: newXP,
                xpGained: amount
            };
        } catch (error) {
            console.error('Error awarding XP:', error);
            throw error;
        }
    }

    /**
     * Calculate rank based on total XP
     */
    calculateRank(totalXP) {
        for (let i = this.ranks.length - 1; i >= 0; i--) {
            if (totalXP >= this.ranks[i].minXP) {
                return this.ranks[i].name;
            }
        }
        return 'Geek Squad';
    }

    /**
     * Award BTC
     */
    async awardBTC(userId, amount) {
        try {
            await this.pool.query(
                `UPDATE user_profiles 
                 SET btc_earned = COALESCE(btc_earned, 0) + $1 
                 WHERE user_id = $2`,
                [amount, userId]
            );
        } catch (error) {
            console.error('Error awarding BTC:', error);
            throw error;
        }
    }

    /**
     * Award humanity points
     */
    async awardHumanity(userId, amount) {
        try {
            await this.pool.query(
                `UPDATE user_profiles 
                 SET humanity_score = COALESCE(humanity_score, 0) + $1 
                 WHERE user_id = $2`,
                [amount, userId]
            );
        } catch (error) {
            console.error('Error awarding humanity:', error);
            throw error;
        }
    }

    /**
     * Log reward transaction
     */
    async logReward(userId, missionType, rewards) {
        try {
            await this.pool.query(
                `INSERT INTO reward_transactions 
                 (user_id, mission_type, xp, btc, humanity, created_at)
                 VALUES ($1, $2, $3, $4, $5, NOW())`,
                [userId, missionType, rewards.xp, rewards.btc, rewards.humanity]
            );
        } catch (error) {
            console.error('Error logging reward:', error);
            // Non-critical, don't throw
        }
    }

    /**
     * Get formatted reward message
     */
    getRewardMessage(missionType, rewards, rankUp) {
        let message = `🎉 Mission Complete!\n\n`;
        message += `⭐ ${rewards.xp} XP\n`;
        message += `₿ ${rewards.btc.toFixed(8)} BTC\n`;
        
        if (rewards.humanity > 0) {
            message += `❤️ ${rewards.humanity} Humanity\n`;
        }

        if (rankUp && rankUp.rankedUp) {
            message += `\n🎊 RANK UP! ${rankUp.oldRank} → ${rankUp.newRank}`;
        }

        return message;
    }

    /**
     * Get user rewards summary
     */
    async getUserRewardsSummary(userId) {
        try {
            const result = await this.pool.query(
                `SELECT 
                    xp,
                    rank,
                    btc_earned,
                    humanity_score,
                    missions_completed
                 FROM user_profiles
                 WHERE user_id = $1`,
                [userId]
            );

            if (result.rows.length === 0) {
                return null;
            }

            const user = result.rows[0];
            const currentRank = this.ranks.find(r => r.name === user.rank);
            const nextRank = this.ranks[this.ranks.indexOf(currentRank) + 1];

            return {
                xp: user.xp || 0,
                rank: user.rank || 'Geek Squad',
                rankColor: currentRank?.color || '#00ff88',
                btcEarned: user.btc_earned || 0,
                humanityScore: user.humanity_score || 0,
                missionsCompleted: user.missions_completed || 0,
                nextRank: nextRank?.name || 'Max Rank',
                xpToNextRank: nextRank ? nextRank.minXP - user.xp : 0
            };
        } catch (error) {
            console.error('Error getting rewards summary:', error);
            throw error;
        }
    }

    /**
     * Get leaderboard
     */
    async getLeaderboard(limit = 100) {
        try {
            const result = await this.pool.query(
                `SELECT 
                    u.username,
                    u.profile_image_url,
                    up.xp,
                    up.rank,
                    up.btc_earned,
                    up.humanity_score,
                    up.missions_completed
                 FROM user_profiles up
                 JOIN users u ON up.user_id = u.id
                 ORDER BY up.xp DESC
                 LIMIT $1`,
                [limit]
            );

            return result.rows.map((row, index) => ({
                position: index + 1,
                username: row.username,
                profileImage: row.profile_image_url,
                xp: row.xp,
                rank: row.rank,
                btcEarned: row.btc_earned,
                humanityScore: row.humanity_score,
                missionsCompleted: row.missions_completed
            }));
        } catch (error) {
            console.error('Error getting leaderboard:', error);
            throw error;
        }
    }
}

module.exports = { MissionRewards };
