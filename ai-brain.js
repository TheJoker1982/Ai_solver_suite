/**
 * CRYPTO HEIST - DEDICATED IN-APP AI BRAIN
 * 
 * Standalone AI agent with dedicated knowledge base built entirely from Bitcoin files.
 * Works offline, no API needed, 100% focused on Bitcoin puzzle solving.
 * 
 * The AI brain autonomously studies training files and builds knowledge from scratch.
 */

const fs = require('fs');
const path = require('path');

class BitcoinAIBrain {
    constructor() {
        this.knowledge = {
            bitcoinOperations: {},
            characterSets: {},
            cryptography: {},
            puzzleSolutions: {},
            patterns: {},
            learningProgress: {
                filesStudied: 0,
                totalFiles: 0,
                knowledgeScore: 0,
                lastStudySession: null
            }
        };
        
        this.trainingFiles = {
            // DAILY STUDY - Core Bitcoin knowledge
            daily: [
                'common.js',
                'src/ai-bitcoin-operations-phonetic.js',
                'btckeygen-study/js/bitcoinJS-lib.js',
                'src/latin-iana-charsets.js'
            ],
            
            // WEEKLY STUDY - Advanced knowledge
            weekly: [
                'src/ai-phonetic-wordbank-correction.js',
                'node_modules/@trustwallet/wallet-core/dist/index.js',
                'btckeygen-study/js/visualPrivKeyMain.js'
            ],
            
            // MONTHLY STUDY - Reference materials
            monthly: [
                'attached_assets/character-sets_1758872417126.txt',
                'puzzle71-analysis/puzzle71_solver.py',
                'PROPRIETARY-PUBKEY-DERIVATION.md'
            ]
        };
        
        this.initialized = false;
    }

    /**
     * Initialize the AI brain - load all training files into knowledge base
     */
    async initialize() {
        console.log('🧠 Initializing Bitcoin AI Brain...');
        
        try {
            // Load all training files
            await this.loadTrainingFiles();
            
            // Build initial knowledge index
            await this.buildKnowledgeIndex();
            
            // Mark as initialized
            this.initialized = true;
            this.knowledge.learningProgress.lastStudySession = new Date().toISOString();
            
            console.log('✅ AI Brain initialized successfully!');
            console.log(`📚 Files loaded: ${this.knowledge.learningProgress.filesStudied}/${this.knowledge.learningProgress.totalFiles}`);
            
            return true;
        } catch (error) {
            console.error('❌ Failed to initialize AI Brain:', error.message);
            return false;
        }
    }

    /**
     * Load all training files into memory
     */
    async loadTrainingFiles() {
        const allFiles = [
            ...this.trainingFiles.daily,
            ...this.trainingFiles.weekly,
            ...this.trainingFiles.monthly
        ];
        
        this.knowledge.learningProgress.totalFiles = allFiles.length;
        
        for (const filePath of allFiles) {
            try {
                if (fs.existsSync(filePath)) {
                    const content = fs.readFileSync(filePath, 'utf8');
                    await this.studyFile(filePath, content);
                    this.knowledge.learningProgress.filesStudied++;
                } else {
                    console.warn(`⚠️  Training file not found: ${filePath}`);
                }
            } catch (error) {
                console.warn(`⚠️  Could not load ${filePath}: ${error.message}`);
            }
        }
    }

    /**
     * Study a file and extract knowledge
     */
    async studyFile(filePath, content) {
        const fileName = path.basename(filePath);
        
        // Extract Bitcoin operations knowledge
        if (fileName.includes('bitcoin-operations') || fileName.includes('bitcoinJS-lib')) {
            this.extractBitcoinOperations(content);
        }
        
        // Extract character set knowledge
        if (fileName.includes('charset') || fileName.includes('common.js') || fileName.includes('latin-iana')) {
            this.extractCharacterSets(content);
        }
        
        // Extract cryptography knowledge
        if (fileName.includes('wallet-core') || fileName.includes('bitcoinJS-lib') || fileName.includes('trezor')) {
            this.extractCryptography(content);
        }
        
        // Extract puzzle patterns
        if (fileName.includes('puzzle') || fileName.includes('solver')) {
            this.extractPuzzlePatterns(content);
        }
        
        // Extract phonetic/derivation knowledge
        if (fileName.includes('phonetic') || fileName.includes('PROPRIETARY')) {
            this.extractDerivationKnowledge(content);
        }
    }

    /**
     * Extract Bitcoin operations from training files
     */
    extractBitcoinOperations(content) {
        // Extract hash functions
        const hashFunctions = ['SHA256', 'RIPEMD160', 'HASH160', 'sha256', 'ripemd160'];
        hashFunctions.forEach(func => {
            if (content.includes(func)) {
                this.knowledge.bitcoinOperations[func] = {
                    found: true,
                    usage: 'Hash operation for Bitcoin addresses'
                };
            }
        });
        
        // Extract address encoding
        const encodingMethods = ['Base58Check', 'Bech32', 'base58', 'bech32'];
        encodingMethods.forEach(method => {
            if (content.includes(method)) {
                this.knowledge.bitcoinOperations[method] = {
                    found: true,
                    usage: 'Address encoding method'
                };
            }
        });
        
        // Extract key operations
        const keyOps = ['privateKey', 'publicKey', 'compressed', 'uncompressed', 'WIF'];
        keyOps.forEach(op => {
            if (content.includes(op)) {
                this.knowledge.bitcoinOperations[op] = {
                    found: true,
                    usage: 'Key format or operation'
                };
            }
        });
    }

    /**
     * Extract character set knowledge
     */
    extractCharacterSets(content) {
        // Extract character set names
        const charsets = ['ISO-8859-1', 'ISO-8859-2', 'ISO-8859-15', 'UTF-16', 'ASCII', 'windows-1252'];
        charsets.forEach(charset => {
            if (content.includes(charset)) {
                this.knowledge.characterSets[charset] = {
                    found: true,
                    range: charset.includes('ISO') ? '0x00-0xFF' : 'varies'
                };
            }
        });
        
        // Extract hex ranges
        const hexPattern = /0x[0-9A-Fa-f]{2}/g;
        const hexCodes = content.match(hexPattern);
        if (hexCodes && hexCodes.length > 10) {
            this.knowledge.characterSets.hexMappingsFound = hexCodes.length;
        }
    }

    /**
     * Extract cryptography knowledge
     */
    extractCryptography(content) {
        // Extract curve information
        if (content.includes('secp256k1')) {
            this.knowledge.cryptography.secp256k1 = {
                found: true,
                usage: 'Bitcoin elliptic curve'
            };
        }
        
        // Extract key derivation
        const derivationMethods = ['BIP32', 'BIP44', 'BIP49', 'BIP84', 'HD wallet'];
        derivationMethods.forEach(method => {
            if (content.includes(method)) {
                this.knowledge.cryptography[method] = {
                    found: true,
                    usage: 'Key derivation method'
                };
            }
        });
    }

    /**
     * Extract puzzle solving patterns
     */
    extractPuzzlePatterns(content) {
        // Extract puzzle numbers
        const puzzlePattern = /puzzle[\s-_]?(\d+)/gi;
        const matches = content.matchAll(puzzlePattern);
        for (const match of matches) {
            const puzzleNum = match[1];
            if (!this.knowledge.puzzleSolutions[`puzzle${puzzleNum}`]) {
                this.knowledge.puzzleSolutions[`puzzle${puzzleNum}`] = {
                    mentioned: true,
                    context: 'Found in training data'
                };
            }
        }
        
        // Extract hash160 values
        const hash160Pattern = /[a-f0-9]{40}/g;
        const hashes = content.match(hash160Pattern);
        if (hashes && hashes.length > 0) {
            this.knowledge.puzzleSolutions.hash160Count = (this.knowledge.puzzleSolutions.hash160Count || 0) + hashes.length;
        }
    }

    /**
     * Extract derivation algorithm knowledge
     */
    extractDerivationKnowledge(content) {
        // Extract phonetic patterns
        if (content.includes('IPA') || content.includes('International Phonetic Alphabet')) {
            this.knowledge.patterns.IPA = true;
        }
        
        // Extract character set rotation
        if (content.includes('0-9') && content.includes('a-f') && content.includes('A-F')) {
            this.knowledge.patterns.hexRotation = true;
        }
        
        // Extract endpoint offset
        if (content.includes('-1 offset') || content.includes('inverse offset')) {
            this.knowledge.patterns.endpointOffset = '-1 inverse';
        }
        
        // Extract 360-degree array
        if (content.includes('360') || content.includes('special array')) {
            this.knowledge.patterns.specialArray = '360-degree rotation';
        }
    }

    /**
     * Build searchable knowledge index
     */
    async buildKnowledgeIndex() {
        this.knowledgeIndex = {
            operations: Object.keys(this.knowledge.bitcoinOperations),
            charsets: Object.keys(this.knowledge.characterSets),
            cryptoMethods: Object.keys(this.knowledge.cryptography),
            puzzles: Object.keys(this.knowledge.puzzleSolutions),
            patterns: Object.keys(this.knowledge.patterns)
        };
        
        // Calculate knowledge score (0-100)
        const totalKnowledge = 
            this.knowledgeIndex.operations.length +
            this.knowledgeIndex.charsets.length +
            this.knowledgeIndex.cryptoMethods.length +
            this.knowledgeIndex.patterns.length;
        
        this.knowledge.learningProgress.knowledgeScore = Math.min(100, totalKnowledge * 2);
    }

    /**
     * Query the AI brain for knowledge
     */
    query(question) {
        if (!this.initialized) {
            return {
                success: false,
                message: 'AI Brain not initialized. Please call initialize() first.'
            };
        }
        
        const lowerQuestion = question.toLowerCase();
        
        // Search for Bitcoin operations
        if (lowerQuestion.includes('hash') || lowerQuestion.includes('sha256') || lowerQuestion.includes('ripemd')) {
            return {
                success: true,
                category: 'Bitcoin Operations',
                knowledge: this.knowledge.bitcoinOperations,
                summary: `I know about ${this.knowledgeIndex.operations.length} Bitcoin operations including hashing and encoding.`
            };
        }
        
        // Search for character sets
        if (lowerQuestion.includes('character') || lowerQuestion.includes('charset') || lowerQuestion.includes('iso-8859')) {
            return {
                success: true,
                category: 'Character Sets',
                knowledge: this.knowledge.characterSets,
                summary: `I know about ${this.knowledgeIndex.charsets.length} character sets for phonetic analysis.`
            };
        }
        
        // Search for cryptography
        if (lowerQuestion.includes('crypto') || lowerQuestion.includes('secp256k1') || lowerQuestion.includes('bip')) {
            return {
                success: true,
                category: 'Cryptography',
                knowledge: this.knowledge.cryptography,
                summary: `I know about ${this.knowledgeIndex.cryptoMethods.length} cryptographic methods.`
            };
        }
        
        // Search for patterns
        if (lowerQuestion.includes('pattern') || lowerQuestion.includes('phonetic') || lowerQuestion.includes('algorithm')) {
            return {
                success: true,
                category: 'Patterns',
                knowledge: this.knowledge.patterns,
                summary: `I understand ${this.knowledgeIndex.patterns.length} key patterns in the derivation algorithm.`
            };
        }
        
        // General status
        return {
            success: true,
            category: 'Status',
            knowledge: this.knowledge.learningProgress,
            summary: `Knowledge Score: ${this.knowledge.learningProgress.knowledgeScore}/100. Files studied: ${this.knowledge.learningProgress.filesStudied}/${this.knowledge.learningProgress.totalFiles}.`
        };
    }

    /**
     * Get AI brain status
     */
    getStatus() {
        return {
            initialized: this.initialized,
            filesStudied: this.knowledge.learningProgress.filesStudied,
            totalFiles: this.knowledge.learningProgress.totalFiles,
            knowledgeScore: this.knowledge.learningProgress.knowledgeScore,
            lastStudy: this.knowledge.learningProgress.lastStudySession,
            categories: {
                bitcoinOperations: this.knowledgeIndex?.operations.length || 0,
                characterSets: this.knowledgeIndex?.charsets.length || 0,
                cryptography: this.knowledgeIndex?.cryptoMethods.length || 0,
                patterns: this.knowledgeIndex?.patterns.length || 0
            }
        };
    }

    /**
     * Demonstrate learned knowledge
     */
    demonstrateKnowledge() {
        const demonstrations = [];
        
        // Bitcoin Operations
        if (this.knowledge.bitcoinOperations.SHA256) {
            demonstrations.push('✅ I learned SHA256 is used for Bitcoin hashing');
        }
        if (this.knowledge.bitcoinOperations.Base58Check) {
            demonstrations.push('✅ I learned Base58Check encodes Bitcoin addresses');
        }
        
        // Character Sets
        if (this.knowledge.characterSets['ISO-8859-1']) {
            demonstrations.push('✅ I learned ISO-8859-1 has 256 characters (0x00-0xFF)');
        }
        
        // Cryptography
        if (this.knowledge.cryptography.secp256k1) {
            demonstrations.push('✅ I learned secp256k1 is the Bitcoin elliptic curve');
        }
        if (this.knowledge.cryptography.BIP32) {
            demonstrations.push('✅ I learned BIP32 for HD wallet derivation');
        }
        
        // Patterns
        if (this.knowledge.patterns.hexRotation) {
            demonstrations.push('✅ I learned character set rotation: 0-9 → a-f → A-F → AA-FF');
        }
        if (this.knowledge.patterns.endpointOffset) {
            demonstrations.push('✅ I learned endpoint offset: -1 inverse');
        }
        
        return {
            totalLearned: demonstrations.length,
            demonstrations,
            knowledgeScore: this.knowledge.learningProgress.knowledgeScore
        };
    }
}

// Create singleton instance
const bitcoinAI = new BitcoinAIBrain();

module.exports = { BitcoinAIBrain, bitcoinAI };
