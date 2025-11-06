/**
 * Interactive AI Debugger for Crypto Heist
 * Monitors errors, analyzes issues, and provides real-time debugging assistance
 */

class AIDebugger {
    constructor() {
        this.errors = [];
        this.apiCalls = [];
        this.performance = [];
        this.maxStoredErrors = 50;
        this.isActive = true;
        
        // Auto-initialize
        this.init();
    }

    init() {
        console.log('🔍 AI Debugger: ACTIVE');
        
        // Monitor console errors
        this.interceptErrors();
        
        // Monitor API calls
        this.interceptFetch();
        
        // Monitor performance
        this.monitorPerformance();
        
        // Check for errors every 2 seconds
        setInterval(() => this.analyzeRecentErrors(), 2000);
    }

    /**
     * Intercept and log console errors
     */
    interceptErrors() {
        const originalError = console.error;
        const self = this;
        
        console.error = function(...args) {
            // Store error
            self.logError({
                type: 'console',
                message: args.join(' '),
                stack: new Error().stack,
                timestamp: Date.now()
            });
            
            // Call original
            originalError.apply(console, args);
        };

        // Catch unhandled errors
        window.addEventListener('error', (event) => {
            self.logError({
                type: 'runtime',
                message: event.message,
                filename: event.filename,
                line: event.lineno,
                col: event.colno,
                stack: event.error?.stack,
                timestamp: Date.now()
            });
        });

        // Catch promise rejections
        window.addEventListener('unhandledrejection', (event) => {
            self.logError({
                type: 'promise',
                message: event.reason?.message || String(event.reason),
                stack: event.reason?.stack,
                timestamp: Date.now()
            });
        });
    }

    /**
     * Intercept and monitor fetch calls
     */
    interceptFetch() {
        const originalFetch = window.fetch;
        const self = this;
        
        window.fetch = async function(...args) {
            const startTime = performance.now();
            const url = args[0];
            
            try {
                const response = await originalFetch.apply(this, args);
                const endTime = performance.now();
                
                // Clone response to read it
                const clone = response.clone();
                let data;
                try {
                    data = await clone.json();
                } catch (e) {
                    data = await clone.text();
                }
                
                // Log API call
                self.logAPICall({
                    url: url,
                    method: args[1]?.method || 'GET',
                    status: response.status,
                    success: response.ok,
                    duration: endTime - startTime,
                    response: data,
                    timestamp: Date.now()
                });
                
                // If error response, log it
                if (!response.ok) {
                    self.logError({
                        type: 'api',
                        message: `API Error: ${url} returned ${response.status}`,
                        url: url,
                        status: response.status,
                        response: data,
                        timestamp: Date.now()
                    });
                }
                
                return response;
            } catch (error) {
                const endTime = performance.now();
                
                // Log failed API call
                self.logAPICall({
                    url: url,
                    method: args[1]?.method || 'GET',
                    status: 0,
                    success: false,
                    duration: endTime - startTime,
                    error: error.message,
                    timestamp: Date.now()
                });
                
                self.logError({
                    type: 'network',
                    message: `Network Error: ${url} - ${error.message}`,
                    url: url,
                    error: error.message,
                    timestamp: Date.now()
                });
                
                throw error;
            }
        };
    }

    /**
     * Monitor page performance
     */
    monitorPerformance() {
        // Monitor page load time
        window.addEventListener('load', () => {
            const perfData = performance.timing;
            const pageLoadTime = perfData.loadEventEnd - perfData.navigationStart;
            
            this.performance.push({
                metric: 'page_load',
                value: pageLoadTime,
                timestamp: Date.now()
            });
            
            if (pageLoadTime > 3000) {
                console.warn(`⚠️ Slow page load: ${pageLoadTime}ms`);
            }
        });
    }

    /**
     * Log an error
     */
    logError(error) {
        this.errors.push(error);
        
        // Keep only recent errors
        if (this.errors.length > this.maxStoredErrors) {
            this.errors.shift();
        }
        
        // Show visual notification for critical errors
        if (error.type !== 'console') {
            this.showErrorNotification(error);
        }
    }

    /**
     * Log an API call
     */
    logAPICall(call) {
        this.apiCalls.push(call);
        
        // Keep only last 100 calls
        if (this.apiCalls.length > 100) {
            this.apiCalls.shift();
        }
    }

    /**
     * Analyze recent errors and provide suggestions
     */
    analyzeRecentErrors() {
        if (!this.isActive || this.errors.length === 0) return;
        
        // Get errors from last 5 seconds
        const now = Date.now();
        const recentErrors = this.errors.filter(e => now - e.timestamp < 5000);
        
        if (recentErrors.length === 0) return;
        
        // Group by type
        const errorTypes = {};
        recentErrors.forEach(err => {
            const type = err.type;
            if (!errorTypes[type]) errorTypes[type] = [];
            errorTypes[type].push(err);
        });
        
        // Analyze each type
        for (const [type, errors] of Object.entries(errorTypes)) {
            if (errors.length > 2) {
                console.warn(`🔍 AI Debugger: Multiple ${type} errors detected (${errors.length})`);
                this.provideSuggestions(type, errors);
            }
        }
    }

    /**
     * Provide debugging suggestions based on error type
     */
    provideSuggestions(type, errors) {
        const suggestions = {
            'api': '💡 API errors detected. Check if the server is running and endpoints are correct.',
            'network': '💡 Network errors detected. Check your internet connection or CORS settings.',
            'runtime': '💡 Runtime errors detected. Check browser console for stack traces.',
            'promise': '💡 Promise rejections detected. Check async/await code for proper error handling.'
        };
        
        if (suggestions[type]) {
            console.info(suggestions[type]);
        }
    }

    /**
     * Show visual error notification
     */
    showErrorNotification(error) {
        // Create notification element
        const notification = document.createElement('div');
        notification.className = 'ai-debugger-notification';
        notification.innerHTML = `
            <div class="debug-notification">
                <div class="debug-header">
                    <span class="debug-icon">🔍</span>
                    <span class="debug-title">AI Debugger Alert</span>
                    <button class="debug-close" onclick="this.parentElement.parentElement.remove()">×</button>
                </div>
                <div class="debug-body">
                    <div class="debug-type">${error.type.toUpperCase()} ERROR</div>
                    <div class="debug-message">${error.message}</div>
                    ${error.url ? `<div class="debug-url">URL: ${error.url}</div>` : ''}
                    <button class="debug-ask-ai" onclick="window.aiDebugger.askAI('${error.message.replace(/'/g, "\\'")}')">
                        Ask AI for Help 🤖
                    </button>
                </div>
            </div>
        `;
        
        // Add styles
        if (!document.getElementById('ai-debugger-styles')) {
            const style = document.createElement('style');
            style.id = 'ai-debugger-styles';
            style.textContent = `
                .ai-debugger-notification {
                    position: fixed;
                    bottom: 20px;
                    right: 20px;
                    z-index: 99999;
                    animation: slideInRight 0.3s ease-out;
                }
                
                .debug-notification {
                    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
                    border: 2px solid #00ff88;
                    border-radius: 12px;
                    padding: 16px;
                    box-shadow: 0 8px 32px rgba(0, 255, 136, 0.3);
                    max-width: 400px;
                    font-family: 'Rajdhani', sans-serif;
                }
                
                .debug-header {
                    display: flex;
                    align-items: center;
                    gap: 8px;
                    margin-bottom: 12px;
                }
                
                .debug-icon {
                    font-size: 20px;
                }
                
                .debug-title {
                    color: #00ff88;
                    font-weight: 600;
                    font-size: 16px;
                    flex: 1;
                }
                
                .debug-close {
                    background: none;
                    border: none;
                    color: #fff;
                    font-size: 24px;
                    cursor: pointer;
                    opacity: 0.7;
                    transition: opacity 0.2s;
                }
                
                .debug-close:hover {
                    opacity: 1;
                }
                
                .debug-body {
                    color: #fff;
                }
                
                .debug-type {
                    color: #ff4757;
                    font-weight: 600;
                    font-size: 12px;
                    margin-bottom: 8px;
                }
                
                .debug-message {
                    color: #ddd;
                    font-size: 14px;
                    margin-bottom: 8px;
                    line-height: 1.4;
                }
                
                .debug-url {
                    color: #5f9ea0;
                    font-size: 12px;
                    margin-bottom: 12px;
                    word-break: break-all;
                }
                
                .debug-ask-ai {
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    border: none;
                    padding: 8px 16px;
                    border-radius: 6px;
                    cursor: pointer;
                    font-family: 'Rajdhani', sans-serif;
                    font-weight: 600;
                    transition: all 0.2s;
                }
                
                .debug-ask-ai:hover {
                    transform: translateY(-2px);
                    box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
                }
                
                @keyframes slideInRight {
                    from {
                        transform: translateX(400px);
                        opacity: 0;
                    }
                    to {
                        transform: translateX(0);
                        opacity: 1;
                    }
                }
            `;
            document.head.appendChild(style);
        }
        
        // Add to page
        document.body.appendChild(notification);
        
        // Auto-remove after 10 seconds
        setTimeout(() => {
            notification.style.animation = 'slideInRight 0.3s ease-out reverse';
            setTimeout(() => notification.remove(), 300);
        }, 10000);
    }

    /**
     * Ask AI for help with specific error
     */
    async askAI(errorMessage) {
        console.log('🤖 Asking AI for help with:', errorMessage);
        
        // Build debug context
        const context = {
            error: errorMessage,
            recent_errors: this.errors.slice(-5),
            failed_apis: this.apiCalls.filter(c => !c.success).slice(-5),
            page: window.location.pathname
        };
        
        try {
            const response = await fetch('/api/ai/debug', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(context)
            });
            
            const data = await response.json();
            
            if (data.success) {
                // Show AI response in a modal
                this.showAIResponse(data.response);
            }
        } catch (error) {
            console.error('Failed to get AI help:', error);
        }
    }

    /**
     * Show AI response in modal
     */
    showAIResponse(response) {
        const modal = document.createElement('div');
        modal.className = 'ai-debug-modal';
        modal.innerHTML = `
            <div class="ai-debug-modal-content">
                <div class="ai-debug-modal-header">
                    <h3>🤖 AI Debug Assistant</h3>
                    <button onclick="this.closest('.ai-debug-modal').remove()">×</button>
                </div>
                <div class="ai-debug-modal-body">
                    <pre>${response}</pre>
                </div>
                <div class="ai-debug-modal-footer">
                    <button onclick="this.closest('.ai-debug-modal').remove()">Close</button>
                </div>
            </div>
        `;
        
        // Add modal styles
        if (!document.getElementById('ai-debug-modal-styles')) {
            const style = document.createElement('style');
            style.id = 'ai-debug-modal-styles';
            style.textContent = `
                .ai-debug-modal {
                    position: fixed;
                    top: 0;
                    left: 0;
                    right: 0;
                    bottom: 0;
                    background: rgba(0, 0, 0, 0.8);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    z-index: 999999;
                }
                
                .ai-debug-modal-content {
                    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
                    border: 2px solid #00ff88;
                    border-radius: 16px;
                    max-width: 600px;
                    width: 90%;
                    max-height: 80vh;
                    overflow-y: auto;
                    box-shadow: 0 16px 48px rgba(0, 255, 136, 0.4);
                }
                
                .ai-debug-modal-header {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    padding: 20px;
                    border-bottom: 1px solid rgba(0, 255, 136, 0.3);
                }
                
                .ai-debug-modal-header h3 {
                    color: #00ff88;
                    margin: 0;
                    font-family: 'Rajdhani', sans-serif;
                }
                
                .ai-debug-modal-header button {
                    background: none;
                    border: none;
                    color: white;
                    font-size: 32px;
                    cursor: pointer;
                    opacity: 0.7;
                    transition: opacity 0.2s;
                }
                
                .ai-debug-modal-header button:hover {
                    opacity: 1;
                }
                
                .ai-debug-modal-body {
                    padding: 20px;
                    color: white;
                    font-family: 'Rajdhani', sans-serif;
                }
                
                .ai-debug-modal-body pre {
                    white-space: pre-wrap;
                    line-height: 1.6;
                }
                
                .ai-debug-modal-footer {
                    padding: 20px;
                    border-top: 1px solid rgba(0, 255, 136, 0.3);
                    text-align: right;
                }
                
                .ai-debug-modal-footer button {
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    border: none;
                    padding: 10px 24px;
                    border-radius: 8px;
                    cursor: pointer;
                    font-family: 'Rajdhani', sans-serif;
                    font-weight: 600;
                    transition: all 0.2s;
                }
                
                .ai-debug-modal-footer button:hover {
                    transform: translateY(-2px);
                    box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
                }
            `;
            document.head.appendChild(style);
        }
        
        document.body.appendChild(modal);
    }

    /**
     * Get debug report
     */
    getReport() {
        return {
            errors: this.errors,
            failed_apis: this.apiCalls.filter(c => !c.success),
            slow_apis: this.apiCalls.filter(c => c.duration > 1000),
            total_errors: this.errors.length,
            total_api_calls: this.apiCalls.length,
            error_rate: this.errors.length / Math.max(this.apiCalls.length, 1)
        };
    }

    /**
     * Clear all logged data
     */
    clear() {
        this.errors = [];
        this.apiCalls = [];
        this.performance = [];
        console.log('🔍 AI Debugger: Data cleared');
    }

    /**
     * Toggle debugger on/off
     */
    toggle() {
        this.isActive = !this.isActive;
        console.log(`🔍 AI Debugger: ${this.isActive ? 'ACTIVE' : 'INACTIVE'}`);
        return this.isActive;
    }
}

// Auto-initialize debugger
window.aiDebugger = new AIDebugger();

// Add global helper function
window.getDebugReport = () => {
    const report = window.aiDebugger.getReport();
    console.table(report.errors);
    console.table(report.failed_apis);
    return report;
};
