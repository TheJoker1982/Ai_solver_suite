#!/usr/bin/env node
/**
 * Hash160 Inverse/Opposite Analyzer
 * Find inverse/opposite of whale hash160: 12d5a845f2b212ce0c3bd65a4035881d9219090e
 * Convert to Bitcoin addresses and analyze relationships
 */

const crypto = require('crypto');

class Hash160InverseAnalyzer {
    constructor() {
        this.whaleHash160 = '12d5a845f2b212ce0c3bd65a4035881d9219090e';
        this.whaleAddress = '12ib7dApVFvg82TXKycWBNpN8kFyiAN1dr';
        
        console.log(`🐋 Whale Hash160: ${this.whaleHash160}`);
        console.log(`🏠 Whale Address: ${this.whaleAddress}`);
        console.log(`🔄 Finding inverse/opposite operations`);
    }

    // Base58 operations
    base58Alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz';

    base58Encode(buffer) {
        let num = BigInt('0x' + buffer.toString('hex'));
        let encoded = '';
        
        while (num > 0) {
            const remainder = num % 58n;
            encoded = this.base58Alphabet[Number(remainder)] + encoded;
            num = num / 58n;
        }
        
        for (let i = 0; i < buffer.length && buffer[i] === 0; i++) {
            encoded = '1' + encoded;
        }
        
        return encoded;
    }

    // Double SHA256
    doubleSha256(data) {
        const hash1 = crypto.createHash('sha256').update(data).digest();
        return crypto.createHash('sha256').update(hash1).digest();
    }

    // Convert hash160 to Bitcoin address
    hash160ToAddress(hash160Hex) {
        try {
            const hash160Buffer = Buffer.from(hash160Hex, 'hex');
            const versionedHash = Buffer.concat([Buffer.from([0x00]), hash160Buffer]);
            const checksum = this.doubleSha256(versionedHash).slice(0, 4);
            const fullPayload = Buffer.concat([versionedHash, checksum]);
            return this.base58Encode(fullPayload);
        } catch (error) {
            return null;
        }
    }

    // Bitwise NOT (inverse)
    bitwiseNOT(hexString) {
        let result = '';
        for (let i = 0; i < hexString.length; i++) {
            const digit = parseInt(hexString[i], 16);
            const inverted = (15 - digit).toString(16); // XOR with 0xF
            result += inverted;
        }
        return result;
    }

    // Two's complement
    twosComplement(hexString) {
        try {
            // Convert to BigInt, invert bits, add 1
            const num = BigInt('0x' + hexString);
            const bitLength = hexString.length * 4;
            const mask = (BigInt(1) << BigInt(bitLength)) - BigInt(1);
            
            const inverted = (~num) & mask;
            const twosComp = (inverted + BigInt(1)) & mask;
            
            return twosComp.toString(16).padStart(hexString.length, '0');
        } catch (error) {
            return hexString;
        }
    }

    // Byte reversal
    reverseBytes(hexString) {
        let result = '';
        for (let i = hexString.length - 2; i >= 0; i -= 2) {
            result += hexString.slice(i, i + 2);
        }
        return result;
    }

    // Nibble reversal
    reverseNibbles(hexString) {
        let result = '';
        for (let i = 0; i < hexString.length; i += 2) {
            const byte = hexString.slice(i, i + 2);
            result += byte[1] + byte[0]; // Swap nibbles
        }
        return result;
    }

    // Mathematical inverse (modular)
    mathematicalInverse(hexString) {
        try {
            // Modular inverse using extended Euclidean algorithm (simplified)
            const num = BigInt('0x' + hexString);
            const modulus = BigInt('0x' + 'f'.repeat(40)); // Max 20-byte value
            
            // Simplified: just return (modulus - num) for demo
            const inverse = (modulus - num) % modulus;
            return inverse.toString(16).padStart(40, '0');
        } catch (error) {
            return hexString;
        }
    }

    // XOR with pattern
    xorWithPattern(hexString, pattern) {
        try {
            const num = BigInt('0x' + hexString);
            const patternNum = BigInt('0x' + pattern.repeat(Math.ceil(hexString.length / pattern.length)).slice(0, hexString.length));
            const result = num ^ patternNum;
            return result.toString(16).padStart(hexString.length, '0');
        } catch (error) {
            return hexString;
        }
    }

    // Comprehensive inverse analysis
    async comprehensiveInverseAnalysis() {
        console.log(`\n🔄 COMPREHENSIVE INVERSE ANALYSIS`);
        console.log('='.repeat(70));
        
        const inversions = [
            {
                name: 'Bitwise NOT (Inverse)',
                operation: this.bitwiseNOT(this.whaleHash160),
                description: 'Flip every bit (0→1, 1→0)'
            },
            {
                name: "Two's Complement",
                operation: this.twosComplement(this.whaleHash160),
                description: 'NOT + 1 (mathematical negative)'
            },
            {
                name: 'Byte Reversal',
                operation: this.reverseBytes(this.whaleHash160),
                description: 'Reverse byte order (endianness flip)'
            },
            {
                name: 'Nibble Reversal',
                operation: this.reverseNibbles(this.whaleHash160),
                description: 'Swap nibbles within each byte'
            },
            {
                name: 'Mathematical Inverse',
                operation: this.mathematicalInverse(this.whaleHash160),
                description: 'Modular inverse (max - value)'
            },
            {
                name: 'XOR with 0xAA pattern',
                operation: this.xorWithPattern(this.whaleHash160, 'aa'),
                description: 'XOR with alternating bits pattern'
            },
            {
                name: 'XOR with 0x55 pattern',
                operation: this.xorWithPattern(this.whaleHash160, '55'),
                description: 'XOR with inverse alternating pattern'
            },
            {
                name: 'XOR with 0xFF pattern',
                operation: this.xorWithPattern(this.whaleHash160, 'ff'),
                description: 'XOR with all ones (same as NOT)'
            }
        ];

        console.log(`\n📊 INVERSE OPERATIONS RESULTS`);
        console.log('='.repeat(70));
        
        for (const [index, inversion] of inversions.entries()) {
            console.log(`\n${index + 1}. ${inversion.name}`);
            console.log(`   Description: ${inversion.description}`);
            console.log(`   Hash160: ${inversion.operation}`);
            
            // Convert to Bitcoin address
            const address = this.hash160ToAddress(inversion.operation);
            console.log(`   Address: ${address}`);
            
            // Check if it matches any known patterns
            if (address) {
                if (address.startsWith('1')) {
                    console.log(`   Format: Legacy P2PKH ✅`);
                } else {
                    console.log(`   Format: Invalid/Non-standard ❌`);
                }
                
                // Check for interesting patterns
                if (address.includes('111') || address.includes('000')) {
                    console.log(`   🎯 Contains repeated digits!`);
                }
                
                if (address.length < 26 || address.length > 35) {
                    console.log(`   ⚠️  Unusual address length: ${address.length}`);
                }
            }
        }

        // Special analysis
        console.log(`\n🔍 SPECIAL INVERSE RELATIONSHIPS`);
        console.log('='.repeat(70));
        
        // Check if any inverse operation produces a known whale address
        const knownWhales = [
            '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa', // Genesis
            '1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF', // Famous
            '1P5ZEDWTKTFGxQjZphgWPQUpe554WKDfHQ', // Large
            '1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2'  // Satoshi
        ];
        
        for (const inversion of inversions) {
            const address = this.hash160ToAddress(inversion.operation);
            if (address && knownWhales.includes(address)) {
                console.log(`   🐋 WHALE FOUND! ${inversion.name} → ${address}`);
            }
        }

        // Return the most interesting inverse
        const bitwiseInverse = inversions[0].operation;
        const bitwiseAddress = this.hash160ToAddress(bitwiseInverse);
        
        console.log(`\n🎯 PRIMARY INVERSE RESULT`);
        console.log('='.repeat(50));
        console.log(`   Original: ${this.whaleHash160} → ${this.whaleAddress}`);
        console.log(`   Inverse:  ${bitwiseInverse} → ${bitwiseAddress}`);
        console.log(`   Method: Bitwise NOT (complete bit flip)`);
        
        return {
            original: { hash160: this.whaleHash160, address: this.whaleAddress },
            inverse: { hash160: bitwiseInverse, address: bitwiseAddress },
            allInversions: inversions
        };
    }

    // Analyze inverse relationships
    async analyzeInverseRelationships() {
        console.log(`\n🔗 INVERSE RELATIONSHIP ANALYSIS`);
        console.log('='.repeat(70));
        
        const bitwiseInverse = this.bitwiseNOT(this.whaleHash160);
        const inverseAddress = this.hash160ToAddress(bitwiseInverse);
        
        console.log(`   Original Hash160: ${this.whaleHash160}`);
        console.log(`   Bitwise Inverse:  ${bitwiseInverse}`);
        console.log(`   Original Address: ${this.whaleAddress}`);
        console.log(`   Inverse Address:  ${inverseAddress}`);
        
        // Check if inverse has special properties
        if (inverseAddress) {
            // Count repeated characters
            const charCounts = {};
            for (const char of inverseAddress) {
                charCounts[char] = (charCounts[char] || 0) + 1;
            }
            
            const repeatedChars = Object.entries(charCounts)
                .filter(([char, count]) => count > 2)
                .map(([char, count]) => `${char}×${count}`)
                .join(', ');
            
            if (repeatedChars) {
                console.log(`   🎯 Repeated chars: ${repeatedChars}`);
            }
            
            // Check for patterns
            if (inverseAddress.includes('1111') || inverseAddress.includes('aaaa')) {
                console.log(`   🔥 Contains 4+ repeated characters!`);
            }
            
            // Check if it's a vanity address
            const vanityPatterns = ['111', '888', 'abc', '123', 'sat', 'btc'];
            for (const pattern of vanityPatterns) {
                if (inverseAddress.toLowerCase().includes(pattern)) {
                    console.log(`   ✨ Vanity pattern '${pattern}' found!`);
                }
            }
        }
        
        return { bitwiseInverse, inverseAddress };
    }
}

// Main execution
async function main() {
    try {
        const analyzer = new Hash160InverseAnalyzer();
        
        // Run comprehensive analysis
        const result = await analyzer.comprehensiveInverseAnalysis();
        
        // Analyze relationships
        await analyzer.analyzeInverseRelationships();
        
        console.log(`\n✅ INVERSE ANALYSIS COMPLETE`);
        console.log('='.repeat(50));
        console.log(`   🐋 Original whale: ${result.original.address}`);
        console.log(`   🔄 Primary inverse: ${result.inverse.address}`);
        console.log(`   📊 Total inversions: ${result.allInversions.length}`);
        
        // Save results
        const saveData = {
            whale: result.original,
            primaryInverse: result.inverse,
            allInversions: result.allInversions.map(inv => ({
                name: inv.name,
                hash160: inv.operation,
                address: analyzer.hash160ToAddress(inv.operation)
            })),
            timestamp: new Date().toISOString()
        };
        
        require('fs').writeFileSync('hash160_inverse_analysis.json', JSON.stringify(saveData, null, 2));
        console.log(`   💾 Results saved to hash160_inverse_analysis.json`);
        
    } catch (error) {
        console.error(`❌ Inverse analysis error: ${error.message}`);
    }
}

if (require.main === module) {
    main();
}

module.exports = Hash160InverseAnalyzer;