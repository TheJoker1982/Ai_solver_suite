/**
 * UNIFIED API INTEGRATIONS
 * 
 * Integrates ALL blockchain and AI APIs:
 * - Google Gemini (AI)
 * - Google Developers (OAuth, Drive, etc.)
 * - Etherscan (Ethereum blockchain data)
 * - Tokenomics (Token economics data)
 * - BlockCypher (Bitcoin/Litecoin/Dogecoin data)
 * - BlockScan (Multi-chain block explorer)
 * - Infura (Ethereum node provider)
 */

const axios = require('axios');

class APIIntegrations {
    constructor() {
        this.apis = {
            gemini: {
                name: 'Google Gemini',
                baseUrl: 'https://generativelanguage.googleapis.com/v1',
                apiKey: process.env.GOOGLE_GEMINI_API_KEY || process.env.GEMINI_API_KEY,
                status: 'unknown'
            },
            googleDevelopers: {
                name: 'Google Developers',
                baseUrl: 'https://www.googleapis.com',
                apiKey: process.env.GOOGLE_API_KEY || process.env.GOOGLE_DEVELOPERS_API_KEY,
                status: 'unknown'
            },
            etherscan: {
                name: 'Etherscan',
                baseUrl: 'https://api.etherscan.io/api',
                apiKey: process.env.ETHERSCAN_API_KEY,
                status: 'unknown'
            },
            tokenomics: {
                name: 'Tokenomics',
                baseUrl: 'https://api.tokenomics.io/v1',
                apiKey: process.env.TOKENOMICS_API_KEY,
                status: 'unknown'
            },
            blockcypher: {
                name: 'BlockCypher',
                baseUrl: 'https://api.blockcypher.com/v1',
                apiKey: process.env.BLOCKCYPHER_API_KEY,
                status: 'unknown'
            },
            blockscan: {
                name: 'BlockScan',
                baseUrl: 'https://api.blockscan.com',
                apiKey: process.env.BLOCKSCAN_API_KEY,
                status: 'unknown'
            },
            infura: {
                name: 'Infura',
                baseUrl: 'https://mainnet.infura.io/v3',
                apiKey: process.env.INFURA_API_KEY || process.env.INFURA_PROJECT_ID,
                status: 'unknown'
            }
        };

        this.cache = new Map();
        this.cacheTimeout = 60000; // 60 seconds
    }

    /**
     * Test all API connections
     */
    async testAllConnections() {
        console.log('🔌 Testing API Connections...');
        console.log('═══════════════════════════════════════');

        const results = {};

        for (const [key, api] of Object.entries(this.apis)) {
            try {
                const status = await this.testConnection(key);
                api.status = status ? 'connected' : 'failed';
                results[key] = api.status;
                
                const icon = status ? '✅' : '❌';
                const keyStatus = api.apiKey ? '🔑' : '⚠️  (no key)';
                console.log(`${icon} ${api.name}: ${api.status} ${keyStatus}`);
            } catch (error) {
                api.status = 'error';
                results[key] = 'error';
                console.log(`❌ ${api.name}: error - ${error.message}`);
            }
        }

        console.log('═══════════════════════════════════════');
        return results;
    }

    /**
     * Test individual API connection
     */
    async testConnection(apiKey) {
        const api = this.apis[apiKey];
        if (!api || !api.apiKey) return false;

        try {
            switch (apiKey) {
                case 'gemini':
                    return await this.testGemini();
                case 'etherscan':
                    return await this.testEtherscan();
                case 'blockcypher':
                    return await this.testBlockCypher();
                case 'infura':
                    return await this.testInfura();
                default:
                    return false;
            }
        } catch (error) {
            console.error(`Error testing ${api.name}:`, error.message);
            return false;
        }
    }

    /**
     * Google Gemini - AI Chat
     */
    async testGemini() {
        const api = this.apis.gemini;
        if (!api.apiKey) return false;

        try {
            const response = await axios.post(
                `${api.baseUrl}/models/gemini-pro:generateContent?key=${api.apiKey}`,
                {
                    contents: [{
                        parts: [{ text: 'Hello' }]
                    }]
                },
                { timeout: 5000 }
            );
            return response.status === 200;
        } catch (error) {
            return false;
        }
    }

    /**
     * Gemini AI - Generate content
     */
    async geminiGenerate(prompt, model = 'gemini-pro') {
        const api = this.apis.gemini;
        if (!api.apiKey) {
            throw new Error('Gemini API key not configured');
        }

        try {
            const response = await axios.post(
                `${api.baseUrl}/models/${model}:generateContent?key=${api.apiKey}`,
                {
                    contents: [{
                        parts: [{ text: prompt }]
                    }]
                }
            );

            const text = response.data.candidates[0].content.parts[0].text;
            return { success: true, text };
        } catch (error) {
            return {
                success: false,
                error: error.message
            };
        }
    }

    /**
     * Etherscan - Get ETH balance
     */
    async testEtherscan() {
        const api = this.apis.etherscan;
        if (!api.apiKey) return false;

        try {
            const response = await axios.get(api.baseUrl, {
                params: {
                    module: 'account',
                    action: 'balance',
                    address: '0x0000000000000000000000000000000000000000',
                    tag: 'latest',
                    apikey: api.apiKey
                },
                timeout: 5000
            });
            return response.data.status === '1';
        } catch (error) {
            return false;
        }
    }

    /**
     * Etherscan - Get address balance
     */
    async etherscanGetBalance(address) {
        const api = this.apis.etherscan;
        if (!api.apiKey) {
            throw new Error('Etherscan API key not configured');
        }

        const cacheKey = `etherscan_balance_${address}`;
        if (this.cache.has(cacheKey)) {
            const cached = this.cache.get(cacheKey);
            if (Date.now() - cached.timestamp < this.cacheTimeout) {
                return cached.data;
            }
        }

        try {
            const response = await axios.get(api.baseUrl, {
                params: {
                    module: 'account',
                    action: 'balance',
                    address,
                    tag: 'latest',
                    apikey: api.apiKey
                }
            });

            const data = {
                success: response.data.status === '1',
                balance: response.data.result,
                balanceEth: (parseInt(response.data.result) / 1e18).toFixed(18)
            };

            this.cache.set(cacheKey, { data, timestamp: Date.now() });
            return data;
        } catch (error) {
            return {
                success: false,
                error: error.message
            };
        }
    }

    /**
     * Etherscan - Get transaction history
     */
    async etherscanGetTransactions(address, page = 1, offset = 10) {
        const api = this.apis.etherscan;
        if (!api.apiKey) {
            throw new Error('Etherscan API key not configured');
        }

        try {
            const response = await axios.get(api.baseUrl, {
                params: {
                    module: 'account',
                    action: 'txlist',
                    address,
                    startblock: 0,
                    endblock: 99999999,
                    page,
                    offset,
                    sort: 'desc',
                    apikey: api.apiKey
                }
            });

            return {
                success: response.data.status === '1',
                transactions: response.data.result
            };
        } catch (error) {
            return {
                success: false,
                error: error.message
            };
        }
    }

    /**
     * BlockCypher - Get Bitcoin address info
     */
    async testBlockCypher() {
        const api = this.apis.blockcypher;
        
        try {
            const url = api.apiKey 
                ? `${api.baseUrl}/btc/main/addrs/1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa?token=${api.apiKey}`
                : `${api.baseUrl}/btc/main/addrs/1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa`;
            
            const response = await axios.get(url, { timeout: 5000 });
            return response.status === 200;
        } catch (error) {
            return false;
        }
    }

    /**
     * BlockCypher - Get BTC address info
     */
    async blockcypherGetAddress(address, coin = 'btc') {
        const api = this.apis.blockcypher;
        const cacheKey = `blockcypher_${coin}_${address}`;
        
        if (this.cache.has(cacheKey)) {
            const cached = this.cache.get(cacheKey);
            if (Date.now() - cached.timestamp < this.cacheTimeout) {
                return cached.data;
            }
        }

        try {
            const url = api.apiKey
                ? `${api.baseUrl}/${coin}/main/addrs/${address}?token=${api.apiKey}`
                : `${api.baseUrl}/${coin}/main/addrs/${address}`;
            
            const response = await axios.get(url);
            
            const data = {
                success: true,
                address: response.data.address,
                balance: response.data.balance,
                balanceBTC: (response.data.balance / 1e8).toFixed(8),
                totalReceived: response.data.total_received,
                totalSent: response.data.total_sent,
                txCount: response.data.n_tx
            };

            this.cache.set(cacheKey, { data, timestamp: Date.now() });
            return data;
        } catch (error) {
            return {
                success: false,
                error: error.message
            };
        }
    }

    /**
     * Infura - Test Ethereum connection
     */
    async testInfura() {
        const api = this.apis.infura;
        if (!api.apiKey) return false;

        try {
            const response = await axios.post(
                `${api.baseUrl}/${api.apiKey}`,
                {
                    jsonrpc: '2.0',
                    method: 'eth_blockNumber',
                    params: [],
                    id: 1
                },
                { timeout: 5000 }
            );
            return response.data.result !== undefined;
        } catch (error) {
            return false;
        }
    }

    /**
     * Infura - Get latest block
     */
    async infuraGetLatestBlock() {
        const api = this.apis.infura;
        if (!api.apiKey) {
            throw new Error('Infura API key not configured');
        }

        try {
            const response = await axios.post(
                `${api.baseUrl}/${api.apiKey}`,
                {
                    jsonrpc: '2.0',
                    method: 'eth_blockNumber',
                    params: [],
                    id: 1
                }
            );

            const blockHex = response.data.result;
            const blockNumber = parseInt(blockHex, 16);

            return {
                success: true,
                blockNumber,
                blockHex
            };
        } catch (error) {
            return {
                success: false,
                error: error.message
            };
        }
    }

    /**
     * Infura - Get ETH balance
     */
    async infuraGetBalance(address) {
        const api = this.apis.infura;
        if (!api.apiKey) {
            throw new Error('Infura API key not configured');
        }

        const cacheKey = `infura_balance_${address}`;
        if (this.cache.has(cacheKey)) {
            const cached = this.cache.get(cacheKey);
            if (Date.now() - cached.timestamp < this.cacheTimeout) {
                return cached.data;
            }
        }

        try {
            const response = await axios.post(
                `${api.baseUrl}/${api.apiKey}`,
                {
                    jsonrpc: '2.0',
                    method: 'eth_getBalance',
                    params: [address, 'latest'],
                    id: 1
                }
            );

            const balanceHex = response.data.result;
            const balanceWei = parseInt(balanceHex, 16);
            const balanceEth = (balanceWei / 1e18).toFixed(18);

            const data = {
                success: true,
                balance: balanceWei.toString(),
                balanceEth
            };

            this.cache.set(cacheKey, { data, timestamp: Date.now() });
            return data;
        } catch (error) {
            return {
                success: false,
                error: error.message
            };
        }
    }

    /**
     * Get API status summary
     */
    getStatus() {
        return Object.keys(this.apis).map(key => ({
            id: key,
            name: this.apis[key].name,
            status: this.apis[key].status,
            hasKey: !!this.apis[key].apiKey,
            baseUrl: this.apis[key].baseUrl
        }));
    }

    /**
     * Clear cache
     */
    clearCache() {
        this.cache.clear();
    }
}

module.exports = { APIIntegrations };
