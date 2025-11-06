class EffectsController {
    constructor() {
        this.particlePool = [];
        this.activeEffects = new Set();
        this.init();
    }

    init() {
        this.createParticlePool(100);
        this.setupEventListeners();
    }

    createParticlePool(count) {
        for (let i = 0; i < count; i++) {
            const particle = document.createElement('div');
            particle.className = 'effect-particle';
            particle.style.cssText = `
                position: fixed;
                width: 4px;
                height: 4px;
                border-radius: 50%;
                pointer-events: none;
                z-index: 9999;
                opacity: 0;
            `;
            document.body.appendChild(particle);
            this.particlePool.push(particle);
        }
    }

    setupEventListeners() {
        document.addEventListener('tool-activated', (e) => this.toolActivationEffect(e.detail));
        document.addEventListener('level-up', (e) => this.levelUpEffect(e.detail));
        document.addEventListener('puzzle-solved', (e) => this.puzzleSolvedEffect(e.detail));
        document.addEventListener('scanner-running', (e) => this.scannerEffect(e.detail));
        document.addEventListener('achievement-unlocked', (e) => this.achievementEffect(e.detail));
        document.addEventListener('xp-awarded', (e) => this.xpAwardedEffect(e.detail));
        document.addEventListener('earnings-received', (e) => this.earningsReceivedEffect(e.detail));
    }

    toolActivationEffect(data) {
        const { element, toolName } = data;
        const rect = element?.getBoundingClientRect() || { left: window.innerWidth / 2, top: window.innerHeight / 2 };
        
        this.createNeonPulse(rect.left + rect.width / 2, rect.top + rect.height / 2, '#00ff88');
        this.burstParticles(rect.left + rect.width / 2, rect.top + rect.height / 2, 20, '#00ff88');
        
        if (element) {
            element.style.animation = 'neonGlow 0.5s ease-out';
            setTimeout(() => element.style.animation = '', 500);
        }
    }

    levelUpEffect(data) {
        const { level, rank } = data;
        
        this.createScreenFlash('#FFD700');
        this.createTextExplosion(`LEVEL ${level}!`, window.innerWidth / 2, window.innerHeight / 3);
        this.createTextExplosion(rank, window.innerWidth / 2, window.innerHeight / 2);
        
        this.burstParticles(window.innerWidth / 2, window.innerHeight / 2, 50, '#FFD700');
        
        const audio = new Audio();
        audio.src = 'data:audio/wav;base64,UklGRnoGAABXQVZFZm10IBAAAAABAAEAQB8AAEAfAAABAAgAZGF0YQoGAACBhYqFbF1fdJivrJBhNjVgodDbq2EcBj+a2/LDciUFLIHO8tiJNwgZaLvt559NEAxQp+PwtmMcBjiR1/LMeSwFJHfH8N2QQAoUXrTp66hVFApGn+DyvmwhBTGH0fPTgjMGHm7A7+OZRQ8';
        audio.volume = 0.3;
        audio.play().catch(() => {});
    }

    puzzleSolvedEffect(data) {
        const { btcAmount, puzzleNumber } = data;
        
        this.createScreenFlash('#F7931A');
        this.createConfetti(100);
        this.createTextExplosion(`PUZZLE ${puzzleNumber} SOLVED!`, window.innerWidth / 2, window.innerHeight / 3, '#F7931A');
        this.createTextExplosion(`${btcAmount} BTC`, window.innerWidth / 2, window.innerHeight / 2, '#FFD700');
        
        for (let i = 0; i < 5; i++) {
            setTimeout(() => {
                this.burstParticles(
                    Math.random() * window.innerWidth,
                    Math.random() * window.innerHeight,
                    30,
                    '#F7931A'
                );
            }, i * 200);
        }
    }

    scannerEffect(data) {
        const { element, progress } = data;
        if (!element) return;

        const rect = element.getBoundingClientRect();
        const glowIntensity = Math.sin(Date.now() / 200) * 0.5 + 0.5;
        
        element.style.boxShadow = `
            0 0 ${10 + glowIntensity * 20}px rgba(0, 255, 136, ${0.3 + glowIntensity * 0.3}),
            inset 0 0 ${5 + glowIntensity * 10}px rgba(0, 255, 136, 0.2)
        `;

        if (Math.random() > 0.7) {
            this.createSparkle(
                rect.left + Math.random() * rect.width,
                rect.top + Math.random() * rect.height,
                '#00ff88'
            );
        }
    }

    achievementEffect(data) {
        const { name, badge } = data;
        
        const notification = document.createElement('div');
        notification.className = 'achievement-notification';
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: linear-gradient(135deg, rgba(0,255,136,0.2), rgba(0,200,255,0.2));
            border: 2px solid #00ff88;
            border-radius: 12px;
            padding: 20px;
            color: white;
            font-family: 'Courier New', monospace;
            z-index: 10000;
            animation: slideInRight 0.5s ease-out, neonGlow 2s infinite;
            box-shadow: 0 0 20px rgba(0,255,136,0.5);
        `;
        notification.innerHTML = `
            <div style="font-size: 2rem; margin-bottom: 10px;">${badge || '🏆'}</div>
            <div style="font-size: 0.8rem; color: #00ff88; margin-bottom: 5px;">ACHIEVEMENT UNLOCKED</div>
            <div style="font-size: 1.1rem; font-weight: bold;">${name}</div>
        `;
        
        document.body.appendChild(notification);
        
        this.burstParticles(window.innerWidth - 100, 80, 30, '#00ff88');
        
        setTimeout(() => {
            notification.style.animation = 'slideOutRight 0.5s ease-in';
            setTimeout(() => notification.remove(), 500);
        }, 3000);
    }

    createNeonPulse(x, y, color) {
        const pulse = document.createElement('div');
        pulse.style.cssText = `
            position: fixed;
            left: ${x}px;
            top: ${y}px;
            width: 20px;
            height: 20px;
            border: 2px solid ${color};
            border-radius: 50%;
            pointer-events: none;
            z-index: 9999;
            animation: neonPulse 0.6s ease-out;
        `;
        document.body.appendChild(pulse);
        setTimeout(() => pulse.remove(), 600);
    }

    burstParticles(x, y, count, color) {
        for (let i = 0; i < count; i++) {
            const particle = this.particlePool[i % this.particlePool.length];
            const angle = (Math.PI * 2 * i) / count;
            const velocity = 2 + Math.random() * 3;
            
            particle.style.left = `${x}px`;
            particle.style.top = `${y}px`;
            particle.style.background = color;
            particle.style.opacity = '1';
            
            const duration = 1000 + Math.random() * 500;
            const distance = 50 + Math.random() * 100;
            
            particle.animate([
                {
                    transform: 'translate(0, 0) scale(1)',
                    opacity: 1
                },
                {
                    transform: `translate(${Math.cos(angle) * distance}px, ${Math.sin(angle) * distance}px) scale(0)`,
                    opacity: 0
                }
            ], {
                duration: duration,
                easing: 'cubic-bezier(0, .9, .57, 1)'
            });
        }
    }

    createConfetti(count) {
        const colors = ['#F7931A', '#FFD700', '#00ff88', '#00c8ff', '#ff00ff'];
        
        for (let i = 0; i < count; i++) {
            setTimeout(() => {
                const confetti = document.createElement('div');
                confetti.style.cssText = `
                    position: fixed;
                    left: ${Math.random() * window.innerWidth}px;
                    top: -20px;
                    width: ${5 + Math.random() * 10}px;
                    height: ${5 + Math.random() * 10}px;
                    background: ${colors[Math.floor(Math.random() * colors.length)]};
                    pointer-events: none;
                    z-index: 9999;
                    border-radius: ${Math.random() > 0.5 ? '50%' : '0'};
                `;
                
                document.body.appendChild(confetti);
                
                confetti.animate([
                    {
                        transform: `translate(0, 0) rotate(0deg)`,
                        opacity: 1
                    },
                    {
                        transform: `translate(${Math.random() * 200 - 100}px, ${window.innerHeight + 20}px) rotate(${Math.random() * 720}deg)`,
                        opacity: 0
                    }
                ], {
                    duration: 2000 + Math.random() * 1000,
                    easing: 'cubic-bezier(.25, .46, .45, .94)'
                });
                
                setTimeout(() => confetti.remove(), 3000);
            }, i * 20);
        }
    }

    createTextExplosion(text, x, y, color = '#00ff88') {
        const textEl = document.createElement('div');
        textEl.style.cssText = `
            position: fixed;
            left: ${x}px;
            top: ${y}px;
            transform: translate(-50%, -50%) scale(0);
            font-size: 3rem;
            font-weight: bold;
            color: ${color};
            font-family: 'Courier New', monospace;
            pointer-events: none;
            z-index: 10000;
            text-shadow: 0 0 20px ${color}, 0 0 40px ${color};
            white-space: nowrap;
        `;
        textEl.textContent = text;
        document.body.appendChild(textEl);
        
        textEl.animate([
            {
                transform: 'translate(-50%, -50%) scale(0)',
                opacity: 0
            },
            {
                transform: 'translate(-50%, -50%) scale(1.2)',
                opacity: 1,
                offset: 0.3
            },
            {
                transform: 'translate(-50%, -50%) scale(1)',
                opacity: 1,
                offset: 0.7
            },
            {
                transform: 'translate(-50%, -50%) scale(0.8)',
                opacity: 0
            }
        ], {
            duration: 2000,
            easing: 'cubic-bezier(.25, .46, .45, .94)'
        });
        
        setTimeout(() => textEl.remove(), 2000);
    }

    createSparkle(x, y, color) {
        const sparkle = document.createElement('div');
        sparkle.style.cssText = `
            position: fixed;
            left: ${x}px;
            top: ${y}px;
            width: 4px;
            height: 4px;
            background: ${color};
            border-radius: 50%;
            pointer-events: none;
            z-index: 9999;
            box-shadow: 0 0 10px ${color};
        `;
        document.body.appendChild(sparkle);
        
        sparkle.animate([
            { transform: 'scale(0)', opacity: 0 },
            { transform: 'scale(2)', opacity: 1, offset: 0.5 },
            { transform: 'scale(0)', opacity: 0 }
        ], {
            duration: 600,
            easing: 'ease-out'
        });
        
        setTimeout(() => sparkle.remove(), 600);
    }

    createScreenFlash(color) {
        const flash = document.createElement('div');
        flash.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: ${color};
            pointer-events: none;
            z-index: 9998;
            opacity: 0;
        `;
        document.body.appendChild(flash);
        
        flash.animate([
            { opacity: 0 },
            { opacity: 0.3, offset: 0.1 },
            { opacity: 0 }
        ], {
            duration: 400,
            easing: 'ease-out'
        });
        
        setTimeout(() => flash.remove(), 400);
    }

    triggerToolEffect(toolName, element) {
        document.dispatchEvent(new CustomEvent('tool-activated', {
            detail: { element, toolName }
        }));
    }

    triggerLevelUp(level, rank) {
        document.dispatchEvent(new CustomEvent('level-up', {
            detail: { level, rank }
        }));
    }

    triggerPuzzleSolved(puzzleNumber, btcAmount) {
        document.dispatchEvent(new CustomEvent('puzzle-solved', {
            detail: { puzzleNumber, btcAmount }
        }));
    }

    triggerAchievement(name, badge) {
        document.dispatchEvent(new CustomEvent('achievement-unlocked', {
            detail: { name, badge }
        }));
    }

    xpAwardedEffect(data) {
        const { amount, leveledUp, newLevel, newRank } = data;
        
        const notification = document.createElement('div');
        notification.className = 'xp-notification';
        notification.style.cssText = `
            position: fixed;
            top: 80px;
            right: 20px;
            background: linear-gradient(135deg, rgba(0,255,136,0.2), rgba(0,200,255,0.2));
            border: 2px solid #00ff88;
            border-radius: 12px;
            padding: 15px 25px;
            color: white;
            font-family: 'Courier New', monospace;
            z-index: 10000;
            animation: slideInRight 0.5s ease-out;
            box-shadow: 0 0 20px rgba(0,255,136,0.5);
        `;
        
        notification.innerHTML = `
            <div style="font-size: 1.5rem; font-weight: bold; color: #00ff88;">+${amount} XP</div>
            ${leveledUp ? `<div style="font-size: 1.2rem; margin-top: 10px; color: #ffd700;">LEVEL UP! ${newLevel}</div>` : ''}
            ${leveledUp && newRank ? `<div style="font-size: 0.9rem; margin-top: 5px;">${newRank}</div>` : ''}
        `;
        
        document.body.appendChild(notification);
        
        this.burstParticles(window.innerWidth - 100, 100, 20, '#00ff88');
        
        if (leveledUp) {
            this.levelUpEffect({ level: newLevel, rank: newRank });
        }
        
        setTimeout(() => {
            notification.style.animation = 'slideOutRight 0.5s ease-in';
            setTimeout(() => notification.remove(), 500);
        }, 3000);
    }

    triggerXPAward(amount, leveledUp = false, newLevel = null, newRank = null) {
        document.dispatchEvent(new CustomEvent('xp-awarded', {
            detail: { amount, leveledUp, newLevel, newRank }
        }));
    }

    earningsReceivedEffect(data) {
        const { btcAmount, usdAmount, puzzleNumber } = data;
        
        this.createScreenFlash('#F7931A');
        
        const notification = document.createElement('div');
        notification.className = 'earnings-notification';
        notification.style.cssText = `
            position: fixed;
            top: 120px;
            right: 20px;
            background: linear-gradient(135deg, rgba(247,147,26,0.2), rgba(255,215,0,0.2));
            border: 2px solid #F7931A;
            border-radius: 12px;
            padding: 20px 30px;
            color: white;
            font-family: 'Courier New', monospace;
            z-index: 10000;
            animation: slideInRight 0.5s ease-out, neonGlow 2s infinite;
            box-shadow: 0 0 30px rgba(247,147,26,0.8);
        `;
        
        notification.innerHTML = `
            <div style="font-size: 3rem; margin-bottom: 10px; text-align: center;">💰</div>
            <div style="font-size: 0.8rem; color: #FFD700; margin-bottom: 5px; text-align: center;">EARNINGS</div>
            <div style="font-size: 1.8rem; font-weight: bold; color: #F7931A; text-align: center;">+${btcAmount} BTC</div>
            ${usdAmount ? `<div style="font-size: 1.2rem; color: #00ff88; margin-top: 5px; text-align: center;">$${usdAmount.toFixed(2)}</div>` : ''}
            ${puzzleNumber ? `<div style="font-size: 0.9rem; margin-top: 10px; text-align: center;">Puzzle ${puzzleNumber}</div>` : ''}
        `;
        
        document.body.appendChild(notification);
        
        this.createTextExplosion(
            `+${btcAmount} BTC`, 
            window.innerWidth / 2, 
            window.innerHeight / 3, 
            '#F7931A'
        );
        
        this.burstParticles(window.innerWidth - 150, 180, 40, '#F7931A');
        
        for (let i = 0; i < 3; i++) {
            setTimeout(() => {
                this.createSparkle(
                    window.innerWidth - 150 + (Math.random() - 0.5) * 100,
                    180 + (Math.random() - 0.5) * 100,
                    '#FFD700'
                );
            }, i * 200);
        }
        
        const audio = new Audio();
        audio.src = 'data:audio/wav;base64,UklGRiQAAABXQVZFZm10IBAAAAABAAEARKwAAIhYAQACABAAZGF0YQAAAAA=';
        audio.volume = 0.4;
        audio.play().catch(() => {});
        
        setTimeout(() => {
            notification.style.animation = 'slideOutRight 0.5s ease-in';
            setTimeout(() => notification.remove(), 500);
        }, 4000);
    }

    triggerEarningsReceived(btcAmount, usdAmount = null, puzzleNumber = null) {
        document.dispatchEvent(new CustomEvent('earnings-received', {
            detail: { btcAmount, usdAmount, puzzleNumber }
        }));
    }
}

const effectsController = new EffectsController();

if (typeof window !== 'undefined') {
    window.effectsController = effectsController;
}
