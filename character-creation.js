/**
 * GTA-STYLE CHARACTER CREATION SYSTEM
 * 
 * Full character customization with stats, skills, appearance
 */

class CharacterCreation {
    constructor() {
        this.characterTemplates = {
            rookie: {
                name: 'Street Rookie',
                stats: { hacking: 1, fighting: 1, intelligence: 1, luck: 1 },
                startingRank: 'Geek Squad'
            },
            hacker: {
                name: 'Code Slinger',
                stats: { hacking: 3, fighting: 1, intelligence: 3, luck: 1 },
                startingRank: 'Script Kiddie'
            },
            brawler: {
                name: 'Street Fighter',
                stats: { hacking: 1, fighting: 3, intelligence: 1, luck: 3 },
                startingRank: 'Geek Squad'
            }
        };

        this.appearances = {
            faces: ['face1', 'face2', 'face3', 'face4', 'face5'],
            hair: ['short', 'long', 'bald', 'mohawk', 'dreadlocks'],
            clothes: ['casual', 'hoodie', 'suit', 'tactical', 'cyberpunk'],
            accessories: ['none', 'glasses', 'mask', 'headphones', 'hat']
        };

        this.rankProgression = [
            { rank: 'Geek Squad', minXP: 0 },
            { rank: 'Script Kiddie', minXP: 100 },
            { rank: 'Code Hustler', minXP: 500 },
            { rank: 'Crypto Runner', minXP: 2000 },
            { rank: 'Blockchain Boss', minXP: 10000 },
            { rank: 'Crypto Kingpin', minXP: 50000 }
        ];
    }

    /**
     * Create new character
     */
    createCharacter(options) {
        const character = {
            id: this.generateCharacterId(),
            name: options.name || 'Crypto Player',
            template: options.template || 'rookie',
            
            // Stats
            stats: {
                hacking: options.stats?.hacking || 1,
                fighting: options.stats?.fighting || 1,
                intelligence: options.stats?.intelligence || 1,
                luck: options.stats?.luck || 1
            },
            
            // Appearance
            appearance: {
                face: options.appearance?.face || 'face1',
                hair: options.appearance?.hair || 'short',
                clothes: options.appearance?.clothes || 'casual',
                accessories: options.appearance?.accessories || 'none',
                skinTone: options.appearance?.skinTone || '#ffdbac'
            },
            
            // Progression
            rank: 'Geek Squad',
            xp: 0,
            level: 1,
            
            // Inventory
            wallet: {
                btc: 0,
                eth: 0,
                bch: 0
            },
            items: [],
            achievements: [],
            
            // Mission tracking
            missionsCompleted: 0,
            puzzlesSolved: 0,
            fightsWon: 0,
            peopleRescued: 0,
            
            createdAt: new Date(),
            lastActive: new Date()
        };

        return character;
    }

    /**
     * Generate unique character ID
     */
    generateCharacterId() {
        return `char_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
    }

    /**
     * Add XP and check for rank up
     */
    addXP(character, amount) {
        character.xp += amount;
        
        // Check for rank up
        const newRank = this.calculateRank(character.xp);
        if (newRank !== character.rank) {
            const oldRank = character.rank;
            character.rank = newRank;
            return {
                rankedUp: true,
                oldRank,
                newRank,
                message: `🎉 RANK UP! ${oldRank} → ${newRank}`
            };
        }
        
        return { rankedUp: false };
    }

    /**
     * Calculate rank based on XP
     */
    calculateRank(xp) {
        for (let i = this.rankProgression.length - 1; i >= 0; i--) {
            if (xp >= this.rankProgression[i].minXP) {
                return this.rankProgression[i].rank;
            }
        }
        return 'Geek Squad';
    }

    /**
     * Customize appearance
     */
    customizeAppearance(character, changes) {
        if (changes.face && this.appearances.faces.includes(changes.face)) {
            character.appearance.face = changes.face;
        }
        if (changes.hair && this.appearances.hair.includes(changes.hair)) {
            character.appearance.hair = changes.hair;
        }
        if (changes.clothes && this.appearances.clothes.includes(changes.clothes)) {
            character.appearance.clothes = changes.clothes;
        }
        if (changes.accessories && this.appearances.accessories.includes(changes.accessories)) {
            character.appearance.accessories = changes.accessories;
        }
        if (changes.skinTone) {
            character.appearance.skinTone = changes.skinTone;
        }
        
        return character;
    }

    /**
     * Upgrade character stats
     */
    upgradeStat(character, statName, amount) {
        if (character.stats[statName] !== undefined) {
            character.stats[statName] += amount;
            return {
                success: true,
                message: `${statName} increased by ${amount}!`,
                newValue: character.stats[statName]
            };
        }
        return { success: false, message: 'Invalid stat name' };
    }

    /**
     * Get character HTML for display
     */
    getCharacterHTML(character) {
        return `
            <div class="character-card">
                <div class="character-avatar">
                    <div class="avatar-display" style="background: ${character.appearance.skinTone}">
                        ${character.appearance.face}
                    </div>
                </div>
                <div class="character-info">
                    <h3>${character.name}</h3>
                    <div class="rank-badge">${character.rank}</div>
                    <div class="xp-bar">
                        <div class="xp-fill" style="width: ${this.getXPProgress(character)}%"></div>
                        <span>${character.xp} XP</span>
                    </div>
                </div>
                <div class="character-stats">
                    <div class="stat">🔓 Hacking: ${character.stats.hacking}</div>
                    <div class="stat">👊 Fighting: ${character.stats.fighting}</div>
                    <div class="stat">🧠 Intelligence: ${character.stats.intelligence}</div>
                    <div class="stat">🍀 Luck: ${character.stats.luck}</div>
                </div>
                <div class="character-achievements">
                    <div>🎯 Missions: ${character.missionsCompleted}</div>
                    <div>🧩 Puzzles: ${character.puzzlesSolved}</div>
                    <div>⚔️ Fights: ${character.fightsWon}</div>
                    <div>🚑 Rescued: ${character.peopleRescued}</div>
                </div>
            </div>
        `;
    }

    /**
     * Get XP progress to next rank (percentage)
     */
    getXPProgress(character) {
        const currentRankIndex = this.rankProgression.findIndex(r => r.rank === character.rank);
        if (currentRankIndex === this.rankProgression.length - 1) return 100;
        
        const current = this.rankProgression[currentRankIndex];
        const next = this.rankProgression[currentRankIndex + 1];
        
        const progress = ((character.xp - current.minXP) / (next.minXP - current.minXP)) * 100;
        return Math.min(100, Math.max(0, progress));
    }
}

module.exports = { CharacterCreation };
