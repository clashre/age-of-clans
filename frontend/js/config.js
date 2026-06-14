// Game Configuration
const GAME_CONFIG = {
  // API
  API_BASE_URL: 'http://localhost:3000/api/python',
  
  // Game settings
  GRID_SIZE: 40,
  MAP_WIDTH: 20,
  MAP_HEIGHT: 15,
  
  // Resources
  RESOURCES: {
    gold: { name: 'Oro', icon: '⚜️', color: 0xffd700 },
    elixir: { name: 'Elixir', icon: '💜', color: 0xb535f6 }
  },
  
  // Building types
  BUILDINGS: {
    townhall: { name: 'Ayuntamiento', cost: { gold: 100, elixir: 0 }, time: 30, hp: 200 },
    barracks: { name: 'Barracones', cost: { gold: 50, elixir: 0 }, time: 20, hp: 100 },
    laboratory: { name: 'Laboratorio', cost: { gold: 75, elixir: 50 }, time: 40, hp: 150 },
    storage: { name: 'Almacén', cost: { gold: 40, elixir: 0 }, time: 15, hp: 80 },
    wall: { name: 'Muro', cost: { gold: 30, elixir: 0 }, time: 10, hp: 50 }
  },
  
  // Troop types
  TROOPS: {
    barbarian: { name: 'Bárbaro', cost: { gold: 10, elixir: 0 }, time: 10, damage: 8, hp: 20 },
    archer: { name: 'Arquero', cost: { gold: 20, elixir: 0 }, time: 15, damage: 6, hp: 15 },
    giant: { name: 'Gigante', cost: { gold: 50, elixir: 30 }, time: 30, damage: 20, hp: 100 },
    goblin: { name: 'Trasgo', cost: { gold: 40, elixir: 0 }, time: 20, damage: 6, hp: 12 }
  },
  
  // Combat
  COMBAT: {
    playerDamageMultiplier: 1.0,
    enemyDamageMultiplier: 0.8,
    defenseEffectiveness: 1.2
  }
};