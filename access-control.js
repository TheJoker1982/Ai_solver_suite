/**
 * Client-Side DRM and Access Control
 * Prevents unauthorized copying, downloading, and modification
 */

class AccessControl {
    constructor() {
        this.tier = 'free'; // Default tier
        this.userId = 'anonymous';
        this.sessionId = this.generateSessionId();
        this.initDRM();
    }

    generateSessionId() {
        return `session_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
    }

    /**
     * Initialize DRM protection measures
     */
    initDRM() {
        // Disable right-click context menu
        document.addEventListener('contextmenu', (e) => {
            e.preventDefault();
            this.showDRMWarning('Right-click disabled. Content is protected.');
            return false;
        });

        // Disable keyboard shortcuts for copying/saving
        document.addEventListener('keydown', (e) => {
            // Disable Ctrl+S (Save)
            if ((e.ctrlKey || e.metaKey) && e.key === 's') {
                e.preventDefault();
                this.showDRMWarning('File saving disabled. Content is protected.');
                return false;
            }

            // Disable Ctrl+C on code/sensitive areas
            if ((e.ctrlKey || e.metaKey) && e.key === 'c') {
                if (e.target.classList.contains('protected-content')) {
                    e.preventDefault();
                    this.showDRMWarning('Copying disabled on protected content.');
                    return false;
                }
            }

            // Disable F12, Ctrl+Shift+I (DevTools)
            if (e.key === 'F12' || ((e.ctrlKey || e.metaKey) && e.shiftKey && e.key === 'I')) {
                e.preventDefault();
                this.showDRMWarning('Developer tools access restricted.');
                return false;
            }
        });

        // Disable text selection on protected elements
        document.querySelectorAll('.protected-content').forEach(el => {
            el.style.userSelect = 'none';
            el.style.webkitUserSelect = 'none';
            el.style.mozUserSelect = 'none';
        });

        // Add watermark to all pages
        this.addWatermark();

        // Track usage
        this.trackSession();
    }

    /**
     * Show DRM warning message
     */
    showDRMWarning(message) {
        const warning = document.createElement('div');
        warning.className = 'drm-warning';
        warning.textContent = `🔒 ${message}`;
        warning.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: rgba(255, 0, 0, 0.9);
            color: white;
            padding: 15px 20px;
            border-radius: 8px;
            z-index: 10000;
            font-weight: bold;
            animation: fadeInOut 3s forwards;
        `;
        document.body.appendChild(warning);

        setTimeout(() => warning.remove(), 3000);
    }

    /**
     * Add invisible watermark to page
     */
    addWatermark() {
        const watermark = document.createElement('div');
        watermark.className = 'page-watermark';
        watermark.textContent = `Session: ${this.sessionId} | User: ${this.userId} | CRYPTO HEIST © 2025`;
        watermark.style.cssText = `
            position: fixed;
            bottom: 5px;
            right: 5px;
            font-size: 8px;
            color: rgba(255, 255, 255, 0.1);
            pointer-events: none;
            z-index: 9999;
        `;
        document.body.appendChild(watermark);
    }

    /**
     * Track user session
     */
    async trackSession() {
        const sessionData = {
            sessionId: this.sessionId,
            userId: this.userId,
            tier: this.tier,
            page: window.location.pathname,
            timestamp: new Date().toISOString(),
            userAgent: navigator.userAgent
        };

        // Send to server for tracking (implement backend endpoint)
        // await fetch('/api/track-session', {
        //     method: 'POST',
        //     headers: { 'Content-Type': 'application/json' },
        //     body: JSON.stringify(sessionData)
        // });
    }

    /**
     * Check if user can access a feature
     */
    async checkAccess(featureName, dailyUsage = {}) {
        try {
            const response = await fetch('/api/knowledge/check-access', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    toolName: 'platform',
                    featureName,
                    userTier: this.tier,
                    dailyUsage
                })
            });

            const data = await response.json();
            return data.access;
        } catch (error) {
            console.error('Access check failed:', error);
            return { allowed: false, reason: 'Access check failed' };
        }
    }

    /**
     * Show upgrade prompt for premium features
     */
    showUpgradePrompt(feature) {
        const modal = document.createElement('div');
        modal.innerHTML = `
            <div style="
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                background: linear-gradient(135deg, #1a0033 0%, #000 50%, #001a33 100%);
                border: 2px solid #00ffff;
                border-radius: 15px;
                padding: 30px;
                max-width: 500px;
                z-index: 10001;
                box-shadow: 0 0 30px rgba(0, 255, 255, 0.5);
            ">
                <h2 style="color: #00ffff; margin-bottom: 20px; font-size: 24px;">
                    🔒 Premium Feature
                </h2>
                <p style="color: #fff; margin-bottom: 20px;">
                    <strong>${feature}</strong> requires a Premium subscription.
                </p>
                <p style="color: #aaa; margin-bottom: 20px;">
                    Upgrade to Premium for just <strong style="color: #F7931A;">$0.99/month</strong> and unlock:
                </p>
                <ul style="color: #fff; margin-bottom: 20px; list-style: none;">
                    <li>✅ Unlimited AI queries</li>
                    <li>✅ Unlimited HD derivations</li>
                    <li>✅ Brute force scanner access</li>
                    <li>✅ Puzzle data export</li>
                    <li>✅ Priority support</li>
                </ul>
                <div style="display: flex; gap: 10px;">
                    <button onclick="window.location.href='/subscribe'" style="
                        flex: 1;
                        background: linear-gradient(135deg, #00ffff, #0080ff);
                        color: #000;
                        border: none;
                        padding: 12px;
                        border-radius: 5px;
                        font-weight: bold;
                        cursor: pointer;
                    ">Upgrade Now</button>
                    <button onclick="this.parentElement.parentElement.parentElement.remove()" style="
                        flex: 1;
                        background: #333;
                        color: #fff;
                        border: none;
                        padding: 12px;
                        border-radius: 5px;
                        cursor: pointer;
                    ">Maybe Later</button>
                </div>
            </div>
            <div onclick="this.parentElement.remove()" style="
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0, 0, 0, 0.8);
                z-index: 10000;
            "></div>
        `;
        document.body.appendChild(modal);
    }

    /**
     * Set user tier (from authentication)
     */
    setUserTier(tier, userId) {
        this.tier = tier;
        this.userId = userId;
    }
}

// Initialize access control on page load
const accessControl = new AccessControl();

// Make available globally
window.accessControl = accessControl;

// Add CSS animation
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeInOut {
        0% { opacity: 0; transform: translateY(-20px); }
        20% { opacity: 1; transform: translateY(0); }
        80% { opacity: 1; transform: translateY(0); }
        100% { opacity: 0; transform: translateY(-20px); }
    }

    .protected-content {
        user-select: none !important;
        -webkit-user-select: none !important;
        -moz-user-select: none !important;
    }
`;
document.head.appendChild(style);
