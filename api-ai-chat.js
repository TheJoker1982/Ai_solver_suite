/**
 * API Endpoint for Bitcoin AI Chat
 * Provides REST API access to the AI brain
 */

const express = require('express');
const { bitcoinJesus } = require('./bitcoin-learning-engine');

const router = express.Router();

// Bitcoin Jesus is always ready (initialized on module load)
async function ensureBitcoinJesusReady() {
    // Bitcoin Jesus is always studying and ready
    return true;
}

// POST /api/ai/chat - Talk to Bitcoin Jesus
router.post('/chat', async (req, res) => {
    try {
        await ensureBitcoinJesusReady();
        
        const { message } = req.body;
        
        if (!message) {
            return res.status(400).json({
                success: false,
                error: 'Message is required'
            });
        }
        
        const response = await bitcoinJesus.chat(message);
        res.json(response);
    } catch (error) {
        res.status(500).json({
            success: false,
            error: error.message
        });
    }
});

// GET /api/ai/status - Get Bitcoin Jesus learning status
router.get('/status', async (req, res) => {
    try {
        await ensureBitcoinJesusReady();
        
        const response = await bitcoinJesus.chat('status');
        res.json(response);
    } catch (error) {
        res.status(500).json({
            success: false,
            error: error.message
        });
    }
});

// GET /api/ai/knowledge - See what Bitcoin Jesus has mastered
router.get('/knowledge', async (req, res) => {
    try {
        await ensureBitcoinJesusReady();
        
        const status = bitcoinJesus.getStatus();
        res.json(status);
    } catch (error) {
        res.status(500).json({
            success: false,
            error: error.message
        });
    }
});

module.exports = router;
