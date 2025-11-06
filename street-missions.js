/**
 * RANDOM STREET MISSIONS & RESCUE OPERATIONS
 * 
 * GTA-style random encounters:
 * - Street fights and brawls
 * - Human trafficking rescue operations
 * - Building fires and emergency response
 * - Theft prevention
 * - Gang confrontations
 */

class StreetMissions {
    constructor() {
        this.activeMissions = new Map();
        this.missionTypes = this.initializeMissionTypes();
        this.rewardMultipliers = {
            easy: 1,
            medium: 2,
            hard: 5,
            extreme: 10
        };
    }

    /**
     * Initialize all mission types
     */
    initializeMissionTypes() {
        return {
            // STREET FIGHTS
            streetFight: {
                name: 'Street Brawl',
                description: 'Random thug challenges you to a fight',
                difficulty: ['easy', 'medium', 'hard'],
                rewards: { xp: 50, btc: 0.00001 },
                duration: 120, // seconds
                successRate: 0.7
            },
            gangConfrontation: {
                name: 'Gang Territory Fight',
                description: 'Local gang tries to shake you down',
                difficulty: ['medium', 'hard', 'extreme'],
                rewards: { xp: 200, btc: 0.0001 },
                duration: 300,
                successRate: 0.5
            },

            // RESCUE MISSIONS
            traffickingRescue: {
                name: 'Human Trafficking Rescue',
                description: 'Intel on trafficking operation - rescue victims',
                difficulty: ['hard', 'extreme'],
                rewards: { xp: 1000, btc: 0.001, humanity: 100 },
                duration: 600,
                successRate: 0.4,
                specialReward: 'Hero Badge'
            },
            buildingFire: {
                name: 'Building Fire Emergency',
                description: 'People trapped in burning building',
                difficulty: ['medium', 'hard'],
                rewards: { xp: 500, btc: 0.0005, humanity: 50 },
                duration: 300,
                successRate: 0.6,
                specialReward: 'Firefighter Badge'
            },
            kidnappingRescue: {
                name: 'Kidnapping Rescue',
                description: 'Ransom situation - save the hostage',
                difficulty: ['hard', 'extreme'],
                rewards: { xp: 750, btc: 0.00075, humanity: 75 },
                duration: 450,
                successRate: 0.45
            },

            // THEFT & CRIME PREVENTION
            theftPrevention: {
                name: 'Stop the Thief',
                description: 'Witness theft in progress',
                difficulty: ['easy', 'medium'],
                rewards: { xp: 100, btc: 0.00005 },
                duration: 60,
                successRate: 0.75
            },
            carjacking: {
                name: 'Stop Carjacking',
                description: 'Someone being carjacked nearby',
                difficulty: ['medium', 'hard'],
                rewards: { xp: 300, btc: 0.0003 },
                duration: 180,
                successRate: 0.55
            }
        };
    }

    /**
     * Spawn random mission based on player location and level
     */
    spawnRandomMission(playerLevel, location = 'downtown') {
        const availableMissions = this.getAvailableMissions(playerLevel);
        const missionType = this.selectRandomMission(availableMissions);
        const difficulty = this.selectDifficulty(missionType, playerLevel);

        const mission = {
            id: this.generateMissionId(),
            type: missionType.name,
            description: missionType.description,
            difficulty,
            rewards: this.calculateRewards(missionType.rewards, difficulty),
            timeLimit: missionType.duration,
            location,
            spawnedAt: Date.now(),
            status: 'active',
            successRate: missionType.successRate,
            specialReward: missionType.specialReward || null
        };

        this.activeMissions.set(mission.id, mission);
        return mission;
    }

    /**
     * Get missions available for player level
     */
    getAvailableMissions(playerLevel) {
        const missions = [];
        
        for (const [key, mission] of Object.entries(this.missionTypes)) {
            // Easy missions always available
            if (mission.difficulty.includes('easy')) {
                missions.push(mission);
            }
            // Medium missions at level 3+
            else if (playerLevel >= 3 && mission.difficulty.includes('medium')) {
                missions.push(mission);
            }
            // Hard missions at level 5+
            else if (playerLevel >= 5 && mission.difficulty.includes('hard')) {
                missions.push(mission);
            }
            // Extreme missions at level 10+
            else if (playerLevel >= 10 && mission.difficulty.includes('extreme')) {
                missions.push(mission);
            }
        }
        
        return missions;
    }

    /**
     * Select random mission from available
     */
    selectRandomMission(availableMissions) {
        return availableMissions[Math.floor(Math.random() * availableMissions.length)];
    }

    /**
     * Select appropriate difficulty
     */
    selectDifficulty(missionType, playerLevel) {
        const available = missionType.difficulty.filter(diff => {
            if (diff === 'easy') return true;
            if (diff === 'medium') return playerLevel >= 3;
            if (diff === 'hard') return playerLevel >= 5;
            if (diff === 'extreme') return playerLevel >= 10;
            return false;
        });
        
        return available[Math.floor(Math.random() * available.length)];
    }

    /**
     * Calculate rewards based on difficulty
     */
    calculateRewards(baseRewards, difficulty) {
        const multiplier = this.rewardMultipliers[difficulty];
        
        return {
            xp: Math.floor(baseRewards.xp * multiplier),
            btc: baseRewards.btc * multiplier,
            humanity: baseRewards.humanity ? baseRewards.humanity * multiplier : 0
        };
    }

    /**
     * Generate unique mission ID
     */
    generateMissionId() {
        return `mission_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
    }

    /**
     * Complete mission and award rewards
     */
    completeMission(missionId, success = true) {
        const mission = this.activeMissions.get(missionId);
        if (!mission) {
            return { success: false, error: 'Mission not found' };
        }

        // Check if mission expired
        const elapsed = Date.now() - mission.spawnedAt;
        if (elapsed > mission.timeLimit * 1000) {
            mission.status = 'expired';
            return {
                success: false,
                message: '⏰ Mission time expired!',
                mission
            };
        }

        // Determine success based on success rate
        const succeeded = success && Math.random() < mission.successRate;

        if (succeeded) {
            mission.status = 'completed';
            return {
                success: true,
                message: `✅ Mission Complete: ${mission.type}`,
                rewards: mission.rewards,
                specialReward: mission.specialReward,
                mission
            };
        } else {
            mission.status = 'failed';
            return {
                success: false,
                message: `❌ Mission Failed: ${mission.type}`,
                mission
            };
        }
    }

    /**
     * Get mission HTML for display
     */
    getMissionHTML(mission) {
        const timeRemaining = Math.max(0, mission.timeLimit - Math.floor((Date.now() - mission.spawnedAt) / 1000));
        
        const difficultyColor = {
            easy: '#4ade80',
            medium: '#fbbf24',
            hard: '#f87171',
            extreme: '#dc2626'
        };

        return `
            <div class="mission-card ${mission.difficulty}" data-mission-id="${mission.id}">
                <div class="mission-header">
                    <h3>${mission.type}</h3>
                    <span class="difficulty-badge" style="background: ${difficultyColor[mission.difficulty]}">
                        ${mission.difficulty.toUpperCase()}
                    </span>
                </div>
                <p class="mission-description">${mission.description}</p>
                <div class="mission-timer">
                    ⏱️ ${Math.floor(timeRemaining / 60)}:${(timeRemaining % 60).toString().padStart(2, '0')}
                </div>
                <div class="mission-rewards">
                    <div>⭐ ${mission.rewards.xp} XP</div>
                    <div>₿ ${mission.rewards.btc.toFixed(8)} BTC</div>
                    ${mission.rewards.humanity ? `<div>❤️ ${mission.rewards.humanity} Humanity</div>` : ''}
                </div>
                ${mission.specialReward ? `<div class="special-reward">🏆 ${mission.specialReward}</div>` : ''}
                <button class="accept-mission-btn" onclick="acceptMission('${mission.id}')">
                    Accept Mission
                </button>
            </div>
        `;
    }

    /**
     * Get all active missions
     */
    getActiveMissions() {
        return Array.from(this.activeMissions.values()).filter(m => m.status === 'active');
    }

    /**
     * Clean up expired missions
     */
    cleanupExpiredMissions() {
        const now = Date.now();
        for (const [id, mission] of this.activeMissions.entries()) {
            const elapsed = now - mission.spawnedAt;
            if (elapsed > mission.timeLimit * 1000) {
                mission.status = 'expired';
                this.activeMissions.delete(id);
            }
        }
    }
}

module.exports = { StreetMissions };
