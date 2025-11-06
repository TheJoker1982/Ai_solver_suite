/**
 * 3D BLOCKCHAIN CITY - EXPANDED
 * 
 * Full GTA-style explorable city with:
 * - Explorable streets and buildings
 * - Interactive NPCs
 * - Blockchain terminals (Bitcoin, Ethereum, Bitcoin Cash)
 * - Mission locations (rescue missions, street fights)
 * - Dynamic weather and day/night cycle
 */

const BABYLON = require('@babylonjs/core');

class BlockchainCity3D {
    constructor(canvasId) {
        this.canvasId = canvasId;
        this.engine = null;
        this.scene = null;
        this.camera = null;
        this.player = null;
        
        this.npcs = [];
        this.buildings = [];
        this.terminals = [];
        this.missionMarkers = [];
        
        this.timeOfDay = 12; // 0-24 hours
        this.weather = 'clear'; // clear, rain, fog
    }

    /**
     * Initialize the 3D city
     */
    async initialize() {
        const canvas = document.getElementById(this.canvasId);
        if (!canvas) {
            throw new Error(`Canvas #${this.canvasId} not found`);
        }

        // Create Babylon engine and scene
        this.engine = new BABYLON.Engine(canvas, true);
        this.scene = new BABYLON.Scene(this.engine);
        this.scene.clearColor = new BABYLON.Color3(0.02, 0.02, 0.1);

        // Setup camera (third-person)
        this.setupCamera();

        // Setup lighting
        this.setupLighting();

        // Build city
        await this.buildCity();

        // Create player character
        this.createPlayer();

        // Spawn NPCs
        this.spawnNPCs();

        // Add blockchain terminals
        this.addBlockchainTerminals();

        // Add mission markers
        this.addMissionMarkers();

        // Start render loop
        this.engine.runRenderLoop(() => {
            this.update();
            this.scene.render();
        });

        // Handle window resize
        window.addEventListener('resize', () => {
            this.engine.resize();
        });

        console.log('🏙️ 3D Blockchain City initialized!');
    }

    /**
     * Setup third-person camera
     */
    setupCamera() {
        this.camera = new BABYLON.ArcRotateCamera(
            'camera',
            -Math.PI / 2,
            Math.PI / 3,
            20,
            new BABYLON.Vector3(0, 5, 0),
            this.scene
        );
        this.camera.attachControl(this.scene.getEngine().getRenderingCanvas(), true);
        this.camera.lowerRadiusLimit = 5;
        this.camera.upperRadiusLimit = 50;
        this.camera.wheelPrecision = 20;
    }

    /**
     * Setup dynamic lighting (day/night cycle)
     */
    setupLighting() {
        // Hemispheric light (ambient)
        this.ambientLight = new BABYLON.HemisphericLight(
            'ambient',
            new BABYLON.Vector3(0, 1, 0),
            this.scene
        );
        this.ambientLight.intensity = 0.6;

        // Directional light (sun)
        this.sunLight = new BABYLON.DirectionalLight(
            'sun',
            new BABYLON.Vector3(1, -1, 1),
            this.scene
        );
        this.sunLight.intensity = 0.8;

        // Point lights for street lamps
        this.streetLights = [];
    }

    /**
     * Build the city
     */
    async buildCity() {
        // Ground
        const ground = BABYLON.MeshBuilder.CreateGround(
            'ground',
            { width: 200, height: 200 },
            this.scene
        );
        const groundMat = new BABYLON.StandardMaterial('groundMat', this.scene);
        groundMat.diffuseColor = new BABYLON.Color3(0.2, 0.2, 0.2);
        ground.material = groundMat;

        // City blocks
        this.createCityBlock(-50, -50, 'downtown'); // Downtown area
        this.createCityBlock(50, -50, 'tech-district'); // Tech district
        this.createCityBlock(-50, 50, 'industrial'); // Industrial
        this.createCityBlock(50, 50, 'residential'); // Residential

        // Roads
        this.createRoads();

        // Street lamps
        this.createStreetLamps();

        // Skyscrapers
        this.createSkyscraper(-40, 0, -40, 50);
        this.createSkyscraper(40, 0, -40, 60);
        this.createSkyscraper(-40, 0, 40, 45);
        this.createSkyscraper(40, 0, 40, 55);
    }

    /**
     * Create a city block
     */
    createCityBlock(x, z, type) {
        const blockSize = 40;
        const buildingCount = 4;

        for (let i = 0; i < buildingCount; i++) {
            const bx = x + (Math.random() - 0.5) * blockSize;
            const bz = z + (Math.random() - 0.5) * blockSize;
            const height = 10 + Math.random() * 20;
            
            this.createBuilding(bx, 0, bz, height, type);
        }
    }

    /**
     * Create a single building
     */
    createBuilding(x, y, z, height, type) {
        const building = BABYLON.MeshBuilder.CreateBox(
            `building_${this.buildings.length}`,
            { width: 8, height, depth: 8 },
            this.scene
        );
        
        building.position = new BABYLON.Vector3(x, height / 2, z);

        // Material based on building type
        const mat = new BABYLON.StandardMaterial(`buildingMat_${this.buildings.length}`, this.scene);
        
        switch (type) {
            case 'downtown':
                mat.diffuseColor = new BABYLON.Color3(0.3, 0.3, 0.4);
                mat.emissiveColor = new BABYLON.Color3(0.1, 0.1, 0.2);
                break;
            case 'tech-district':
                mat.diffuseColor = new BABYLON.Color3(0.2, 0.4, 0.6);
                mat.emissiveColor = new BABYLON.Color3(0.0, 0.2, 0.4);
                break;
            case 'industrial':
                mat.diffuseColor = new BABYLON.Color3(0.4, 0.3, 0.2);
                break;
            case 'residential':
                mat.diffuseColor = new BABYLON.Color3(0.5, 0.4, 0.3);
                break;
        }
        
        building.material = mat;
        
        // Add windows
        this.addWindows(building, height);
        
        this.buildings.push({
            mesh: building,
            type,
            position: { x, y, z },
            height,
            interactive: Math.random() > 0.7 // 30% of buildings are enterable
        });
        
        return building;
    }

    /**
     * Add windows to building
     */
    addWindows(building, height) {
        const floors = Math.floor(height / 3);
        
        for (let floor = 0; floor < floors; floor++) {
            // Add glowing windows (simple boxes)
            if (Math.random() > 0.3) { // 70% chance of lit windows
                const window1 = BABYLON.MeshBuilder.CreateBox(
                    'window',
                    { width: 0.5, height: 1, depth: 0.1 },
                    this.scene
                );
                
                window1.parent = building;
                window1.position.y = (floor - floors / 2) * 3;
                window1.position.x = 4.1;
                
                const windowMat = new BABYLON.StandardMaterial('windowMat', this.scene);
                windowMat.emissiveColor = new BABYLON.Color3(1, 0.9, 0.6);
                window1.material = windowMat;
            }
        }
    }

    /**
     * Create a skyscraper
     */
    createSkyscraper(x, y, z, height) {
        const skyscraper = BABYLON.MeshBuilder.CreateBox(
            'skyscraper',
            { width: 15, height, depth: 15 },
            this.scene
        );
        
        skyscraper.position = new BABYLON.Vector3(x, height / 2, z);
        
        const mat = new BABYLON.StandardMaterial('skyMat', this.scene);
        mat.diffuseColor = new BABYLON.Color3(0.1, 0.1, 0.2);
        mat.specularColor = new BABYLON.Color3(0.3, 0.3, 0.4);
        skyscraper.material = mat;
        
        // Add many windows
        this.addWindows(skyscraper, height);
        
        this.buildings.push({
            mesh: skyscraper,
            type: 'skyscraper',
            position: { x, y, z },
            height,
            interactive: true
        });
    }

    /**
     * Create roads
     */
    createRoads() {
        const roadMat = new BABYLON.StandardMaterial('roadMat', this.scene);
        roadMat.diffuseColor = new BABYLON.Color3(0.1, 0.1, 0.1);

        // Main roads (cross pattern)
        const roadH = BABYLON.MeshBuilder.CreateGround(
            'roadH',
            { width: 200, height: 10 },
            this.scene
        );
        roadH.position.y = 0.1;
        roadH.material = roadMat;

        const roadV = BABYLON.MeshBuilder.CreateGround(
            'roadV',
            { width: 10, height: 200 },
            this.scene
        );
        roadV.position.y = 0.1;
        roadV.material = roadMat;
    }

    /**
     * Create street lamps
     */
    createStreetLamps() {
        const positions = [
            [-90, 0], [-60, 0], [-30, 0], [0, 0], [30, 0], [60, 0], [90, 0],
            [0, -90], [0, -60], [0, -30], [0, 30], [0, 60], [0, 90]
        ];

        positions.forEach(([x, z]) => {
            this.createStreetLamp(x, 0, z);
        });
    }

    /**
     * Create single street lamp
     */
    createStreetLamp(x, y, z) {
        // Pole
        const pole = BABYLON.MeshBuilder.CreateCylinder(
            'lamp-pole',
            { diameter: 0.3, height: 8 },
            this.scene
        );
        pole.position = new BABYLON.Vector3(x, 4, z);

        // Light
        const light = new BABYLON.PointLight(
            'streetLight',
            new BABYLON.Vector3(x, 8, z),
            this.scene
        );
        light.diffuse = new BABYLON.Color3(1, 0.9, 0.7);
        light.intensity = 20;
        light.range = 20;

        this.streetLights.push(light);
    }

    /**
     * Create player character
     */
    createPlayer() {
        // Simple capsule for player
        this.player = BABYLON.MeshBuilder.CreateCapsule(
            'player',
            { radius: 0.5, height: 2 },
            this.scene
        );
        this.player.position = new BABYLON.Vector3(0, 1, 0);

        const playerMat = new BABYLON.StandardMaterial('playerMat', this.scene);
        playerMat.diffuseColor = new BABYLON.Color3(0, 1, 0.5);
        playerMat.emissiveColor = new BABYLON.Color3(0, 0.3, 0.15);
        this.player.material = playerMat;

        // Camera follows player
        this.camera.lockedTarget = this.player;
    }

    /**
     * Spawn NPCs
     */
    spawnNPCs() {
        const npcCount = 20;
        
        for (let i = 0; i < npcCount; i++) {
            const npc = this.createNPC(
                (Math.random() - 0.5) * 180,
                1,
                (Math.random() - 0.5) * 180
            );
            this.npcs.push(npc);
        }
    }

    /**
     * Create single NPC
     */
    createNPC(x, y, z) {
        const npc = BABYLON.MeshBuilder.CreateCapsule(
            'npc',
            { radius: 0.5, height: 2 },
            this.scene
        );
        npc.position = new BABYLON.Vector3(x, y, z);

        const mat = new BABYLON.StandardMaterial('npcMat', this.scene);
        mat.diffuseColor = new BABYLON.Color3(
            Math.random(),
            Math.random(),
            Math.random()
        );
        npc.material = mat;

        return {
            mesh: npc,
            type: Math.random() > 0.5 ? 'friendly' : 'hostile',
            speed: 0.5 + Math.random(),
            direction: Math.random() * Math.PI * 2
        };
    }

    /**
     * Add blockchain terminals
     */
    addBlockchainTerminals() {
        // Bitcoin terminal
        this.createTerminal(-20, 0, -20, 'Bitcoin', '#f7931a');
        
        // Ethereum terminal
        this.createTerminal(20, 0, -20, 'Ethereum', '#627eea');
        
        // Bitcoin Cash terminal
        this.createTerminal(0, 0, -20, 'Bitcoin Cash', '#8dc451');
    }

    /**
     * Create blockchain terminal
     */
    createTerminal(x, y, z, blockchain, color) {
        const terminal = BABYLON.MeshBuilder.CreateBox(
            `terminal_${blockchain}`,
            { width: 2, height: 3, depth: 0.5 },
            this.scene
        );
        terminal.position = new BABYLON.Vector3(x, 1.5, z);

        const mat = new BABYLON.StandardMaterial(`terminalMat_${blockchain}`, this.scene);
        mat.diffuseColor = BABYLON.Color3.FromHexString(color);
        mat.emissiveColor = BABYLON.Color3.FromHexString(color).scale(0.3);
        terminal.material = mat;

        this.terminals.push({
            mesh: terminal,
            blockchain,
            position: { x, y, z },
            interactive: true
        });
    }

    /**
     * Add mission markers
     */
    addMissionMarkers() {
        // Rescue mission marker
        this.createMissionMarker(30, 0, 30, 'rescue', '#ff0000');
        
        // Street fight marker
        this.createMissionMarker(-30, 0, 30, 'fight', '#ff9900');
        
        // Puzzle challenge marker
        this.createMissionMarker(30, 0, -30, 'puzzle', '#00ff00');
    }

    /**
     * Create mission marker
     */
    createMissionMarker(x, y, z, type, color) {
        const marker = BABYLON.MeshBuilder.CreateCylinder(
            `mission_${type}`,
            { diameter: 2, height: 5 },
            this.scene
        );
        marker.position = new BABYLON.Vector3(x, 2.5, z);

        const mat = new BABYLON.StandardMaterial(`missionMat_${type}`, this.scene);
        mat.diffuseColor = BABYLON.Color3.FromHexString(color);
        mat.emissiveColor = BABYLON.Color3.FromHexString(color).scale(0.5);
        mat.alpha = 0.7;
        marker.material = mat;

        // Rotating animation
        this.scene.registerBeforeRender(() => {
            marker.rotation.y += 0.02;
        });

        this.missionMarkers.push({
            mesh: marker,
            type,
            position: { x, y, z },
            active: true
        });
    }

    /**
     * Update loop
     */
    update() {
        // Update NPCs
        this.npcs.forEach(npc => {
            // Simple random walk
            npc.mesh.position.x += Math.cos(npc.direction) * npc.speed * 0.1;
            npc.mesh.position.z += Math.sin(npc.direction) * npc.speed * 0.1;

            // Change direction occasionally
            if (Math.random() < 0.01) {
                npc.direction = Math.random() * Math.PI * 2;
            }

            // Keep in bounds
            if (Math.abs(npc.mesh.position.x) > 95) npc.direction += Math.PI;
            if (Math.abs(npc.mesh.position.z) > 95) npc.direction += Math.PI;
        });

        // Update day/night cycle
        this.updateDayNight();
    }

    /**
     * Update day/night cycle
     */
    updateDayNight() {
        // Advance time slowly
        this.timeOfDay += 0.001;
        if (this.timeOfDay >= 24) this.timeOfDay = 0;

        // Adjust lighting based on time
        const sunIntensity = Math.max(0, Math.sin((this.timeOfDay / 24) * Math.PI * 2));
        this.sunLight.intensity = sunIntensity * 0.8;
        this.ambientLight.intensity = 0.3 + sunIntensity * 0.3;

        // Street lights brighter at night
        const nightIntensity = 1 - sunIntensity;
        this.streetLights.forEach(light => {
            light.intensity = nightIntensity * 20;
        });
    }

    /**
     * Move player
     */
    movePlayer(direction) {
        const speed = 0.5;
        switch (direction) {
            case 'forward':
                this.player.position.z += speed;
                break;
            case 'backward':
                this.player.position.z -= speed;
                break;
            case 'left':
                this.player.position.x -= speed;
                break;
            case 'right':
                this.player.position.x += speed;
                break;
        }
    }

    /**
     * Check for interactions (terminals, NPCs, missions)
     */
    checkInteractions() {
        const playerPos = this.player.position;

        // Check terminals
        this.terminals.forEach(terminal => {
            const distance = BABYLON.Vector3.Distance(
                playerPos,
                terminal.mesh.position
            );
            if (distance < 3) {
                return {
                    type: 'terminal',
                    data: terminal
                };
            }
        });

        // Check mission markers
        this.missionMarkers.forEach(marker => {
            if (!marker.active) return;
            
            const distance = BABYLON.Vector3.Distance(
                playerPos,
                marker.mesh.position
            );
            if (distance < 3) {
                return {
                    type: 'mission',
                    data: marker
                };
            }
        });

        // Check NPCs
        this.npcs.forEach(npc => {
            const distance = BABYLON.Vector3.Distance(
                playerPos,
                npc.mesh.position
            );
            if (distance < 2) {
                return {
                    type: 'npc',
                    data: npc
                };
            }
        });

        return null;
    }
}

module.exports = { BlockchainCity3D };
