/**
 * CRYPTO HEIST - AI CHAT INTERFACE
 * 
 * User-facing interface to interact with the dedicated Bitcoin AI brain.
 * Works offline, no external API needed.
 */

const { bitcoinAI } = require('./ai-brain');

class BitcoinAIChat {
    constructor() {
        this.conversationHistory = [];
        this.ready = false;
    }

    /**
     * Initialize the AI chat system
     */
    async initialize() {
        console.log('💬 Initializing AI Chat Interface...');
        
        // Initialize the AI brain
        this.ready = await bitcoinAI.initialize();
        
        if (this.ready) {
            console.log('✅ AI Chat ready!');
            this.addMessage('system', 'Bitcoin AI Brain initialized. Ready to assist with puzzle solving!');
        } else {
            console.log('❌ AI Chat initialization failed');
        }
        
        return this.ready;
    }

    /**
     * Send a message to the AI and get a response
     */
    async chat(userMessage) {
        if (!this.ready) {
            return {
                success: false,
                message: 'AI not initialized. Please wait...'
            };
        }
        
        // Add user message to history
        this.addMessage('user', userMessage);
        
        // Query the AI brain
        const response = await this.processMessage(userMessage);
        
        // Add AI response to history
        this.addMessage('ai', response.message);
        
        return response;
    }

    /**
     * Process user message and generate AI response
     */
    async processMessage(message) {
        const lowerMessage = message.toLowerCase();
        
        // Status check
        if (lowerMessage.includes('status') || lowerMessage.includes('how are you')) {
            const status = bitcoinAI.getStatus();
            return {
                success: true,
                message: `🧠 AI Status:\n` +
                    `✅ Knowledge Score: ${status.knowledgeScore}/100\n` +
                    `📚 Files Studied: ${status.filesStudied}/${status.totalFiles}\n` +
                    `🔧 Bitcoin Operations: ${status.categories.bitcoinOperations}\n` +
                    `🔤 Character Sets: ${status.categories.characterSets}\n` +
                    `🔐 Crypto Methods: ${status.categories.cryptography}\n` +
                    `📊 Patterns: ${status.categories.patterns}`,
                data: status
            };
        }
        
        // Knowledge demonstration
        if (lowerMessage.includes('what do you know') || lowerMessage.includes('what have you learned')) {
            const demo = bitcoinAI.demonstrateKnowledge();
            return {
                success: true,
                message: `📚 Here's what I learned (Knowledge Score: ${demo.knowledgeScore}/100):\n\n` +
                    demo.demonstrations.join('\n') +
                    `\n\n📊 Total concepts learned: ${demo.totalLearned}`,
                data: demo
            };
        }
        
        // Bitcoin operations query
        if (lowerMessage.includes('bitcoin') || lowerMessage.includes('hash') || lowerMessage.includes('address')) {
            const result = bitcoinAI.query('bitcoin operations');
            return {
                success: true,
                message: `🔧 ${result.summary}\n\nKnown operations: ${result.knowledge ? Object.keys(result.knowledge).join(', ') : 'Loading...'}`,
                data: result
            };
        }
        
        // Character set query
        if (lowerMessage.includes('character') || lowerMessage.includes('charset') || lowerMessage.includes('phonetic')) {
            const result = bitcoinAI.query('character sets');
            return {
                success: true,
                message: `🔤 ${result.summary}\n\nKnown charsets: ${result.knowledge ? Object.keys(result.knowledge).join(', ') : 'Loading...'}`,
                data: result
            };
        }
        
        // Cryptography query
        if (lowerMessage.includes('crypto') || lowerMessage.includes('secp256k1') || lowerMessage.includes('key derivation')) {
            const result = bitcoinAI.query('cryptography');
            return {
                success: true,
                message: `🔐 ${result.summary}\n\nKnown methods: ${result.knowledge ? Object.keys(result.knowledge).join(', ') : 'Loading...'}`,
                data: result
            };
        }
        
        // Pattern query
        if (lowerMessage.includes('pattern') || lowerMessage.includes('algorithm') || lowerMessage.includes('derivation')) {
            const result = bitcoinAI.query('patterns');
            return {
                success: true,
                message: `📊 ${result.summary}\n\nKnown patterns: ${result.knowledge ? Object.keys(result.knowledge).join(', ') : 'Loading...'}`,
                data: result
            };
        }
        
        // Help
        if (lowerMessage.includes('help')) {
            return {
                success: true,
                message: `💡 I'm your dedicated Bitcoin AI assistant! Ask me about:\n\n` +
                    `🔧 Bitcoin operations (hashing, encoding, keys)\n` +
                    `🔤 Character sets (ISO-8859, UTF-16, phonetic analysis)\n` +
                    `🔐 Cryptography (secp256k1, BIP32/44, HD wallets)\n` +
                    `📊 Patterns (algorithm derivation, rotation, offsets)\n` +
                    `📈 Status (my knowledge score and learning progress)\n\n` +
                    `Try: "What do you know?" or "Status" or "Tell me about Bitcoin hashing"`
            };
        }
        
        // Default response - general query
        const result = bitcoinAI.query(message);
        return {
            success: true,
            message: result.summary || 'I\'m still learning about that topic. Try asking about Bitcoin operations, character sets, cryptography, or patterns!',
            data: result
        };
    }

    /**
     * Add message to conversation history
     */
    addMessage(sender, message) {
        this.conversationHistory.push({
            sender,
            message,
            timestamp: new Date().toISOString()
        });
    }

    /**
     * Get conversation history
     */
    getHistory() {
        return this.conversationHistory;
    }

    /**
     * Clear conversation history
     */
    clearHistory() {
        this.conversationHistory = [];
    }
}

// Create singleton instance
const aiChat = new BitcoinAIChat();

module.exports = { BitcoinAIChat, aiChat };
