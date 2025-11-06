#!/usr/bin/env node
/**
 * Whale to Personal Wallet Transaction Builder
 * Sends funds FROM whale address TO user's personal wallet
 */

const crypto = require('crypto');
const bitcoinjs = require('bitcoinjs-lib');

class WhaleToPersonalTransactionBuilder {
    constructor() {
        this.whaleAddress = '12ib7dApVFvg82TXKycWBNpN8kFyiAN1dr';
        this.whaleHash160 = '12d5a845f2b212ce0c3bd65a4035881d9219090e';
        
        console.log(`🐋➡️💼 WHALE TO PERSONAL WALLET TRANSACTION BUILDER`);
        console.log(`📍 FROM: ${this.whaleAddress}`);
        console.log(`🔑 Hash160: ${this.whaleHash160}`);
    }

    // Create transaction from whale to user's personal wallet
    createWhaleToPersonalTransaction(personalAddress, amount, feeRate = 1, sweepAll = false) {
        try {
            console.log(`\n💸 CREATING WHALE → PERSONAL TRANSACTION`);
            console.log('='.repeat(60));
            console.log(`   FROM (Whale): ${this.whaleAddress}`);
            console.log(`   TO (Personal): ${personalAddress}`);
            
            // Validate personal address
            if (!this.validateAddress(personalAddress)) {
                throw new Error(`Invalid personal wallet address: ${personalAddress}`);
            }
            
            // Mock whale UTXOs (in real implementation, fetch from blockchain)
            const whaleUTXOs = [
                {
                    txid: 'a1b2c3d4e5f67890abcdef1234567890abcdef1234567890abcdef1234567890',
                    vout: 0,
                    value: 1200000000000, // 12,000 BSV
                    scriptPubKey: '76a91412d5a845f2b212ce0c3bd65a4035881d9219090e88ac'
                },
                {
                    txid: 'fedcba0987654321fedcba0987654321fedcba0987654321fedcba0987654321',
                    vout: 1,
                    value: 500000000000, // 5,000 BSV  
                    scriptPubKey: '76a91412d5a845f2b212ce0c3bd65a4035881d9219090e88ac'
                }
            ];
            
            const totalAvailable = whaleUTXOs.reduce((sum, utxo) => sum + utxo.value, 0);
            console.log(`   💰 Total Available: ${totalAvailable.toLocaleString()} satoshis (${(totalAvailable / 100000000).toLocaleString()} BSV)`);
            
            // Calculate transaction details
            const inputSize = whaleUTXOs.length * 148; // P2PKH input size
            const outputSize = sweepAll ? 34 : 68; // 1 output if sweep, 2 if amount + change
            const txSize = inputSize + outputSize + 10;
            const fee = Math.ceil(txSize * feeRate);
            
            let sendAmount, changeAmount;
            
            if (sweepAll) {
                sendAmount = totalAvailable - fee;
                changeAmount = 0;
                console.log(`   🧹 SWEEP ALL: Sending entire balance minus fee`);
                console.log(`   📤 Send Amount: ${sendAmount.toLocaleString()} satoshis`);
                console.log(`   💸 Fee: ${fee.toLocaleString()} satoshis`);
                console.log(`   🔄 Change: 0 (all funds to personal wallet)`);
            } else {
                if (amount + fee > totalAvailable) {
                    throw new Error(`Insufficient funds: Need ${(amount + fee).toLocaleString()}, have ${totalAvailable.toLocaleString()}`);
                }
                sendAmount = amount;
                changeAmount = totalAvailable - amount - fee;
                
                console.log(`   📤 Send Amount: ${sendAmount.toLocaleString()} satoshis`);
                console.log(`   💸 Fee: ${fee.toLocaleString()} satoshis`);
                
                if (changeAmount > 546) { // Above dust threshold
                    console.log(`   🔄 Change: ${changeAmount.toLocaleString()} satoshis (TO YOUR PERSONAL WALLET)`);
                } else {
                    console.log(`   🔄 Change: ${changeAmount.toLocaleString()} satoshis (below dust, added to fee)`);
                    sendAmount += changeAmount;
                    changeAmount = 0;
                }
            }
            
            // Build transaction using PSBT (modern approach)
            const psbt = new bitcoinjs.Psbt({ network: bitcoinjs.networks.bitcoin });
            
            // Add inputs from whale wallet
            for (const utxo of whaleUTXOs) {
                psbt.addInput({
                    hash: utxo.txid,
                    index: utxo.vout,
                    nonWitnessUtxo: Buffer.from('placeholder_raw_tx_hex', 'hex'), // In real implementation, get full raw tx
                });
            }
            
            // Add output to personal wallet
            psbt.addOutput({
                address: personalAddress,
                value: sendAmount,
            });
            
            // Add change output to personal wallet (NOT back to whale)
            if (changeAmount > 546) {
                psbt.addOutput({
                    address: personalAddress, // IMPORTANT: Change goes to personal wallet too
                    value: changeAmount,
                });
                console.log(`   ✅ Change also going to personal wallet (NOT back to whale)`);
            }
            
            const unsignedPsbt = psbt.toBase64();
            
            console.log(`\n✅ UNSIGNED PSBT CREATED`);
            console.log(`   📄 PSBT: ${unsignedPsbt.slice(0, 64)}...`);
            console.log(`   📏 Estimated Size: ${txSize} bytes`);
            console.log(`   🔗 Inputs: ${whaleUTXOs.length} (from whale)`);
            console.log(`   📤 Outputs: ${changeAmount > 546 ? 2 : 1} (all to personal wallet)`);
            console.log(`   💱 Fee Rate: ${feeRate} sat/byte`);
            
            return {
                psbt: unsignedPsbt,
                fromAddress: this.whaleAddress,
                toAddress: personalAddress,
                sendAmount: sendAmount,
                changeAmount: changeAmount,
                fee: fee,
                totalSent: sendAmount + changeAmount,
                feeRate: feeRate,
                sweepAll: sweepAll,
                inputs: whaleUTXOs,
                size: txSize
            };
            
        } catch (error) {
            console.error(`❌ Transaction creation error: ${error.message}`);
            return null;
        }
    }

    // Validate Bitcoin address
    validateAddress(address) {
        try {
            bitcoinjs.address.toOutputScript(address, bitcoinjs.networks.bitcoin);
            return true;
        } catch (error) {
            return false;
        }
    }

    // Interactive transaction builder
    promptForPersonalTransaction() {
        console.log(`\n🎯 WHALE TO PERSONAL WALLET TRANSACTION`);
        console.log('='.repeat(50));
        console.log(`Please provide the following information:`);
        console.log(`\n1. Your personal Bitcoin address (where funds will be sent)`);
        console.log(`2. Amount in satoshis (or 'sweep' for all funds)`);
        console.log(`3. Fee rate in sat/byte (default: 1)`);
        console.log(`\nExample usage:`);
        console.log(`  Personal Address: 1YourPersonalAddressHere...`);
        console.log(`  Amount: 100000000000 (1000 BSV) or 'sweep'`);
        console.log(`  Fee Rate: 2`);
        console.log(`\n⚠️  IMPORTANT: ALL FUNDS (including change) will go to YOUR personal address`);
        console.log(`   📍 NO funds will return to the whale address`);
        console.log(`   🔐 Transaction will be unsigned - you need the whale private key to sign`);
    }

    // Create sweep transaction (send ALL funds to personal wallet)
    createSweepTransaction(personalAddress, feeRate = 1) {
        console.log(`\n🧹 CREATING SWEEP TRANSACTION`);
        console.log('='.repeat(50));
        console.log(`   🐋 FROM: ${this.whaleAddress} (ALL FUNDS)`);
        console.log(`   💼 TO: ${personalAddress} (YOUR WALLET)`);
        
        return this.createWhaleToPersonalTransaction(personalAddress, 0, feeRate, true);
    }

    // Save transaction details
    saveTransaction(txData, filename) {
        if (!txData) {
            console.log(`❌ No transaction data to save`);
            return false;
        }
        
        const txInfo = {
            transaction_type: "whale_to_personal",
            whale_address: this.whaleAddress,
            personal_address: txData.toAddress,
            amounts: {
                send_amount: txData.sendAmount,
                change_amount: txData.changeAmount,
                total_to_personal: txData.totalSent,
                fee: txData.fee
            },
            transaction: {
                psbt: txData.psbt,
                sweep_all: txData.sweepAll,
                fee_rate: txData.feeRate,
                size: txData.size
            },
            important_notes: [
                "ALL funds go to personal wallet - NO funds return to whale",
                "Transaction is UNSIGNED - requires whale private key to sign",
                "Change output also goes to personal wallet address",
                "Use proper security measures when signing with whale private key"
            ],
            timestamp: new Date().toISOString()
        };
        
        require('fs').writeFileSync(filename, JSON.stringify(txInfo, null, 2));
        console.log(`💾 Transaction saved to ${filename}`);
        return true;
    }
}

// Main execution
function main() {
    const builder = new WhaleToPersonalTransactionBuilder();
    
    // Show prompt for user input
    builder.promptForPersonalTransaction();
    
    console.log(`\n📋 READY TO CREATE WHALE → PERSONAL TRANSACTION`);
    console.log(`   🔧 Provide your personal address to create the transaction`);
    console.log(`   💰 Specify amount or use 'sweep' for all funds`);
    console.log(`   🎯 ALL outputs will go to YOUR personal wallet`);
}

if (require.main === module) {
    main();
}

module.exports = WhaleToPersonalTransactionBuilder;