/**
 * AI REFERENCE LIBRARIES
 * 
 * Critical libraries the AI must study regularly for address-to-public-key derivation
 */

const REFERENCE_LIBRARIES = {
    /**
     * TRUSTWALLET CORE (GitHub: trustwallet/wallet-core)
     * Cross-platform, cross-blockchain wallet library - 130+ blockchains
     * 
     * CRITICAL FOR AI LEARNING:
     * - C++ core implementation with strict C interfaces
     * - BIP39, BIP44, BIP49, BIP84 derivation paths
     * - Trezor crypto library fork (cryptographic primitives)
     * - Multi-blockchain address generation patterns
     * - Protobuf cross-language serialization
     */
    trustWalletCore: {
        github: 'https://github.com/trustwallet/wallet-core',
        installed: true,  // Already in package: @trustwallet/wallet-core
        license: 'Apache 2.0',
        languages: ['C++', 'Rust', 'Swift', 'Java/Kotlin'],
        
        keyDirectories: {
            'src/': 'C++ core blockchain implementations',
            'src/proto/': 'Protobuf blockchain interfaces',
            'include/TrustWalletCore/': 'Public API headers (TW prefix)',
            'rust/chains/': 'Rust blockchain implementations',
            'trezor-crypto/': 'Cryptographic primitives (CRITICAL)',
            'registry.json': 'Master blockchain definitions'
        },
        
        criticalFiles: [
            'src/Bitcoin/Address.cpp',
            'src/Bitcoin/Entry.cpp',
            'src/Bitcoin/Signer.cpp',
            'src/PrivateKey.cpp',
            'src/PublicKey.cpp',
            'src/Hash.cpp',
            'trezor-crypto/secp256k1.c',
            'trezor-crypto/ecdsa.c',
            'trezor-crypto/address.c',
            'registry.json'
        ],
        
        learningGoals: [
            'Study how TrustWallet derives addresses from keys (forward direction)',
            'Learn cryptographic primitives from trezor-crypto',
            'Understand BIP32/39/44 HD derivation implementations',
            'Study secp256k1 point multiplication patterns',
            'Analyze Base58Check encoding/decoding',
            'Learn hash function chains (SHA256, RIPEMD160)',
            'Understand how to REVERSE these processes'
        ],
        
        aiInstructions: `
            TrustWallet Core shows the STANDARD forward direction (private key → address).
            AI must study this to understand the REVERSE (address → public key).
            
            Key insights for reverse engineering:
            1. Address structure reveals hash operations used
            2. Public key format (compressed/uncompressed) affects address
            3. Network byte prefixes indicate blockchain type
            4. Base58Check contains checksums that can be validated
            5. Character sets reveal encoding patterns
            6. HD derivation paths show key relationships
            
            Study these patterns to build REVERSE algorithm.
        `
    },
    
    /**
     * KAZUKI/KAZULI PHONETIC IMPLEMENTATION
     * Files the user provided long ago with phonetic character set analysis
     * 
     * LOCATION: To be found in Drive imports or old uploaded files
     */
    kazukiPhonetic: {
        status: 'SEARCHING',
        expectedLocation: 'Drive imports or old files from user',
        possibleNames: [
            'kazuki_phonetic.py',
            'kazuli_solver.py',
            'phonetic_analysis.py',
            'charset_phonetic.py'
        ],
        
        expectedFeatures: [
            'Phonetic character set mappings',
            'International Phonetic Alphabet (IPA) usage',
            'Character set rotation algorithms',
            'Concatenation marker detection',
            'Recursive matching patterns',
            'Address-to-public-key reverse logic'
        ],
        
        aiInstructions: `
            Once located, study Kazuki/Kazuli implementation regularly.
            This likely contains the EXACT phonetic algorithm for:
            - Mapping Bitcoin operations to character sets
            - Using IPA for gap-filling
            - Applying character set rotations
            - Endpoint -1 offset calculations
            - Quiet concatenation technology
        `
    },
    
    /**
     * BTCKEYGEN.COM FILES
     * Visual Bitcoin private key generator
     */
    btcKeygenFiles: {
        github: 'https://github.com/MrFreeDragon/VisualBTC',
        zipUrl: 'https://btckeygen.com/archive/visualBTC.zip',
        
        criticalFiles: {
            'bitcoin.js': {
                status: 'SEARCHING',
                expectedContent: 'Bitcoin cryptographic operations implementation',
                learningGoals: [
                    'Study secp256k1 implementation',
                    'Learn public key derivation from private key',
                    'Understand address generation from public key',
                    'Analyze Base58 encoding/decoding'
                ]
            },
            'common.js': {
                status: 'FOUND ✅',
                location: './common.js',
                content: 'Complete character set library',
                features: [
                    'IANA character sets (ISO-8859-1 through ISO-8859-15)',
                    'Bitcoin-specific charsets (BASE58, HEX, BECH32)',
                    'Character set detection and conversion',
                    'Base conversion utilities',
                    'Sequence generation'
                ]
            }
        }
    },
    
    /**
     * EXISTING PROJECT FILES
     * Files already in the CRYPTO HEIST platform
     */
    existingFiles: {
        'common.js': {
            status: 'FOUND ✅',
            aiStudyFrequency: 'DAILY',
            content: 'Complete IANA and Bitcoin character sets'
        },
        'attached_assets/character-sets_1758872417126.txt': {
            status: 'FOUND ✅',
            aiStudyFrequency: 'MONTHLY',
            content: 'Official IANA Character Sets Registry (834 lines) - Reference only',
            features: [
                'Internet Assigned Numbers Authority character sets',
                'ISO-8859-1 through ISO-8859-15 registry',
                'MIBenum values for character set identification',
                'Aliases and reference documentation',
                'International character set standards'
            ],
            note: 'Registry only - See src/latin-iana-charsets.js for actual mappings'
        },
        'src/latin-iana-charsets.js': {
            status: 'CREATED ✅',
            aiStudyFrequency: 'WEEKLY',
            content: 'ACTUAL Latin IANA character mappings (0x00-0xFF)',
            features: [
                'ISO-8859-1 complete character table (Western European)',
                'ISO-8859-2 complete character table (Central European)',
                'ISO-8859-15 with Euro sign (€)',
                'Windows-1252 (web browser standard)',
                'Helper functions: getChar(), getAllChars(), analyzeHex()',
                'Phonetic analysis support for address-to-pubkey derivation'
            ],
            criticalForAI: [
                'Use for character set rotation in phonetic analysis',
                'Hex code to actual character conversion',
                'Pattern matching across different Latin character sets',
                'Gap-filling when algorithm needs character set mapping'
            ]
        },
        'src/ai-bitcoin-operations-phonetic.js': {
            status: 'CREATED ✅',
            aiStudyFrequency: 'DAILY',
            content: '36 Bitcoin operations + IPA + Latin IANA + UTF-16 + ASCII + HD + 360° array'
        },
        'src/ai-phonetic-wordbank-correction.js': {
            status: 'CREATED ✅',
            aiStudyFrequency: 'DAILY',
            content: 'Character set rules and correction logic'
        },
        'src/ai-study-scheduler.js': {
            status: 'CREATED ✅',
            aiStudyFrequency: 'WEEKLY',
            content: 'Study schedule and progress tracking'
        },
        'btckeygen/keygen_script.py': {
            status: 'FOUND ✅',
            aiStudyFrequency: 'WEEKLY',
            content: 'Standard Bitcoin key generation (forward direction)'
        },
        'puzzle71-analysis/puzzle71_solver.py': {
            status: 'FOUND ✅',
            aiStudyFrequency: 'WEEKLY',
            content: 'Puzzle 71 brute force solver (standard method)'
        }
    }
};

/**
 * AI STUDY PRIORITY MATRIX
 */
const STUDY_PRIORITY = {
    criticalDaily: [
        'common.js - Character set library',
        'src/ai-bitcoin-operations-phonetic.js - 36 operations + phonetic sets',
        'TrustWallet trezor-crypto/ - Cryptographic primitives'
    ],
    
    importantWeekly: [
        'TrustWallet src/Bitcoin/ - Bitcoin implementation',
        'Kazuki/Kazuli phonetic files (once found)',
        'bitcoin.js from btckeygen (once found)',
        'src/ai-phonetic-wordbank-correction.js'
    ],
    
    reviewMonthly: [
        'TrustWallet registry.json - Blockchain definitions',
        'btckeygen/keygen_script.py',
        'puzzle71-analysis/puzzle71_solver.py',
        'src/ai-study-scheduler.js'
    ]
};

/**
 * INTEGRATION CHECKLIST
 */
const INTEGRATION_CHECKLIST = {
    trustWalletCore: {
        packageInstalled: true,  // @trustwallet/wallet-core in package.json
        needsStudy: true,
        files: [
            'node_modules/@trustwallet/wallet-core/**/*.js',
            'GitHub: trustwallet/wallet-core (C++ source)'
        ]
    },
    
    kazukiPhonetic: {
        located: false,
        searchLocations: [
            'Drive imports',
            'Old uploaded files',
            'Hidden directories'
        ],
        action: 'SEARCH DRIVE IMPORTS'
    },
    
    btckeygen: {
        commonJs: true,
        bitcoinJs: false,
        action: 'DOWNLOAD FROM GITHUB OR FIND IN DRIVE'
    }
};

/**
 * GITHUB DOWNLOAD INSTRUCTIONS
 */
const GITHUB_DOWNLOAD = {
    trustWallet: {
        repo: 'https://github.com/trustwallet/wallet-core',
        command: 'git clone https://github.com/trustwallet/wallet-core.git trustwallet-core-study',
        studyFiles: [
            'trustwallet-core-study/trezor-crypto/**/*.c',
            'trustwallet-core-study/src/Bitcoin/**/*.cpp',
            'trustwallet-core-study/include/TrustWalletCore/*.h'
        ]
    },
    
    btckeygen: {
        repo: 'https://github.com/MrFreeDragon/VisualBTC',
        command: 'git clone https://github.com/MrFreeDragon/VisualBTC.git btckeygen-study',
        studyFiles: [
            'btckeygen-study/bitcoin.js',
            'btckeygen-study/common.js',
            'btckeygen-study/index.html'
        ]
    }
};

module.exports = {
    REFERENCE_LIBRARIES,
    STUDY_PRIORITY,
    INTEGRATION_CHECKLIST,
    GITHUB_DOWNLOAD
};
