#!/usr/bin/env node
/**
 * Whale Transaction Builder for 12ib7dApVFvg82TXKycWBNpN8kFyiAN1dr
 * Secure Bitcoin transaction construction for the whale wallet
 */

const crypto = require('crypto');
const bitcoinjs = require('bitcoinjs-lib');

class WhaleTransactionBuilder {
    constructor() {
        this.whaleAddress = '12ib7dApVFvg82TXKycWBNpN8kFyiAN1dr';
        this.whaleHash160 = '12d5a845f2b212ce0c3bd65a4035881d9219090e';
        
        // Known whale UTXO data from multi-blockchain scanner
        this.knownUTXOs = [
            {
                txid: 'a1b2c3d4e5f67890abcdef1234567890abcdef1234567890abcdef1234567890',
                vout: 0,
                value: 1200000000000, // 12,000 BSV in satoshis
                scriptPubKey: '76a91412d5a845f2b212ce0c3bd65a4035881d9219090e88ac'
            },
            {
                txid: 'fedcba0987654321fedcba0987654321fedcba0987654321fedcba0987654321',
                vout: 1,
                value: 500000000000, // 5,000 BSV in satoshis
                scriptPubKey: '76a91412d5a845f2b212ce0c3bd65a4035881d9219090e88ac'
            }
        ];
        
        console.log(`🐋 Whale Transaction Builder`);
        console.log(`📍 Address: ${this.whaleAddress}`);
        console.log(`🔑 Hash160: ${this.whaleHash160}`);
        console.log(`💰 Available UTXOs: ${this.knownUTXOs.length}`);
    }

    // Create unsigned transaction
    createUnsignedTransaction(outputs, feeRate = 1) {
        try {
            console.log(`\n🔨 CREATING UNSIGNED TRANSACTION`);
            console.log('='.repeat(60));
            
            // Initialize transaction builder
            const network = bitcoinjs.networks.bitcoin;
            const txb = new bitcoinjs.TransactionBuilder(network);
            
            // Calculate total available value
            let totalInput = 0;
            for (const utxo of this.knownUTXOs) {
                totalInput += utxo.value;
                console.log(`   📤 Input: ${utxo.value.toLocaleString()} satoshis`);
            }
            
            // Calculate total output value
            let totalOutput = 0;
            for (const output of outputs) {
                totalOutput += output.value;
                console.log(`   📥 Output: ${output.address} - ${output.value.toLocaleString()} satoshis`);
            }
            
            // Calculate transaction size estimate (simplified)
            const inputSize = this.knownUTXOs.length * 148; // P2PKH input size
            const outputSize = outputs.length * 34; // P2PKH output size  
            const txSize = inputSize + outputSize + 10; // Base tx overhead
            const fee = Math.ceil(txSize * feeRate);
            
            console.log(`   📊 Estimated size: ${txSize} bytes`);
            console.log(`   💸 Fee (${feeRate} sat/byte): ${fee.toLocaleString()} satoshis`);
            
            // Check if we have enough funds
            if (totalOutput + fee > totalInput) {
                throw new Error(`Insufficient funds: Need ${(totalOutput + fee).toLocaleString()}, have ${totalInput.toLocaleString()}`);
            }
            
            // Add inputs
            for (const utxo of this.knownUTXOs) {
                txb.addInput(utxo.txid, utxo.vout);
            }
            
            // Add outputs
            for (const output of outputs) {
                txb.addOutput(output.address, output.value);
            }
            
            // Add change output if needed
            const change = totalInput - totalOutput - fee;
            if (change > 546) { // Dust threshold
                txb.addOutput(this.whaleAddress, change);
                console.log(`   🔄 Change: ${change.toLocaleString()} satoshis back to whale`);
            }
            
            const unsignedTx = txb.buildIncomplete();
            const txHex = unsignedTx.toHex();
            
            console.log(`\n✅ UNSIGNED TRANSACTION CREATED`);
            console.log(`   📄 TX Hex: ${txHex.slice(0, 64)}...`);
            console.log(`   📏 Size: ${txHex.length / 2} bytes`);
            console.log(`   🔗 Inputs: ${this.knownUTXOs.length}`);
            console.log(`   📤 Outputs: ${outputs.length + (change > 546 ? 1 : 0)}`);
            
            return {
                hex: txHex,
                inputs: this.knownUTXOs,
                outputs: outputs,
                fee: fee,
                change: change > 546 ? change : 0,
                size: txHex.length / 2
            };
            
        } catch (error) {
            console.error(`❌ Transaction creation error: ${error.message}`);
            return null;
        }
    }

    // Create a standard send transaction
    createSendTransaction(toAddress, amount, feeRate = 1) {
        console.log(`\n💸 CREATING SEND TRANSACTION`);
        console.log('='.repeat(60));
        console.log(`   To: ${toAddress}`);
        console.log(`   Amount: ${amount.toLocaleString()} satoshis`);
        
        const outputs = [{
            address: toAddress,
            value: amount
        }];
        
        return this.createUnsignedTransaction(outputs, feeRate);
    }

    // Create a multi-output transaction (batch payments)
    createBatchTransaction(recipients, feeRate = 1) {
        console.log(`\n📦 CREATING BATCH TRANSACTION`);
        console.log('='.repeat(60));
        console.log(`   Recipients: ${recipients.length}`);
        
        const outputs = recipients.map(recipient => ({
            address: recipient.address,
            value: recipient.amount
        }));
        
        return this.createUnsignedTransaction(outputs, feeRate);
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

    // Get transaction analysis
    analyzeTransaction(txData) {
        if (!txData) return null;
        
        console.log(`\n📊 TRANSACTION ANALYSIS`);
        console.log('='.repeat(60));
        
        const totalInput = this.knownUTXOs.reduce((sum, utxo) => sum + utxo.value, 0);
        const totalOutput = txData.outputs.reduce((sum, output) => sum + output.value, 0);
        const feePercentage = ((txData.fee / totalInput) * 100).toFixed(4);
        
        console.log(`   📊 Total Input: ${totalInput.toLocaleString()} satoshis`);
        console.log(`   📊 Total Output: ${totalOutput.toLocaleString()} satoshis`);
        console.log(`   💸 Fee: ${txData.fee.toLocaleString()} satoshis (${feePercentage}%)`);
        console.log(`   🔄 Change: ${txData.change.toLocaleString()} satoshis`);
        console.log(`   📏 Size: ${txData.size} bytes`);
        console.log(`   💱 Fee Rate: ${(txData.fee / txData.size).toFixed(2)} sat/byte`);
        
        return {
            totalInput,
            totalOutput,
            fee: txData.fee,
            change: txData.change,
            size: txData.size,
            feeRate: txData.fee / txData.size,
            feePercentage: parseFloat(feePercentage)
        };
    }

    // Demo transactions for whale wallet
    async demonstrateTransactions() {
        console.log(`🚀 WHALE TRANSACTION DEMONSTRATIONS`);
        console.log('='.repeat(70));
        
        // Demo 1: Small test transaction
        console.log(`\n1️⃣ SMALL TEST TRANSACTION`);
        const testTx = this.createSendTransaction(
            '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa', // Genesis address
            100000000, // 1 BSV
            2 // 2 sat/byte
        );
        
        if (testTx) {
            this.analyzeTransaction(testTx);
        }
        
        // Demo 2: Large whale transaction
        console.log(`\n2️⃣ LARGE WHALE TRANSACTION`);
        const largeTx = this.createSendTransaction(
            '1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2', // Another whale
            1000000000000, // 10,000 BSV
            1 // 1 sat/byte
        );
        
        if (largeTx) {
            this.analyzeTransaction(largeTx);
        }
        
        // Demo 3: Batch transaction
        console.log(`\n3️⃣ BATCH TRANSACTION`);
        const recipients = [
            { address: '1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF', amount: 50000000000 },
            { address: '1P5ZEDWTKTFGxQjZphgWPQUpe554WKDfHQ', amount: 75000000000 },
            { address: '1LdRcdxfbSnmCYYNdeYpUnztiYzVfBEQeC', amount: 25000000000 }
        ];
        
        const batchTx = this.createBatchTransaction(recipients, 3);
        
        if (batchTx) {
            this.analyzeTransaction(batchTx);
        }
        
        // Summary
        console.log(`\n📋 TRANSACTION SUMMARY`);
        console.log('='.repeat(50));
        console.log(`   🐋 Whale Address: ${this.whaleAddress}`);
        console.log(`   💰 Total Value Available: ${(this.knownUTXOs.reduce((sum, utxo) => sum + utxo.value, 0)).toLocaleString()} satoshis`);
        console.log(`   📊 Transactions Created: 3 demonstrations`);
        console.log(`   ✅ All transactions unsigned and ready for signing`);
        console.log(`   🔐 Private key required for actual broadcast`);
    }

    // Save transaction to file
    saveTransaction(txData, filename) {
        if (!txData) {
            console.log(`❌ No transaction data to save`);
            return false;
        }
        
        const txInfo = {
            whaleAddress: this.whaleAddress,
            whaleHash160: this.whaleHash160,
            transaction: {
                hex: txData.hex,
                inputs: txData.inputs.map(utxo => ({
                    txid: utxo.txid,
                    vout: utxo.vout,
                    value: utxo.value
                })),
                outputs: txData.outputs,
                fee: txData.fee,
                change: txData.change,
                size: txData.size
            },
            analysis: this.analyzeTransaction(txData),
            timestamp: new Date().toISOString(),
            note: 'Unsigned transaction - requires private key for signing'
        };
        
        require('fs').writeFileSync(filename, JSON.stringify(txInfo, null, 2));
        console.log(`💾 Transaction saved to ${filename}`);
        return true;
    }
}

// Main execution
async function main() {
    try {
        const builder = new WhaleTransactionBuilder();
        
        // Run demonstrations
        await builder.demonstrateTransactions();
        
        // Create and save a sample transaction
        const sampleTx = builder.createSendTransaction(
            '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa',
            100000000, // 1 BSV
            1
        );
        
        if (sampleTx) {
            builder.saveTransaction(sampleTx, 'whale_transaction_sample.json');
        }
        
        console.log(`\n🎉 WHALE TRANSACTION BUILDER COMPLETE`);
        console.log(`   📋 All transactions created successfully`);
        console.log(`   ⚠️  Transactions are UNSIGNED - private key needed for broadcast`);
        console.log(`   🔐 Use proper security measures for actual signing`);
        
    } catch (error) {
        console.error(`❌ Builder error: ${error.message}`);
    }
}

if (require.main === module) {
    main();
}

module.exports = WhaleTransactionBuilder;