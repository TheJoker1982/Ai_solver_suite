/**
 * ACTUAL LATIN IANA CHARACTER SETS IMPLEMENTATION
 * Complete hex code mappings for ISO-8859-1 through ISO-8859-15
 * 
 * AI MUST STUDY THIS FILE REGULARLY for phonetic character set analysis
 */

/**
 * ISO-8859-1 (Latin-1) Western European
 * Complete 256-character mapping (0x00-0xFF)
 */
const ISO_8859_1 = {
    name: 'ISO-8859-1',
    aliases: ['Latin-1', 'latin1', 'l1', 'IBM819', 'CP819', 'csISOLatin1'],
    description: 'Western European (includes English, French, German, Spanish, Portuguese)',
    
    // 0x00-0x7F: Identical to ASCII
    ascii: Array.from({length: 128}, (_, i) => String.fromCharCode(i)),
    
    // 0xA0-0xFF: Extended Latin characters
    extended: {
        0xA0: '\u00A0', // Non-breaking space
        0xA1: '¡', 0xA2: '¢', 0xA3: '£', 0xA4: '¤', 0xA5: '¥', 0xA6: '¦', 0xA7: '§',
        0xA8: '¨', 0xA9: '©', 0xAA: 'ª', 0xAB: '«', 0xAC: '¬', 0xAD: '\u00AD', 0xAE: '®', 0xAF: '¯',
        0xB0: '°', 0xB1: '±', 0xB2: '²', 0xB3: '³', 0xB4: '´', 0xB5: 'µ', 0xB6: '¶', 0xB7: '·',
        0xB8: '¸', 0xB9: '¹', 0xBA: 'º', 0xBB: '»', 0xBC: '¼', 0xBD: '½', 0xBE: '¾', 0xBF: '¿',
        0xC0: 'À', 0xC1: 'Á', 0xC2: 'Â', 0xC3: 'Ã', 0xC4: 'Ä', 0xC5: 'Å', 0xC6: 'Æ', 0xC7: 'Ç',
        0xC8: 'È', 0xC9: 'É', 0xCA: 'Ê', 0xCB: 'Ë', 0xCC: 'Ì', 0xCD: 'Í', 0xCE: 'Î', 0xCF: 'Ï',
        0xD0: 'Ð', 0xD1: 'Ñ', 0xD2: 'Ò', 0xD3: 'Ó', 0xD4: 'Ô', 0xD5: 'Õ', 0xD6: 'Ö', 0xD7: '×',
        0xD8: 'Ø', 0xD9: 'Ù', 0xDA: 'Ú', 0xDB: 'Û', 0xDC: 'Ü', 0xDD: 'Ý', 0xDE: 'Þ', 0xDF: 'ß',
        0xE0: 'à', 0xE1: 'á', 0xE2: 'â', 0xE3: 'ã', 0xE4: 'ä', 0xE5: 'å', 0xE6: 'æ', 0xE7: 'ç',
        0xE8: 'è', 0xE9: 'é', 0xEA: 'ê', 0xEB: 'ë', 0xEC: 'ì', 0xED: 'í', 0xEE: 'î', 0xEF: 'ï',
        0xF0: 'ð', 0xF1: 'ñ', 0xF2: 'ò', 0xF3: 'ó', 0xF4: 'ô', 0xF5: 'õ', 0xF6: 'ö', 0xF7: '÷',
        0xF8: 'ø', 0xF9: 'ù', 0xFA: 'ú', 0xFB: 'û', 0xFC: 'ü', 0xFD: 'ý', 0xFE: 'þ', 0xFF: 'ÿ'
    }
};

/**
 * ISO-8859-2 (Latin-2) Central European
 */
const ISO_8859_2 = {
    name: 'ISO-8859-2',
    aliases: ['Latin-2', 'latin2', 'l2', 'csISOLatin2'],
    description: 'Central European (includes Polish, Czech, Slovak, Hungarian, Slovenian)',
    
    extended: {
        0xA0: '\u00A0', 0xA1: 'Ą', 0xA2: '˘', 0xA3: 'Ł', 0xA4: '¤', 0xA5: 'Ľ', 0xA6: 'Ś', 0xA7: '§',
        0xA8: '¨', 0xA9: 'Š', 0xAA: 'Ş', 0xAB: 'Ť', 0xAC: 'Ź', 0xAD: '\u00AD', 0xAE: 'Ž', 0xAF: 'Ż',
        0xB0: '°', 0xB1: 'ą', 0xB2: '˛', 0xB3: 'ł', 0xB4: '´', 0xB5: 'ľ', 0xB6: 'ś', 0xB7: 'ˇ',
        0xB8: '¸', 0xB9: 'š', 0xBA: 'ş', 0xBB: 'ť', 0xBC: 'ź', 0xBD: '˝', 0xBE: 'ž', 0xBF: 'ż',
        0xC0: 'Ŕ', 0xC1: 'Á', 0xC2: 'Â', 0xC3: 'Ă', 0xC4: 'Ä', 0xC5: 'Ĺ', 0xC6: 'Ć', 0xC7: 'Ç',
        0xC8: 'Č', 0xC9: 'É', 0xCA: 'Ę', 0xCB: 'Ë', 0xCC: 'Ě', 0xCD: 'Í', 0xCE: 'Î', 0xCF: 'Ď',
        0xD0: 'Đ', 0xD1: 'Ń', 0xD2: 'Ň', 0xD3: 'Ó', 0xD4: 'Ô', 0xD5: 'Ő', 0xD6: 'Ö', 0xD7: '×',
        0xD8: 'Ř', 0xD9: 'Ů', 0xDA: 'Ú', 0xDB: 'Ű', 0xDC: 'Ü', 0xDD: 'Ý', 0xDE: 'Ţ', 0xDF: 'ß',
        0xE0: 'ŕ', 0xE1: 'á', 0xE2: 'â', 0xE3: 'ă', 0xE4: 'ä', 0xE5: 'ĺ', 0xE6: 'ć', 0xE7: 'ç',
        0xE8: 'č', 0xE9: 'é', 0xEA: 'ę', 0xEB: 'ë', 0xEC: 'ě', 0xED: 'í', 0xEE: 'î', 0xEF: 'ď',
        0xF0: 'đ', 0xF1: 'ń', 0xF2: 'ň', 0xF3: 'ó', 0xF4: 'ô', 0xF5: 'ő', 0xF6: 'ö', 0xF7: '÷',
        0xF8: 'ř', 0xF9: 'ů', 0xFA: 'ú', 0xFB: 'ű', 0xFC: 'ü', 0xFD: 'ý', 0xFE: 'ţ', 0xFF: '˙'
    }
};

/**
 * ISO-8859-15 (Latin-9) - Revision of Latin-1 with Euro sign
 */
const ISO_8859_15 = {
    name: 'ISO-8859-15',
    aliases: ['Latin-9', 'latin9', 'l9', 'csISOLatin9'],
    description: 'Western European with Euro sign (€) - Updated version of ISO-8859-1',
    
    extended: {
        // Most same as ISO-8859-1, but with these replacements:
        0xA4: '€', // Euro sign (was ¤ in Latin-1)
        0xA6: 'Š', // (was ¦ in Latin-1)
        0xA8: 'š', // (was ¨ in Latin-1)
        0xB4: 'Ž', // (was ´ in Latin-1)
        0xB8: 'ž', // (was ¸ in Latin-1)
        0xBC: 'Œ', // (was ¼ in Latin-1)
        0xBD: 'œ', // (was ½ in Latin-1)
        0xBE: 'Ÿ', // (was ¾ in Latin-1)
        
        // Rest same as ISO-8859-1
        0xA0: '\u00A0', 0xA1: '¡', 0xA2: '¢', 0xA3: '£', 0xA5: '¥', 0xA7: '§',
        0xA9: '©', 0xAA: 'ª', 0xAB: '«', 0xAC: '¬', 0xAD: '\u00AD', 0xAE: '®', 0xAF: '¯',
        0xB0: '°', 0xB1: '±', 0xB2: '²', 0xB3: '³', 0xB5: 'µ', 0xB6: '¶', 0xB7: '·',
        0xB9: '¹', 0xBA: 'º', 0xBB: '»', 0xBF: '¿',
        0xC0: 'À', 0xC1: 'Á', 0xC2: 'Â', 0xC3: 'Ã', 0xC4: 'Ä', 0xC5: 'Å', 0xC6: 'Æ', 0xC7: 'Ç',
        0xC8: 'È', 0xC9: 'É', 0xCA: 'Ê', 0xCB: 'Ë', 0xCC: 'Ì', 0xCD: 'Í', 0xCE: 'Î', 0xCF: 'Ï',
        0xD0: 'Ð', 0xD1: 'Ñ', 0xD2: 'Ò', 0xD3: 'Ó', 0xD4: 'Ô', 0xD5: 'Õ', 0xD6: 'Ö', 0xD7: '×',
        0xD8: 'Ø', 0xD9: 'Ù', 0xDA: 'Ú', 0xDB: 'Û', 0xDC: 'Ü', 0xDD: 'Ý', 0xDE: 'Þ', 0xDF: 'ß',
        0xE0: 'à', 0xE1: 'á', 0xE2: 'â', 0xE3: 'ã', 0xE4: 'ä', 0xE5: 'å', 0xE6: 'æ', 0xE7: 'ç',
        0xE8: 'è', 0xE9: 'é', 0xEA: 'ê', 0xEB: 'ë', 0xEC: 'ì', 0xED: 'í', 0xEE: 'î', 0xEF: 'ï',
        0xF0: 'ð', 0xF1: 'ñ', 0xF2: 'ò', 0xF3: 'ó', 0xF4: 'ô', 0xF5: 'õ', 0xF6: 'ö', 0xF7: '÷',
        0xF8: 'ø', 0xF9: 'ù', 0xFA: 'ú', 0xFB: 'û', 0xFC: 'ü', 0xFD: 'ý', 0xFE: 'þ', 0xFF: 'ÿ'
    }
};

/**
 * WINDOWS-1252 (CP1252) - Windows Latin-1
 * Often used instead of ISO-8859-1 in web browsers
 */
const WINDOWS_1252 = {
    name: 'windows-1252',
    aliases: ['CP1252', 'Windows-1252'],
    description: 'Windows Western European - Uses 0x80-0x9F for printable characters',
    
    // 0x80-0x9F: Printable characters (differs from ISO-8859-1)
    c1_printable: {
        0x80: '€', 0x82: '‚', 0x83: 'ƒ', 0x84: '„', 0x85: '…', 0x86: '†', 0x87: '‡',
        0x88: 'ˆ', 0x89: '‰', 0x8A: 'Š', 0x8B: '‹', 0x8C: 'Œ', 0x8E: 'Ž',
        0x91: ''', 0x92: ''', 0x93: '"', 0x94: '"', 0x95: '•', 0x96: '–', 0x97: '—',
        0x98: '˜', 0x99: '™', 0x9A: 'š', 0x9B: '›', 0x9C: 'œ', 0x9E: 'ž', 0x9F: 'Ÿ'
    },
    
    // 0xA0-0xFF: Same as ISO-8859-1
    extended: ISO_8859_1.extended
};

/**
 * HELPER FUNCTIONS FOR AI ANALYSIS
 */
const LatinCharsets = {
    /**
     * Get character by hex code from specific charset
     */
    getChar(charset, hexCode) {
        if (hexCode < 0x80) {
            return String.fromCharCode(hexCode);
        }
        
        const charsetData = this.getCharset(charset);
        if (!charsetData) return null;
        
        if (charsetData.c1_printable && hexCode >= 0x80 && hexCode <= 0x9F) {
            return charsetData.c1_printable[hexCode];
        }
        
        return charsetData.extended[hexCode] || null;
    },
    
    /**
     * Get full charset data
     */
    getCharset(name) {
        const charsets = {
            'ISO-8859-1': ISO_8859_1,
            'ISO-8859-2': ISO_8859_2,
            'ISO-8859-15': ISO_8859_15,
            'windows-1252': WINDOWS_1252
        };
        return charsets[name] || charsets['ISO-8859-1'];
    },
    
    /**
     * Get all characters as array for a charset
     */
    getAllChars(charset) {
        const chars = [];
        for (let i = 0; i < 256; i++) {
            const char = this.getChar(charset, i);
            if (char) chars.push(char);
        }
        return chars;
    },
    
    /**
     * Analyze hex string using Latin charsets for phonetic matching
     */
    analyzeHex(hexString, charset = 'ISO-8859-1') {
        const bytes = hexString.match(/.{1,2}/g) || [];
        const chars = bytes.map(byte => {
            const code = parseInt(byte, 16);
            return this.getChar(charset, code);
        });
        return chars.join('');
    }
};

/**
 * AI TRAINING INSTRUCTIONS
 */
const AI_LATIN_CHARSET_TRAINING = {
    usage: 'AI should use these ACTUAL character mappings for phonetic analysis',
    
    criticalNotes: [
        '0x00-0x7F: Always identical to ASCII across all Latin charsets',
        '0x80-0x9F: Control codes in ISO-8859-*, printable in Windows-1252',
        '0xA0-0xFF: Extended Latin characters (language-specific)',
        'ISO-8859-1 = Western European (most common)',
        'ISO-8859-15 = ISO-8859-1 + Euro sign (€)',
        'windows-1252 = Most common in web browsers'
    ],
    
    forPhoneticAnalysis: [
        'Use Latin charset mappings for character set gap-filling',
        'Match hex codes to actual characters for pattern recognition',
        'Apply charset-specific characters when phonetic analysis needs manual additions',
        'Use 0xA0-0xFF range for extended character phonetic matching',
        'Remember: Bitcoin hashes use lowercase a-f (0x61-0x66 in ASCII)'
    ],
    
    studyFrequency: 'WEEKLY - Review with ai-bitcoin-operations-phonetic.js'
};

module.exports = {
    ISO_8859_1,
    ISO_8859_2,
    ISO_8859_15,
    WINDOWS_1252,
    LatinCharsets,
    AI_LATIN_CHARSET_TRAINING
};
