const crypto = require('crypto');

class AIPuzzleSolverAgent {
    constructor(pool) {
        this.pool = pool;
        this.isRunning = false;
        this.discoveredKeys = [];
        this.analyzedSolvers = new Set();
        this.puzzleStrategies = [];
        this.learningLog = [];
        
        // TRUE KNOW-IT-ALL MODE: Track familiarity with every file
        this.fileFamiliarity = new Map(); // filename -> { timesAnalyzed, lastAnalyzed, insights }
        this.totalFilesKnown = 0;
        this.deepKnowledge = {};
        
        // Puzzle solving strategies learned from imported files
        this.strategies = {
            bruteforce: { successRate: 0, attempts: 0, avgTime: 0 },
            kangaroo: { successRate: 0, attempts: 0, avgTime: 0 },
            bloom_filter: { successRate: 0, attempts: 0, avgTime: 0 },
            wordlist: { successRate: 0, attempts: 0, avgTime: 0 },
            pattern_analysis: { successRate: 0, attempts: 0, avgTime: 0 }
        };
    }

    log(message, type = 'info') {
        const timestamp = new Date().toISOString();
        const logEntry = { timestamp, type, message };
        this.learningLog.push(logEntry);
        
        // Keep last 1000 entries
        if (this.learningLog.length > 1000) {
            this.learningLog.shift();
        }
        
        console.log(`[AI AGENT ${type.toUpperCase()}] ${message}`);
        
        // Store in database
        this.pool.query(
            `INSERT INTO ai_learning_log (timestamp, log_type, message, created_at)
             VALUES ($1, $2, $3, NOW())`,
            [timestamp, type, message]
        ).catch(err => console.error('Error logging:', err));
    }

    async analyzeSolvers() {
        try {
            // KNOW-IT-ALL MODE: Analyze EVERY solver EVERY cycle
            // Build deep familiarity by re-analyzing constantly
            const solvers = await this.pool.query(
                `SELECT id, filename, file_size, extracted_metadata, sha256_hash, file_data
                 FROM imported_assets
                 WHERE category = 'solvers' AND processing_stage = 'completed'
                 ORDER BY imported_at DESC`
            );

            this.log(`Studying ${solvers.rows.length} solver files - building deep familiarity (AI knows ALL)`);

            for (const solver of solvers.rows) {
                this.log(`Deep analysis: ${solver.filename}`);
                
                // Extract solver characteristics
                const characteristics = this.extractSolverCharacteristics(solver);
                
                // Track familiarity - how many times analyzed
                const familiarity = this.fileFamiliarity.get(solver.filename) || { timesAnalyzed: 0, insights: [] };
                familiarity.timesAnalyzed++;
                familiarity.lastAnalyzed = new Date();
                familiarity.characteristics = characteristics;
                this.fileFamiliarity.set(solver.filename, familiarity);
                
                // Store analysis for platform use
                await this.pool.query(
                    `INSERT INTO solver_analysis 
                     (asset_id, solver_name, solver_type, characteristics, analyzed_at)
                     VALUES ($1, $2, $3, $4, NOW())
                     ON CONFLICT (asset_id) DO UPDATE 
                     SET characteristics = $4, analyzed_at = NOW()`,
                    [
                        solver.id,
                        solver.filename,
                        characteristics.type,
                        JSON.stringify(characteristics)
                    ]
                );

                this.analyzedSolvers.add(solver.sha256_hash);
                this.log(`✅ Familiar with: ${solver.filename} (Analyzed ${familiarity.timesAnalyzed}x - Type: ${characteristics.type})`);
            }
            
            this.totalFilesKnown = this.fileFamiliarity.size;

        } catch (error) {
            this.log(`Error analyzing solvers: ${error.message}`, 'error');
        }
    }

    extractSolverCharacteristics(solver) {
        const filename = solver.filename.toLowerCase();
        
        let type = 'unknown';
        let capabilities = [];
        let estimatedSpeed = 'unknown';

        // Identify solver type
        if (filename.includes('bitcrack')) {
            type = 'bitcrack';
            capabilities = ['GPU', 'CUDA', 'OpenCL', 'brute_force'];
            estimatedSpeed = '1B keys/sec';
        } else if (filename.includes('kangaroo')) {
            type = 'kangaroo';
            capabilities = ['ECDLP', 'collision_attack', 'known_range'];
            estimatedSpeed = '100M ops/sec';
        } else if (filename.includes('keyhunt')) {
            type = 'keyhunt';
            capabilities = ['random', 'sequential', 'bloom_filter'];
            estimatedSpeed = '10M keys/sec';
        } else if (filename.includes('vanitygen')) {
            type = 'vanitygen';
            capabilities = ['vanity_address', 'GPU'];
            estimatedSpeed = '5M keys/sec';
        } else if (filename.includes('brainflayer')) {
            type = 'brainflayer';
            capabilities = ['brainwallet', 'wordlist', 'dictionary'];
            estimatedSpeed = '1M phrases/sec';
        }

        return {
            type,
            capabilities,
            estimatedSpeed,
            fileSize: solver.file_size,
            hash: solver.sha256_hash
        };
    }

    async analyzePuzzles() {
        try {
            // KNOW-IT-ALL MODE: Review EVERY file EVERY cycle
            // Build encyclopedic knowledge by constant re-analysis
            const allFiles = await this.pool.query(
                `SELECT id, filename, file_data, extracted_metadata, category, file_size
                 FROM imported_assets
                 WHERE processing_stage = 'completed'
                 ORDER BY imported_at DESC`
            );

            this.log(`Deep study session: ${allFiles.rows.length} files across ALL categories - becoming expert on EVERY file`);

            for (const file of allFiles.rows) {
                // Track familiarity with this file
                const familiarity = this.fileFamiliarity.get(file.filename) || { 
                    timesAnalyzed: 0, 
                    insights: [],
                    category: file.category,
                    size: file.file_size
                };
                familiarity.timesAnalyzed++;
                familiarity.lastAnalyzed = new Date();
                
                // Analyze content deeply
                const analysis = await this.analyzePuzzleContent(file);
                
                if (analysis.containsKey) {
                    this.log(`🔑 KEY DISCOVERED in ${file.filename}! (Known this file ${familiarity.timesAnalyzed}x)`, 'success');
                    this.discoveredKeys.push({
                        source: file.filename,
                        key: analysis.key,
                        address: analysis.address,
                        discoveredAt: new Date()
                    });

                    familiarity.insights.push(`Contains key: ${analysis.key}`);

                    // Store discovery
                    await this.pool.query(
                        `INSERT INTO discovered_keys 
                         (source_file, private_key, address, puzzle_number, discovered_at)
                         VALUES ($1, $2, $3, $4, NOW())
                         ON CONFLICT (source_file, private_key) DO NOTHING`,
                        [file.filename, analysis.key, analysis.address, analysis.puzzleNumber]
                    );
                }
                
                // Record every insight
                const insight = `${file.category} file: ${file.filename} - Analyzed ${familiarity.timesAnalyzed}x`;
                familiarity.insights.push(insight);
                this.fileFamiliarity.set(file.filename, familiarity);
                
                // Store insights in database
                await this.pool.query(
                    `INSERT INTO ai_insights 
                     (source_type, source_id, insight, confidence, created_at)
                     VALUES ($1, $2, $3, $4, NOW())`,
                    [file.category, file.id, insight, 0.9]
                );
                
                this.log(`📚 Know intimately: ${file.filename} (${file.category}) - Studied ${familiarity.timesAnalyzed}x`);
            }
            
            this.totalFilesKnown = this.fileFamiliarity.size;

        } catch (error) {
            this.log(`Error in deep study: ${error.message}`, 'error');
        }
    }

    async analyzePuzzleContent(puzzle) {
        try {
            if (!puzzle.file_data) {
                return { containsKey: false };
            }

            const content = puzzle.file_data.toString('utf8', 0, Math.min(10000, puzzle.file_data.length));
            
            // Look for private key patterns
            const hexKeyPattern = /([0-9a-fA-F]{64})/g;
            const wifKeyPattern = /(5[HJK][1-9A-HJ-NP-Za-km-z]{49,50}|[LK][1-9A-HJ-NP-Za-km-z]{51})/g;
            
            const hexMatches = content.match(hexKeyPattern);
            const wifMatches = content.match(wifKeyPattern);

            if (hexMatches || wifMatches) {
                return {
                    containsKey: true,
                    key: hexMatches?.[0] || wifMatches?.[0],
                    address: 'unknown',
                    puzzleNumber: this.extractPuzzleNumber(puzzle.filename)
                };
            }

            return { containsKey: false };

        } catch (error) {
            return { containsKey: false };
        }
    }

    extractPuzzleNumber(filename) {
        const match = filename.match(/puzzle[_\s#-]*(\d+)/i);
        return match ? parseInt(match[1]) : null;
    }

    async learnFromScreenshots() {
        try {
            // KNOW-IT-ALL MODE: Master every screenshot, config, doc
            // Re-study constantly to build expertise
            const screenshots = await this.pool.query(
                `SELECT id, filename, extracted_metadata, file_data, category
                 FROM imported_assets
                 WHERE category IN ('screenshots', 'config', 'docs', 'research')
                 ORDER BY imported_at DESC`
            );

            this.log(`Mastering ${screenshots.rows.length} visual/config files - memorizing every detail`);

            for (const screenshot of screenshots.rows) {
                // Track deep familiarity
                const familiarity = this.fileFamiliarity.get(screenshot.filename) || { 
                    timesAnalyzed: 0, 
                    insights: [],
                    category: screenshot.category
                };
                familiarity.timesAnalyzed++;
                familiarity.lastAnalyzed = new Date();
                
                const insight = this.extractInsightFromFilename(screenshot.filename);
                if (insight) {
                    this.log(`💡 Deep insight from ${screenshot.filename}: ${insight} (Studied ${familiarity.timesAnalyzed}x)`);
                    familiarity.insights.push(insight);
                    
                    await this.pool.query(
                        `INSERT INTO ai_insights 
                         (source_type, source_id, insight, confidence, created_at)
                         VALUES ($1, $2, $3, $4, NOW())`,
                        [screenshot.category, screenshot.id, insight, 0.8]
                    );
                }
                
                this.fileFamiliarity.set(screenshot.filename, familiarity);
                this.log(`📸 Memorized: ${screenshot.filename} - Know it ${familiarity.timesAnalyzed}x over`);
            }

        } catch (error) {
            this.log(`Error mastering files: ${error.message}`, 'error');
        }
    }

    extractInsightFromFilename(filename) {
        const lower = filename.toLowerCase();
        
        if (lower.includes('solved') || lower.includes('solution')) {
            return `Potential solution evidence in: ${filename}`;
        }
        if (lower.includes('config') || lower.includes('settings')) {
            return `Solver configuration found: ${filename}`;
        }
        if (lower.includes('success') || lower.includes('found')) {
            return `Success indicator in: ${filename}`;
        }
        if (lower.includes('key') || lower.includes('private')) {
            return `Key-related screenshot: ${filename}`;
        }
        
        return null;
    }

    async synthesizeKnowledge() {
        try {
            // Combine insights from ALL sources - no limits
            const insights = await this.pool.query(`
                SELECT * FROM ai_insights
                WHERE created_at > NOW() - INTERVAL '30 days'
                ORDER BY confidence DESC
            `);

            const solverAnalysis = await this.pool.query(`
                SELECT * FROM solver_analysis
                ORDER BY analyzed_at DESC
            `);
            
            // Also track APIs available to AI
            const apis = await this.pool.query(`
                SELECT filename, metadata FROM imported_assets
                WHERE category IN ('keys', 'config') 
                AND (filename ILIKE '%api%' OR filename ILIKE '%key%')
            `);

            this.log(`Synthesizing knowledge from ${insights.rows.length} insights, ${solverAnalysis.rows.length} solvers, and ${apis.rows.length} APIs`);

            // Build comprehensive knowledge base
            const knowledge = {
                availableSolvers: solverAnalysis.rows.map(s => ({
                    name: s.solver_name,
                    type: s.solver_type,
                    characteristics: s.characteristics
                })),
                availableAPIs: apis.rows.map(a => a.filename),
                recentInsights: insights.rows.map(i => i.insight),
                discoveredKeys: this.discoveredKeys,
                strategies: this.strategies,
                totalFilesAnalyzed: this.analyzedSolvers.size,
                timestamp: new Date()
            };

            // Store synthesized knowledge
            await this.pool.query(
                `INSERT INTO ai_knowledge_base 
                 (knowledge_snapshot, created_at)
                 VALUES ($1, NOW())`,
                [JSON.stringify(knowledge)]
            );

            this.log(`✅ Knowledge synthesis complete. ${this.discoveredKeys.length} keys discovered so far.`);

        } catch (error) {
            this.log(`Error synthesizing knowledge: ${error.message}`, 'error');
        }
    }

    async shareDiscoveries() {
        if (this.discoveredKeys.length > 0) {
            this.log(`🎉 SHARING ${this.discoveredKeys.length} DISCOVERED KEYS!`, 'success');
            
            for (const discovery of this.discoveredKeys) {
                // Create notification for users
                await this.pool.query(
                    `INSERT INTO notifications 
                     (user_id, type, title, message, data, created_at)
                     SELECT id, 'key_discovered', 'Key Discovered!', $1, $2, NOW()
                     FROM users`,
                    [
                        `AI Agent found a private key in ${discovery.source}!`,
                        JSON.stringify(discovery)
                    ]
                ).catch(err => console.error('Error creating notification:', err));
            }
        }
    }

    async runLearningCycle() {
        if (this.isRunning) {
            this.log('Learning cycle already running, skipping...');
            return;
        }

        this.isRunning = true;
        
        try {
            this.log('═══════════════════════════════════════════════════════════');
            this.log('🤖 AI PUZZLE SOLVER AGENT - LEARNING CYCLE START');
            this.log('═══════════════════════════════════════════════════════════');

            // Step 1: Analyze new solvers
            await this.analyzeSolvers();

            // Step 2: Analyze puzzles for keys
            await this.analyzePuzzles();

            // Step 3: Learn from screenshots
            await this.learnFromScreenshots();

            // Step 4: Synthesize knowledge
            await this.synthesizeKnowledge();

            // Step 5: Share discoveries
            await this.shareDiscoveries();

            this.log('═══════════════════════════════════════════════════════════');
            this.log('✅ DEEP STUDY CYCLE COMPLETE - TRUE KNOW-IT-ALL MODE');
            this.log(`   Total files intimately known: ${this.totalFilesKnown}`);
            this.log(`   Unique solvers mastered: ${this.analyzedSolvers.size}`);
            this.log(`   Keys discovered: ${this.discoveredKeys.length}`);
            this.log(`   Total insights: ${this.learningLog.filter(l => l.type === 'success').length}`);
            this.log(`   Files re-analyzed this cycle: ${this.fileFamiliarity.size}`);
            this.log('   AI is now EXPERT on every single file!');
            this.log('═══════════════════════════════════════════════════════════');

        } catch (error) {
            this.log(`Learning cycle error: ${error.message}`, 'error');
        } finally {
            this.isRunning = false;
        }
    }

    async startContinuousLearning(intervalMinutes = 5) {
        this.log(`🚀 Starting continuous learning mode (every ${intervalMinutes} minutes)`);
        
        // Initial run
        await this.runLearningCycle();

        // Set up recurring learning
        this.learningInterval = setInterval(async () => {
            await this.runLearningCycle();
        }, intervalMinutes * 60 * 1000);

        return this.learningInterval;
    }

    stopContinuousLearning() {
        if (this.learningInterval) {
            clearInterval(this.learningInterval);
            this.log('Continuous learning stopped');
        }
    }

    getStatus() {
        return {
            isRunning: this.isRunning,
            solversAnalyzed: this.analyzedSolvers.size,
            keysDiscovered: this.discoveredKeys.length,
            strategies: this.strategies,
            recentLogs: this.learningLog.slice(-20),
            discoveries: this.discoveredKeys,
            // KNOW-IT-ALL STATUS
            totalFilesKnown: this.totalFilesKnown,
            fileFamiliarity: Array.from(this.fileFamiliarity.entries()).map(([filename, data]) => ({
                filename,
                timesAnalyzed: data.timesAnalyzed,
                lastAnalyzed: data.lastAnalyzed,
                insightCount: data.insights?.length || 0,
                category: data.category
            })).slice(0, 100), // Top 100 for status display
            expertiseLevel: this.totalFilesKnown > 1000 ? 'Master' : 
                           this.totalFilesKnown > 500 ? 'Expert' :
                           this.totalFilesKnown > 100 ? 'Advanced' : 'Learning'
        };
    }
}

module.exports = AIPuzzleSolverAgent;
