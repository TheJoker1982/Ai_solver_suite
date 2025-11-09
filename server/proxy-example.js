/*
  Minimal secure proxy example (Express)
  - Reads backend secrets from environment variables (so DO NOT store secrets in source).
  - Example endpoints: /proxy/blockstream/..., /proxy/eth
  - Uses simple rate limiting and CORS whitelist.
  - For production, run this on your server and store secrets in the platform's secret manager.
*/

const express = require('express');
const fetch = require('node-fetch'); // npm i node-fetch@2
const rateLimit = require('express-rate-limit'); // npm i express-rate-limit
const helmet = require('helmet');
const mcache = require('memory-cache');

const app = express();

app.use(helmet());
app.use(express.json());

// Rate limit (adjust to your needs)
const limiter = rateLimit({
  windowMs: 10 * 1000, // 10s
  max: 20 // max 20 requests per window per IP
});
app.use(limiter);

// CORS whitelist - only allow your frontend
const allowedOrigins = [
  'https://yourdomain.com',
  'http://localhost:3000'
];
app.use(function (req, res, next) {
  const origin = req.headers.origin;
  if (allowedOrigins.includes(origin)) {
    res.setHeader('Access-Control-Allow-Origin', origin);
  }
  res.header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization');
  next();
});

// Simple in-memory cache helper
const cache = new mcache.Cache();

function cached(key, ttlMs, fetcher) {
  const hit = cache.get(key);
  if (hit) return Promise.resolve(hit);
  return fetcher().then(result => {
    cache.put(key, result, ttlMs);
    return result;
  });
}

// Environment-configured endpoints and keys (set via your backend secrets manager)
const BLOCKSTREAM_API_URL = process.env.BLOCKSTREAM_API_URL || 'https://blockstream.info/api';
const BLOCKSTREAM_API_KEY = process.env.BLOCKSTREAM_API_KEY || null; // optional

// Example: /proxy/blockstream/blocks/tip/height
app.get('/proxy/blockstream/blocks/tip/height', async (req, res) => {
  try {
    const key = 'blockstream:blockheight';
    const result = await cached(key, 5000, async () => {
      const url = `${BLOCKSTREAM_API_URL}/blocks/tip/height`;
      const headers = {};
      if (BLOCKSTREAM_API_KEY) headers['x-api-key'] = BLOCKSTREAM_API_KEY;
      const r = await fetch(url, { headers, timeout: 5000 });
      if (!r.ok) {
        const text = await r.text().catch(() => '');
        throw new Error('Upstream error: ' + r.status + ' ' + text);
      }
      const text = await r.text();
      return text;
    });
    res.set('Content-Type', 'text/plain').send(result);
  } catch (err) {
    console.error('proxy error', err);
    res.status(502).json({ error: 'Upstream fetch failed', message: err.message });
  }
});

// Example Ethereum JSON-RPC proxy (POST)
const ETH_RPC_URL = process.env.ETH_RPC_URL || null;
app.post('/proxy/eth', async (req, res) => {
  if (!ETH_RPC_URL) return res.status(500).json({ error: 'ETH_RPC_URL not configured' });
  try {
    // Basic validation: no broadcasting of private keys allowed
    const body = req.body;
    // Prevent direct eth_sendRawTransaction from browser clients.
    if (body && body.method === 'eth_sendRawTransaction') {
      return res.status(403).json({ error: 'Broadcasting transactions is disabled via browser proxy. Use server-side flow.' });
    }
    const r = await fetch(ETH_RPC_URL, {
      method: 'POST',
      body: JSON.stringify(body),
      headers: { 'Content-Type': 'application/json' },
      timeout: 8000
    });
    const data = await r.json();
    res.json(data);
  } catch (err) {
    console.error('eth proxy error', err);
    res.status(502).json({ error: 'ETH upstream error', message: err.message });
  }
});

// Start
const port = process.env.PORT || 4000;
app.listen(port, () => {
  console.log(`Proxy listening on ${port}`);
});
