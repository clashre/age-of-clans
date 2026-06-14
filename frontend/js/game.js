// Phaser Game Configuration
const phaserConfig = {
    type: Phaser.AUTO,
    width: window.innerWidth,
    height: window.innerHeight,
    canvas: document.getElementById('game-container'),
    physics: {
        default: 'arcade',
        arcade: {
            gravity: { y: 0 },
            debug: false
        }
    },
    scene: {
        preload: preload,
        create: create,
        update: update
    },
    scale: {
        mode: Phaser.Scale.RESIZE,
        autoCenter: Phaser.Scale.CENTER_BOTH
    }
};

const game = new Phaser.Game(phaserConfig);
let gameState = {
    village: null,
    buildings: [],
    troops: [],
    selectedBuilding: null,
    resources: { gold: 1000, elixir: 500 }
};

function preload() {
    // Load assets here
    console.log('Preloading assets...');
}

function create() {
    const scene = this;
    
    // Create background
    scene.add.rectangle(0, 0, window.innerWidth, window.innerHeight, 0x2d5016)
        .setOrigin(0, 0);
    
    // Create grid
    const gridGraphics = scene.make.graphics({ x: 0, y: 0, add: false });
    gridGraphics.strokeStyle(1, 0x4a7c28, 0.3);
    
    for (let x = 0; x < GAME_CONFIG.MAP_WIDTH; x++) {
        gridGraphics.strokeLineShape([
            new Phaser.Geom.Line(x * GAME_CONFIG.GRID_SIZE, 0, x * GAME_CONFIG.GRID_SIZE, GAME_CONFIG.MAP_HEIGHT * GAME_CONFIG.GRID_SIZE)
        ]);
    }
    
    for (let y = 0; y < GAME_CONFIG.MAP_HEIGHT; y++) {
        gridGraphics.strokeLineShape([
            new Phaser.Geom.Line(0, y * GAME_CONFIG.GRID_SIZE, GAME_CONFIG.MAP_WIDTH * GAME_CONFIG.GRID_SIZE, y * GAME_CONFIG.GRID_SIZE)
        ]);
    }
    
    gridGraphics.generateTexture('grid', GAME_CONFIG.MAP_WIDTH * GAME_CONFIG.GRID_SIZE, GAME_CONFIG.MAP_HEIGHT * GAME_CONFIG.GRID_SIZE);
    scene.add.image(0, 0, 'grid').setOrigin(0, 0);
    gridGraphics.destroy();
    
    // Create sample buildings
    createSampleVillage(scene);
    
    // Input
    scene.input.on('pointerdown', (pointer) => {
        handleMapClick(scene, pointer);
    });
    
    // Update UI
    updateResourcesUI();
}

function update() {
    // Game loop - generate resources, update timers, etc.
}

function createSampleVillage(scene) {
    // Townhall at center
    createBuilding(scene, 9, 7, 'townhall', 1);
    
    // Barracks
    createBuilding(scene, 7, 5, 'barracks', 1);
    createBuilding(scene, 11, 5, 'barracks', 1);
    
    // Storage
    createBuilding(scene, 5, 10, 'storage', 1);
    createBuilding(scene, 13, 10, 'storage', 1);
    
    // Walls
    for (let i = 0; i < 5; i++) {
        createBuilding(scene, 3, 3 + i, 'wall', 1);
        createBuilding(scene, 15, 3 + i, 'wall', 1);
    }
}

function createBuilding(scene, x, y, type, level) {
    const building = scene.add.rectangle(
        x * GAME_CONFIG.GRID_SIZE + GAME_CONFIG.GRID_SIZE / 2,
        y * GAME_CONFIG.GRID_SIZE + GAME_CONFIG.GRID_SIZE / 2,
        GAME_CONFIG.GRID_SIZE - 4,
        GAME_CONFIG.GRID_SIZE - 4,
        0x8b4513
    );
    
    building.setInteractive();
    building.on('pointerover', () => {
        building.setStrokeStyle(2, 0xffd700);
    });
    building.on('pointerout', () => {
        building.setStrokeStyle();
    });
    
    building.buildingType = type;
    building.level = level;
    building.gridX = x;
    building.gridY = y;
    
    gameState.buildings.push(building);
}

function handleMapClick(scene, pointer) {
    console.log('Map clicked at:', pointer.x, pointer.y);
}

function updateResourcesUI() {
    document.getElementById('gold').textContent = gameState.resources.gold;
    document.getElementById('elixir').textContent = gameState.resources.elixir;
}