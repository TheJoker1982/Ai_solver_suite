class AILearningEngine {
    constructor() {
        this.learningData = {
            userPatterns: {},
            toolUsageStats: {},
            successfulStrategies: [],
            errorPatterns: [],
            recommendations: []
        };
        this.sessionData = {
            toolsUsed: [],
            queriesAsked: [],
            puzzlesAttempted: [],
            timeSpent: {},
            successRate: {}
        };
        this.init();
    }

    init() {
        this.loadLearningData();
        this.setupEventListeners();
        this.startSessionTracking();
    }

    loadLearningData() {
        const saved = localStorage.getItem('ai_learning_data');
        if (saved) {
            try {
                this.learningData = JSON.parse(saved);
            } catch (e) {
                console.warn('Failed to load learning data:', e);
            }
        }
    }

    saveLearningData() {
        try {
            localStorage.setItem('ai_learning_data', JSON.stringify(this.learningData));
        } catch (e) {
            console.warn('Failed to save learning data:', e);
        }
    }

    setupEventListeners() {
        document.addEventListener('tool-used', (e) => this.trackToolUsage(e.detail));
        document.addEventListener('ai-query', (e) => this.trackQuery(e.detail));
        document.addEventListener('puzzle-attempt', (e) => this.trackPuzzleAttempt(e.detail));
        document.addEventListener('puzzle-solved', (e) => this.trackPuzzleSuccess(e.detail));
        document.addEventListener('error-occurred', (e) => this.trackError(e.detail));
    }

    startSessionTracking() {
        this.sessionStartTime = Date.now();
        setInterval(() => this.analyzeAndLearn(), 60000);
    }

    trackToolUsage(data) {
        const { toolName, timestamp, parameters, result } = data;
        
        this.sessionData.toolsUsed.push({
            tool: toolName,
            time: timestamp || Date.now(),
            params: parameters,
            success: result?.success || false
        });

        if (!this.learningData.toolUsageStats[toolName]) {
            this.learningData.toolUsageStats[toolName] = {
                totalUses: 0,
                successfulUses: 0,
                avgTimeSpent: 0,
                commonParameters: {},
                relatedTools: {}
            };
        }

        const stats = this.learningData.toolUsageStats[toolName];
        stats.totalUses++;
        if (result?.success) stats.successfulUses++;

        this.updateToolRelations(toolName);
        this.saveLearningData();
    }

    trackQuery(data) {
        const { query, response, satisfied } = data;
        
        this.sessionData.queriesAsked.push({
            query,
            response,
            satisfied: satisfied || false,
            timestamp: Date.now()
        });

        this.analyzeQueryPatterns(query);
    }

    trackPuzzleAttempt(data) {
        const { puzzleNumber, strategy, toolsUsed } = data;
        
        this.sessionData.puzzlesAttempted.push({
            puzzle: puzzleNumber,
            strategy,
            tools: toolsUsed,
            timestamp: Date.now()
        });

        toolsUsed.forEach(tool => {
            if (!this.sessionData.successRate[tool]) {
                this.sessionData.successRate[tool] = { attempts: 0, successes: 0 };
            }
            this.sessionData.successRate[tool].attempts++;
        });
    }

    trackPuzzleSuccess(data) {
        const { puzzleNumber, strategy, toolsUsed, timeSpent, btcAmount } = data;
        
        this.learningData.successfulStrategies.push({
            puzzle: puzzleNumber,
            strategy,
            tools: toolsUsed,
            duration: timeSpent,
            reward: btcAmount,
            timestamp: Date.now()
        });

        this.updateSuccessRates(toolsUsed);
        this.saveLearningData();
    }

    trackError(data) {
        const { error, context, tool } = data;
        
        this.learningData.errorPatterns.push({
            error,
            context,
            tool,
            timestamp: Date.now()
        });

        if (this.learningData.errorPatterns.length > 100) {
            this.learningData.errorPatterns = this.learningData.errorPatterns.slice(-50);
        }

        this.saveLearningData();
    }

    updateToolRelations(currentTool) {
        const recentTools = this.sessionData.toolsUsed.slice(-5);
        const stats = this.learningData.toolUsageStats[currentTool];
        
        recentTools.forEach(usage => {
            if (usage.tool !== currentTool) {
                if (!stats.relatedTools[usage.tool]) {
                    stats.relatedTools[usage.tool] = 0;
                }
                stats.relatedTools[usage.tool]++;
            }
        });
    }

    analyzeQueryPatterns(query) {
        const keywords = query.toLowerCase().split(' ')
            .filter(word => word.length > 3);
        
        keywords.forEach(keyword => {
            if (!this.learningData.userPatterns[keyword]) {
                this.learningData.userPatterns[keyword] = {
                    count: 0,
                    relatedTools: []
                };
            }
            this.learningData.userPatterns[keyword].count++;
        });
    }

    updateSuccessRates(toolsUsed) {
        toolsUsed.forEach(tool => {
            if (!this.sessionData.successRate[tool]) {
                this.sessionData.successRate[tool] = { attempts: 0, successes: 0 };
            }
            this.sessionData.successRate[tool].successes++;
        });
    }

    analyzeAndLearn() {
        this.generateRecommendations();
        this.identifyOptimalStrategies();
        this.detectUserPreferences();
        this.saveLearningData();
    }

    generateRecommendations() {
        this.learningData.recommendations = [];

        const toolStats = this.learningData.toolUsageStats;
        for (const [toolName, stats] of Object.entries(toolStats)) {
            if (stats.totalUses > 5 && stats.successfulUses / stats.totalUses < 0.5) {
                this.learningData.recommendations.push({
                    type: 'improvement',
                    tool: toolName,
                    message: `Your success rate with ${toolName} is low (${Math.round(stats.successfulUses / stats.totalUses * 100)}%). Consider reviewing the documentation or trying related tools.`,
                    relatedTools: Object.keys(stats.relatedTools).slice(0, 3)
                });
            }
        }

        const recentErrors = this.learningData.errorPatterns.slice(-10);
        const errorGroups = {};
        recentErrors.forEach(err => {
            const key = err.tool || 'general';
            errorGroups[key] = (errorGroups[key] || 0) + 1;
        });

        for (const [tool, count] of Object.entries(errorGroups)) {
            if (count > 3) {
                this.learningData.recommendations.push({
                    type: 'warning',
                    tool,
                    message: `Frequent errors detected with ${tool}. Double-check your parameters or try an alternative approach.`
                });
            }
        }

        const successStrategies = this.learningData.successfulStrategies.slice(-20);
        if (successStrategies.length > 0) {
            const toolFrequency = {};
            successStrategies.forEach(strategy => {
                strategy.tools.forEach(tool => {
                    toolFrequency[tool] = (toolFrequency[tool] || 0) + 1;
                });
            });

            const topTools = Object.entries(toolFrequency)
                .sort((a, b) => b[1] - a[1])
                .slice(0, 3)
                .map(([tool]) => tool);

            if (topTools.length > 0) {
                this.learningData.recommendations.push({
                    type: 'success',
                    message: `Your most successful tools are: ${topTools.join(', ')}. Keep using these for similar puzzles!`,
                    tools: topTools
                });
            }
        }
    }

    identifyOptimalStrategies() {
        const strategies = this.learningData.successfulStrategies.slice(-50);
        
        const strategyGroups = {};
        strategies.forEach(s => {
            const key = s.tools.sort().join('+');
            if (!strategyGroups[key]) {
                strategyGroups[key] = {
                    tools: s.tools,
                    count: 0,
                    totalTime: 0,
                    totalReward: 0
                };
            }
            strategyGroups[key].count++;
            strategyGroups[key].totalTime += s.duration || 0;
            strategyGroups[key].totalReward += parseFloat(s.reward) || 0;
        });

        return Object.values(strategyGroups)
            .sort((a, b) => b.totalReward - a.totalReward)
            .slice(0, 5);
    }

    detectUserPreferences() {
        const patterns = this.learningData.userPatterns;
        const topKeywords = Object.entries(patterns)
            .sort((a, b) => b[1].count - a[1].count)
            .slice(0, 10)
            .map(([keyword]) => keyword);

        return {
            interests: topKeywords,
            favoriteTools: this.getFavoriteTools(),
            activityLevel: this.getActivityLevel()
        };
    }

    getFavoriteTools() {
        return Object.entries(this.learningData.toolUsageStats)
            .sort((a, b) => b[1].totalUses - a[1].totalUses)
            .slice(0, 5)
            .map(([tool]) => tool);
    }

    getActivityLevel() {
        const sessionDuration = (Date.now() - this.sessionStartTime) / 1000 / 60;
        const actionsPerMinute = this.sessionData.toolsUsed.length / sessionDuration;
        
        if (actionsPerMinute > 2) return 'high';
        if (actionsPerMinute > 0.5) return 'medium';
        return 'low';
    }

    getSmartSuggestions(context = {}) {
        const suggestions = [];

        if (context.currentPuzzle) {
            const similarSuccess = this.learningData.successfulStrategies
                .filter(s => Math.abs(s.puzzle - context.currentPuzzle) <= 5)
                .slice(-3);

            if (similarSuccess.length > 0) {
                const toolSet = new Set();
                similarSuccess.forEach(s => s.tools.forEach(t => toolSet.add(t)));
                suggestions.push({
                    type: 'strategy',
                    message: `For similar puzzles, these tools were successful: ${Array.from(toolSet).join(', ')}`,
                    tools: Array.from(toolSet)
                });
            }
        }

        const recentTools = this.sessionData.toolsUsed.slice(-3).map(u => u.tool);
        if (recentTools.length > 0) {
            const lastTool = recentTools[recentTools.length - 1];
            const relatedTools = this.learningData.toolUsageStats[lastTool]?.relatedTools || {};
            const topRelated = Object.entries(relatedTools)
                .sort((a, b) => b[1] - a[1])
                .slice(0, 3)
                .map(([tool]) => tool);

            if (topRelated.length > 0) {
                suggestions.push({
                    type: 'next-step',
                    message: `After using ${lastTool}, users often use: ${topRelated.join(', ')}`,
                    tools: topRelated
                });
            }
        }

        return [...suggestions, ...this.learningData.recommendations.slice(0, 3)];
    }

    getPersonalizedGreeting() {
        const preferences = this.detectUserPreferences();
        const activityLevel = preferences.activityLevel;
        const favoriteTools = preferences.favoriteTools.slice(0, 2);

        const greetings = {
            high: `Welcome back, crypto hunter! You've been crushing it with ${favoriteTools.join(' and ')}. Ready for another run?`,
            medium: `Hey there! I noticed you've been making good progress with ${favoriteTools[0]}. Want to continue where you left off?`,
            low: `Welcome! Need help getting started? Your knowledge bank has ${Object.keys(this.learningData.toolUsageStats).length} tools ready to use.`
        };

        return greetings[activityLevel] || greetings.low;
    }

    exportLearningData() {
        return {
            summary: {
                totalToolsUsed: Object.keys(this.learningData.toolUsageStats).length,
                totalActions: Object.values(this.learningData.toolUsageStats)
                    .reduce((sum, stat) => sum + stat.totalUses, 0),
                puzzlesSolved: this.learningData.successfulStrategies.length,
                recommendations: this.learningData.recommendations.length
            },
            preferences: this.detectUserPreferences(),
            topStrategies: this.identifyOptimalStrategies(),
            recentRecommendations: this.learningData.recommendations.slice(0, 5)
        };
    }

    resetLearningData() {
        this.learningData = {
            userPatterns: {},
            toolUsageStats: {},
            successfulStrategies: [],
            errorPatterns: [],
            recommendations: []
        };
        this.saveLearningData();
    }
}

const aiLearning = new AILearningEngine();

if (typeof window !== 'undefined') {
    window.aiLearning = aiLearning;
}
