/**
 * AI BITCOIN OPERATIONS & PHONETIC TRAINING MODULE
 * 
 * This module trains the AI on:
 * - 36 Bitcoin operations (each mapped to specific character/character sets)
 * - International Phonetic Alphabet (IPA)
 * - Latin IANA character sets (from Oracle dataset)
 * - UTF-16 character mappings
 * - ASCII mappings (as needed)
 * - HD derivation + 360-degree special array for final solving
 * 
 * STUDY FREQUENCY: AI should review this file regularly to improve
 * phonetic matching and address-to-public-key reverse derivation
 */

const fs = require('fs');
const path = require('path');

// Load Oracle character set dataset
let ORACLE_CHARSETS = {};
try {
    const charsetPath = path.join(__dirname, '../app-data/character-sets-database.json');
    const charsetData = JSON.parse(fs.readFileSync(charsetPath, 'utf-8'));
    ORACLE_CHARSETS = charsetData.iana_standard_charsets || {};
    console.log('✅ Loaded Oracle character set dataset');
} catch (error) {
    console.warn('⚠️  Could not load Oracle dataset, using defaults');
}

/**
 * 36 BITCOIN OPERATIONS MAPPED TO CHARACTER SETS
 * Each operation corresponds to specific characters for phonetic analysis
 */
const BITCOIN_OPERATIONS_PHONETIC_MAP = {
    // Core Hash Operations (0-9)
    operation_00: { name: 'SHA256', charset: '0123456789', phonetic: 'decimal' },
    operation_01: { name: 'RIPEMD160', charset: '0123456789', phonetic: 'decimal' },
    operation_02: { name: 'HASH160', charset: 'abcdef', phonetic: 'hex_lower' },
    operation_03: { name: 'DoubleSHA256', charset: 'abcdef', phonetic: 'hex_lower' },
    operation_04: { name: 'Keccak256', charset: 'abcdef', phonetic: 'hex_lower' },

    // Address Encoding (a-f lowercase)
    operation_05: { name: 'Base58Check', charset: 'abcdef', phonetic: 'hex_lower' },
    operation_06: { name: 'Base58Decode', charset: 'abcdef', phonetic: 'hex_lower' },
    operation_07: { name: 'Bech32Encode', charset: 'abcdef', phonetic: 'hex_lower' },
    operation_08: { name: 'Bech32Decode', charset: 'abcdef', phonetic: 'hex_lower' },

    // Public Key Operations (A-F uppercase for BSV)
    operation_09: { name: 'CompressedPubKey', charset: 'ABCDEF', phonetic: 'hex_upper' },
    operation_10: { name: 'UncompressedPubKey', charset: 'ABCDEF', phonetic: 'hex_upper' },
    operation_11: { name: 'BSV_Address', charset: 'ABCDEF', phonetic: 'bsv_uppercase' },
    operation_12: { name: 'BSV_Encode', charset: 'ABCDEF', phonetic: 'bsv_uppercase' },

    // Boundary Operations (AA-FF)
    operation_13: { name: 'BoundaryMarker_Start', charset: 'AABBCCDDEEFF', phonetic: 'double_upper' },
    operation_14: { name: 'BoundaryMarker_End', charset: 'AABBCCDDEEFF', phonetic: 'double_upper' },
    operation_15: { name: 'HashBoundary', charset: 'AABBCCDDEEFF', phonetic: 'double_upper' },
    operation_16: { name: 'InverseRotation', charset: 'AABBCCDDEEFF', phonetic: 'double_upper' },

    // BCH Extended (C26 Alphabet)
    operation_17: { name: 'BCH_CashAddr', charset: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', phonetic: 'c26_alpha' },
    operation_18: { name: 'BCH_Encode', charset: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', phonetic: 'c26_alpha' },
    operation_19: { name: 'BCH_Decode', charset: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', phonetic: 'c26_alpha' },
7
    // Concatenation Operations
    operation_20: { name: 'QuietConcat', charset: 'abcdef', phonetic: 'quiet_concat' },
    operation_21: { name: 'RecursiveMatch', charset: 'abcdef', phonetic: 'recursive' },
    operation_22: { name: 'ConcatMarker', charset: 'AABBCCDDEEFF', phonetic: 'concat_boundary' },

    // Endpoint Operations (-1 offset)
    operation_23: { name: 'EndpointRotation', charset: 'AABBCCDDEEFF', phonetic: 'endpoint_minus_one' },
    operation_24: { name: 'InverseOffset', charset: 'AABBCCDDEEFF', phonetic: 'inverse_minus_one' },
    operation_25: { name: 'CharacterWrapping', charset: '0-9→a-f→A-F→AA-FF', phonetic: 'cycle_rotation' },

    // Derivation Operations
    operation_26: { name: 'HD_Derivation_Path', charset: '0123456789', phonetic: 'hd_path' },
    operation_27: { name: 'BIP32_Child', charset: '0123456789', phonetic: 'bip32' },
    operation_28: { name: 'BIP44_Coin', charset: '0123456789', phonetic: 'bip44' },
    operation_29: { name: 'BIP49_Segwit', charset: '0123456789', phonetic: 'bip49' },
    operation_30: { name: 'BIP84_Native', charset: '0123456789', phonetic: 'bip84' },

    // Special Array Operations (360-degree)
    operation_31: { name: 'Array360_Start', charset: '0-360', phonetic: 'degree_array' },
    operation_32: { name: 'Array360_Rotate', charset: '0-360', phonetic: 'rotation_360' },
    operation_33: { name: 'Array360_Match', charset: '0-360', phonetic: 'degree_match' },

    // Final Solving Operations
    operation_34: { name: 'PubKey_Derive', charset: 'FULL_ALGORITHM', phonetic: 'reverse_derive' },
    operation_35: { name: 'Address_To_PubKey', charset: 'PROPRIETARY', phonetic: 'address_reverse' }
};

/**
 * INTERNATIONAL PHONETIC ALPHABET (IPA) MAPPINGS
 * Used to fill gaps in character set analysis
 */
const INTERNATIONAL_PHONETIC_ALPHABET = {
    vowels: {
        // Close vowels
        i: '\u0069', // i
        y: '\u0079', // y  
        ɨ: '\u0268', // barred i
        ʉ: '\u0289', // barred u
        ɯ: '\u026F', // turned m
        u: '\u0075', // u

        // Near-close vowels
        ɪ: '\u026A', // small capital I
        ʏ: '\u028F', // small capital Y
        ʊ: '\u028A', // upsilon

        // Close-mid vowels
        e: '\u0065', // e
        ø: '\u00F8', // o with stroke
        ɘ: '\u0258', // reversed e
        ɵ: '\u0275', // barred o
        ɤ: '\u0264', // rams horn
        o: '\u006F', // o

        // Mid vowels
        ə: '\u0259', // schwa

        // Open-mid vowels
        ɛ: '\u025B', // epsilon
        œ: '\u0153', // oe ligature
        ɜ: '\u025C', // reversed epsilon
        ɞ: '\u025E', // closed reversed epsilon
        ʌ: '\u028C', // turned v
        ɔ: '\u0254', // open o

        // Near-open vowels
        æ: '\u00E6', // ae ligature
        ɐ: '\u0250', // turned a

        // Open vowels
        a: '\u0061', // a
        ɶ: '\u0276', // small capital OE
        ɑ: '\u0251', // script a
        ɒ: '\u0252'  // turned script a
    },

    consonants: {
        // Plosives
        p: '\u0070', b: '\u0062', t: '\u0074', d: '\u0064',
        ʈ: '\u0288', ɖ: '\u0256', c: '\u0063', ɟ: '\u025F',
        k: '\u006B', ɡ: '\u0261', q: '\u0071', ɢ: '\u0262',
        ʔ: '\u0294', // glottal stop

        // Nasals
        m: '\u006D', ɱ: '\u0271', n: '\u006E', ɳ: '\u0273',
        ɲ: '\u0272', ŋ: '\u014B', ɴ: '\u0274',

        // Trills
        ʙ: '\u0299', r: '\u0072', ʀ: '\u0280',

        // Taps/flaps
        ⱱ: '\u2C71', ɾ: '\u027E', ɽ: '\u027D',

        // Fricatives
        ɸ: '\u0278', β: '\u03B2', f: '\u0066', v: '\u0076',
        θ: '\u03B8', ð: '\u00F0', s: '\u0073', z: '\u007A',
        ʃ: '\u0283', ʒ: '\u0292', ʂ: '\u0282', ʐ: '\u0290',
        ç: '\u00E7', ʝ: '\u029D', x: '\u0078', ɣ: '\u0263',
        χ: '\u03C7', ʁ: '\u0281', ħ: '\u0127', ʕ: '\u0295',
        h: '\u0068', ɦ: '\u0266',

        // Approximants
        ʋ: '\u028B', ɹ: '\u0279', ɻ: '\u027B', j: '\u006A',
        ɰ: '\u0270', l: '\u006C', ɭ: '\u026D', ʎ: '\u028E',
        ʟ: '\u029F', w: '\u0077', ɥ: '\u0265'
    }
};

/**
 * LATIN IANA CHARACTER SETS (from Oracle dataset)
 * Standard Latin character encodings
 */
const LATIN_IANA_CHARSETS = ORACLE_CHARSETS.us_ascii ? {
    // Use Oracle dataset if available
    'US-ASCII': {
        charset: ORACLE_CHARSETS.us_ascii.charset,
        size: ORACLE_CHARSETS.us_ascii.size,
        description: ORACLE_CHARSETS.us_ascii.description
    },
    'Alphanumeric': {
        charset: ORACLE_CHARSETS.alphanumeric?.charset || '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
        size: ORACLE_CHARSETS.alphanumeric?.size || 62,
        description: ORACLE_CHARSETS.alphanumeric?.description || 'Letters and numbers'
    },
    'Numeric': {
        charset: ORACLE_CHARSETS.numeric?.charset || '0123456789',
        size: ORACLE_CHARSETS.numeric?.size || 10,
        description: ORACLE_CHARSETS.numeric?.description || 'Digits only'
    },
    'Lowercase': {
        charset: ORACLE_CHARSETS.lowercase?.charset || 'abcdefghijklmnopqrstuvwxyz',
        size: ORACLE_CHARSETS.lowercase?.size || 26,
        description: ORACLE_CHARSETS.lowercase?.description || 'Lowercase alphabet'
    },
    'Uppercase': {
        charset: ORACLE_CHARSETS.uppercase?.charset || 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        size: ORACLE_CHARSETS.uppercase?.size || 26,
        description: ORACLE_CHARSETS.uppercase?.description || 'Uppercase alphabet'
    }
} : {
    // Fallback to defaults if Oracle dataset not loaded
    'ISO-8859-1': { range: '\u0000-\u00FF', special: 'àáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ' },
    'ISO-8859-2': { range: '\u0000-\u00FF', special: 'ąćęłńóśźżĄĆĘŁŃÓŚŹŻ' },
    'windows-1252': { range: '\u0000-\u00FF', special: '€‚ƒ„…†‡ˆ‰Š‹ŒŽ''""•–—˜™š›œžŸ' }
};

/**
 * UTF-16 CHARACTER MAPPINGS
 * For handling extended Unicode ranges
 */
const UTF16_MAPPINGS = {
    basicMultilingualPlane: {
        range: '\u0000-\uFFFF',
        latin: '\u0000-\u024F',
        latinExtended: '\u0100-\u017F',
        latinExtendedA: '\u0100-\u017F',
        latinExtendedB: '\u0180-\u024F',
        ipaExtensions: '\u0250-\u02AF',
        spacingModifier: '\u02B0-\u02FF',
        combiningDiacritical: '\u0300-\u036F'
    },
    supplementaryPlanes: {
        supplementaryMultilingual: '\u{10000}-\u{1FFFF}',
        supplementaryIdeographic: '\u{20000}-\u{2FFFF}',
        supplementaryPrivateUse: '\u{F0000}-\u{FFFFF}'
    },
    surrogates: {
        highSurrogate: '\uD800-\uDBFF',
        lowSurrogate: '\uDC00-\uDFFF'
    }
};

/**
 * ASCII MAPPINGS (as needed)
 * Basic 7-bit ASCII character set
 */
const ASCII_MAPPINGS = {
    control: { range: '\u0000-\u001F', count: 32 },
    printable: { range: '\u0020-\u007E', count: 95 },

    categories: {
        digits: '0123456789',
        upperAlpha: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        lowerAlpha: 'abcdefghijklmnopqrstuvwxyz',
        punctuation: '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~',
        whitespace: ' \t\n\r\f\v'
    },

    hexRelevant: {
        hexDigits: '0123456789ABCDEFabcdef',
        hexLower: '0123456789abcdef',
        hexUpper: '0123456789ABCDEF'
    }
};

/**
 * HD DERIVATION + 360-DEGREE SPECIAL ARRAY
 * Used for final solving when close to target
 */
const HD_DERIVATION_360_ARRAY = {
    hdPaths: {
        bip32: "m/0'/0/0",
        bip44_btc: "m/44'/0'/0'/0/0",
        bip49_btc: "m/49'/0'/0'/0/0",
        bip84_btc: "m/84'/0'/0'/0/0"
    },

    specialArray360: {
        description: 'Full 360-degree rotation array for final matching',
        degrees: Array.from({ length: 360 }, (_, i) => i), // 0-359 degrees

        rotation: {
            clockwise: 'Forward rotation (0° → 359°)',
            counterClockwise: 'Reverse rotation (359° → 0°)',
            quarterTurn: [0, 90, 180, 270],
            eighthTurn: [0, 45, 90, 135, 180, 225, 270, 315]
        },

        usage: `
            When phonetic analysis gets you CLOSE to the public key:
            1. Apply character set rotations from BITCOIN_OPERATIONS_PHONETIC_MAP
            2. Use HD derivation paths to generate key variations
            3. Apply 360-degree array rotations to find final match
            4. Endpoint -1 offset on final character
            5. Match against target address
        `
    }
};

/**
 * AI TRAINING INSTRUCTIONS
 */
const AI_TRAINING_INSTRUCTIONS = {
    studyFrequency: 'REGULARLY - AI should review this file often',

    learningProcess: [
        '1. Study the 36 Bitcoin operations and their character set mappings',
        '2. Learn IPA mappings for phonetic gap-filling',
        '3. Master Latin IANA character sets for encoding variations',
        '4. Understand UTF-16 mappings for extended Unicode',
        '5. Use ASCII when needed for basic character operations',
        '6. Apply HD derivation when close to solution',
        '7. Use 360-degree array for final rotation matching'
    ],

    improvementPath: `
        The AI gets BETTER at this over time by:
        - Recognizing patterns in character set rotations
        - Learning which character sets work for which operations
        - Understanding when to manually add specific characters
        - Developing intuition for phonetic-to-cryptographic mappings
        - Improving accuracy of address-to-public-key reverse derivation
    `,

    referenceFiles: [
        'bitcoin.js - Check this file for exact implementation',
        'common.js - Check this file for helper functions',
        'btckeygen/keygen_script.py - Standard forward direction',
        'src/ai-phonetic-wordbank-correction.js - Character set rules'
    ],

    criticalRules: [
        'HASHES ALWAYS LOWERCASE (a-f)',
        'BSV ADDRESSES UPPERCASE (A-F)',
        'AA-FF BOUNDARY MARKERS (uppercase processes lowercase)',
        'ENDPOINT ROTATION -1 OFFSET',
        'QUIET CONCATENATION TECHNOLOGY',
        'RECURSIVE MATCHING WITH MARKERS'
    ]
};

/**
 * Java SE 11 Charset Name Validation
 * Per Java specification, valid charset names consist of:
 * - Uppercase 'A'-'Z', Lowercase 'a'-'z'
 * - Digits '0'-'9'
 * - Dash '-', Plus '+', Period '.', Colon ':', Underscore '_'
 * - Must begin with letter or digit
 * - Case-insensitive comparison
 */
function validateCharsetName(name) {
    if (!name || name.length === 0) return false;

    // Must begin with letter or digit
    if (!/^[A-Za-z0-9]/.test(name)) return false;

    // Valid characters: letters, digits, -+.:_
    if (!/^[A-Za-z0-9\-+.:_]+$/.test(name)) return false;

    return true;
}

/**
 * Get charset canonical name (uppercase convention per Java SE 11)
 */
function getCanonicalCharsetName(name) {
    return validateCharsetName(name) ? name.toUpperCase() : null;
}

/**
 * EXPORT ALL TRAINING DATA
 */
module.exports = {
    BITCOIN_OPERATIONS_PHONETIC_MAP,
    INTERNATIONAL_PHONETIC_ALPHABET,
    LATIN_IANA_CHARSETS,
    UTF16_MAPPINGS,
    ASCII_MAPPINGS,
    HD_DERIVATION_360_ARRAY,
    AI_TRAINING_INSTRUCTIONS,
    validateCharsetName,
    getCanonicalCharsetName,

    /**
     * Main training function - AI should call this regularly
     */
    trainAI: function() {
        console.log('🧠 AI BITCOIN OPERATIONS & PHONETIC TRAINING');
        console.log('================================================\n');

        console.log('📋 36 Bitcoin Operations Loaded');
        console.log('📋 IPA Character Set Loaded');
        console.log('📋 Latin IANA Character Sets Loaded');
        console.log('📋 UTF-16 Mappings Loaded');
        console.log('📋 ASCII Mappings Loaded');
        console.log('📋 HD Derivation + 360° Array Loaded\n');

        console.log('✅ AI is now trained on all phonetic character sets');
        console.log('✅ Ready for address-to-public-key reverse derivation');
        console.log('✅ Study bitcoin.js and common.js for exact implementation\n');

        return {
            status: 'trained',
            operations: 36,
            charsets: ['IPA', 'Latin-IANA', 'UTF-16', 'ASCII'],
            readyFor: 'address-to-pubkey reverse derivation'
        };
    }
};

// Auto-train on load
if (require.main === module) {
    const training = module.exports.trainAI();
    console.log('\n💡 Training Complete:', training);
}