"""Game Constants and Configuration"""

# Building Configuration
BUILDINGS_CONFIG = {
    "townhall": {
        "name": "Ayuntamiento",
        "levels": {
            1: {"cost": {"gold": 0, "elixir": 0}, "time": 0, "hp": 200, "production_multiplier": 1.0},
            2: {"cost": {"gold": 100, "elixir": 0}, "time": 60, "hp": 250, "production_multiplier": 1.1},
            3: {"cost": {"gold": 200, "elixir": 0}, "time": 120, "hp": 300, "production_multiplier": 1.2},
            4: {"cost": {"gold": 400, "elixir": 0}, "time": 240, "hp": 350, "production_multiplier": 1.3},
            5: {"cost": {"gold": 800, "elixir": 0}, "time": 480, "hp": 400, "production_multiplier": 1.4},
        },
        "defense": 0,
        "type": "resource"
    },
    "barracks": {
        "name": "Barracones",
        "levels": {
            1: {"cost": {"gold": 100, "elixir": 0}, "time": 60, "hp": 150},
            2: {"cost": {"gold": 200, "elixir": 0}, "time": 120, "hp": 200},
            3: {"cost": {"gold": 400, "elixir": 0}, "time": 240, "hp": 250},
            4: {"cost": {"gold": 800, "elixir": 0}, "time": 480, "hp": 300},
            5: {"cost": {"gold": 1600, "elixir": 0}, "time": 960, "hp": 350},
        },
        "defense": 0,
        "type": "production"
    },
    "laboratory": {
        "name": "Laboratorio",
        "levels": {
            1: {"cost": {"gold": 200, "elixir": 100}, "time": 120, "hp": 200},
            2: {"cost": {"gold": 400, "elixir": 200}, "time": 240, "hp": 250},
            3: {"cost": {"gold": 800, "elixir": 400}, "time": 480, "hp": 300},
            4: {"cost": {"gold": 1600, "elixir": 800}, "time": 960, "hp": 350},
            5: {"cost": {"gold": 3200, "elixir": 1600}, "time": 1920, "hp": 400},
        },
        "defense": 0,
        "type": "production"
    },
    "storage_gold": {
        "name": "Almacén de Oro",
        "levels": {
            1: {"cost": {"gold": 50, "elixir": 0}, "time": 30, "hp": 100, "capacity": 5000},
            2: {"cost": {"gold": 100, "elixir": 0}, "time": 60, "hp": 150, "capacity": 7500},
            3: {"cost": {"gold": 200, "elixir": 0}, "time": 120, "hp": 200, "capacity": 10000},
            4: {"cost": {"gold": 400, "elixir": 0}, "time": 240, "hp": 250, "capacity": 15000},
            5: {"cost": {"gold": 800, "elixir": 0}, "time": 480, "hp": 300, "capacity": 20000},
        },
        "defense": 0,
        "type": "storage"
    },
    "storage_elixir": {
        "name": "Almacén de Elixir",
        "levels": {
            1: {"cost": {"gold": 100, "elixir": 50}, "time": 30, "hp": 100, "capacity": 2500},
            2: {"cost": {"gold": 200, "elixir": 100}, "time": 60, "hp": 150, "capacity": 3750},
            3: {"cost": {"gold": 400, "elixir": 200}, "time": 120, "hp": 200, "capacity": 5000},
            4: {"cost": {"gold": 800, "elixir": 400}, "time": 240, "hp": 250, "capacity": 7500},
            5: {"cost": {"gold": 1600, "elixir": 800}, "time": 480, "hp": 300, "capacity": 10000},
        },
        "defense": 0,
        "type": "storage"
    },
    "wall": {
        "name": "Muro",
        "levels": {
            1: {"cost": {"gold": 30, "elixir": 0}, "time": 15, "hp": 50, "defense": 5},
            2: {"cost": {"gold": 60, "elixir": 0}, "time": 30, "hp": 75, "defense": 7},
            3: {"cost": {"gold": 120, "elixir": 0}, "time": 60, "hp": 100, "defense": 10},
            4: {"cost": {"gold": 240, "elixir": 0}, "time": 120, "hp": 150, "defense": 15},
            5: {"cost": {"gold": 480, "elixir": 0}, "time": 240, "hp": 200, "defense": 20},
        },
        "defense": 5,
        "type": "defense"
    },
    "defense_tower": {
        "name": "Torre de Defensa",
        "levels": {
            1: {"cost": {"gold": 200, "elixir": 100}, "time": 90, "hp": 200, "defense": 20, "damage": 15},
            2: {"cost": {"gold": 400, "elixir": 200}, "time": 180, "hp": 300, "defense": 30, "damage": 22},
            3: {"cost": {"gold": 800, "elixir": 400}, "time": 360, "hp": 400, "defense": 40, "damage": 30},
            4: {"cost": {"gold": 1600, "elixir": 800}, "time": 720, "hp": 500, "defense": 50, "damage": 40},
            5: {"cost": {"gold": 3200, "elixir": 1600}, "time": 1440, "hp": 600, "defense": 60, "damage": 50},
        },
        "defense": 20,
        "type": "defense"
    },
    "gold_mine": {
        "name": "Mina de Oro",
        "levels": {
            1: {"cost": {"gold": 50, "elixir": 0}, "time": 30, "hp": 80, "production": 50},
            2: {"cost": {"gold": 100, "elixir": 0}, "time": 60, "hp": 120, "production": 75},
            3: {"cost": {"gold": 200, "elixir": 0}, "time": 120, "hp": 160, "production": 100},
            4: {"cost": {"gold": 400, "elixir": 0}, "time": 240, "hp": 200, "production": 150},
            5: {"cost": {"gold": 800, "elixir": 0}, "time": 480, "hp": 250, "production": 200},
        },
        "defense": 0,
        "type": "production"
    },
    "elixir_collector": {
        "name": "Colector de Elixir",
        "levels": {
            1: {"cost": {"gold": 100, "elixir": 50}, "time": 30, "hp": 80, "production": 25},
            2: {"cost": {"gold": 200, "elixir": 100}, "time": 60, "hp": 120, "production": 35},
            3: {"cost": {"gold": 400, "elixir": 200}, "time": 120, "hp": 160, "production": 50},
            4: {"cost": {"gold": 800, "elixir": 400}, "time": 240, "hp": 200, "production": 75},
            5: {"cost": {"gold": 1600, "elixir": 800}, "time": 480, "hp": 250, "production": 100},
        },
        "defense": 0,
        "type": "production"
    },
}

# Troop Configuration
TROOPS_CONFIG = {
    "barbarian": {
        "name": "Bárbaro",
        "levels": {
            1: {"cost": {"gold": 10, "elixir": 0}, "time": 10, "hp": 20, "damage": 8, "speed": 3},
            2: {"cost": {"gold": 20, "elixir": 0}, "time": 20, "hp": 30, "damage": 12, "speed": 3},
            3: {"cost": {"gold": 40, "elixir": 0}, "time": 40, "hp": 40, "damage": 16, "speed": 3},
            4: {"cost": {"gold": 80, "elixir": 0}, "time": 80, "hp": 50, "damage": 20, "speed": 3},
            5: {"cost": {"gold": 160, "elixir": 0}, "time": 160, "hp": 60, "damage": 25, "speed": 3},
        }
    },
    "archer": {
        "name": "Arquero",
        "levels": {
            1: {"cost": {"gold": 20, "elixir": 0}, "time": 15, "hp": 15, "damage": 6, "speed": 4},
            2: {"cost": {"gold": 40, "elixir": 0}, "time": 30, "hp": 22, "damage": 9, "speed": 4},
            3: {"cost": {"gold": 80, "elixir": 0}, "time": 60, "hp": 30, "damage": 12, "speed": 4},
            4: {"cost": {"gold": 160, "elixir": 0}, "time": 120, "hp": 40, "damage": 16, "speed": 4},
            5: {"cost": {"gold": 320, "elixir": 0}, "time": 240, "hp": 50, "damage": 20, "speed": 4},
        }
    },
    "giant": {
        "name": "Gigante",
        "levels": {
            1: {"cost": {"gold": 50, "elixir": 30}, "time": 30, "hp": 100, "damage": 20, "speed": 2},
            2: {"cost": {"gold": 100, "elixir": 60}, "time": 60, "hp": 150, "damage": 30, "speed": 2},
            3: {"cost": {"gold": 200, "elixir": 120}, "time": 120, "hp": 200, "damage": 40, "speed": 2},
            4: {"cost": {"gold": 400, "elixir": 240}, "time": 240, "hp": 250, "damage": 50, "speed": 2},
            5: {"cost": {"gold": 800, "elixir": 480}, "time": 480, "hp": 300, "damage": 60, "speed": 2},
        }
    },
    "goblin": {
        "name": "Trasgo",
        "levels": {
            1: {"cost": {"gold": 40, "elixir": 0}, "time": 20, "hp": 12, "damage": 6, "speed": 5},
            2: {"cost": {"gold": 80, "elixir": 0}, "time": 40, "hp": 18, "damage": 9, "speed": 5},
            3: {"cost": {"gold": 160, "elixir": 0}, "time": 80, "hp": 25, "damage": 12, "speed": 5},
            4: {"cost": {"gold": 320, "elixir": 0}, "time": 160, "hp": 35, "damage": 16, "speed": 5},
            5: {"cost": {"gold": 640, "elixir": 0}, "time": 320, "hp": 45, "damage": 20, "speed": 5},
        }
    },
}

# Research Configuration
RESEARCH_CONFIG = {
    "troop_damage": {
        "name": "Daño de Tropas",
        "levels": {
            1: {"cost": {"gold": 0, "elixir": 100}, "time": 60, "damage_boost": 1.1},
            2: {"cost": {"gold": 0, "elixir": 200}, "time": 120, "damage_boost": 1.2},
            3: {"cost": {"gold": 0, "elixir": 400}, "time": 240, "damage_boost": 1.3},
            4: {"cost": {"gold": 0, "elixir": 800}, "time": 480, "damage_boost": 1.4},
            5: {"cost": {"gold": 0, "elixir": 1600}, "time": 960, "damage_boost": 1.5},
        }
    },
    "troop_hp": {
        "name": "HP de Tropas",
        "levels": {
            1: {"cost": {"gold": 0, "elixir": 100}, "time": 60, "hp_boost": 1.1},
            2: {"cost": {"gold": 0, "elixir": 200}, "time": 120, "hp_boost": 1.2},
            3: {"cost": {"gold": 0, "elixir": 400}, "time": 240, "hp_boost": 1.3},
            4: {"cost": {"gold": 0, "elixir": 800}, "time": 480, "hp_boost": 1.4},
            5: {"cost": {"gold": 0, "elixir": 1600}, "time": 960, "hp_boost": 1.5},
        }
    },
    "production_gold": {
        "name": "Producción de Oro",
        "levels": {
            1: {"cost": {"gold": 100, "elixir": 0}, "time": 60, "production_boost": 1.1},
            2: {"cost": {"gold": 200, "elixir": 0}, "time": 120, "production_boost": 1.2},
            3: {"cost": {"gold": 400, "elixir": 0}, "time": 240, "production_boost": 1.3},
            4: {"cost": {"gold": 800, "elixir": 0}, "time": 480, "production_boost": 1.4},
            5: {"cost": {"gold": 1600, "elixir": 0}, "time": 960, "production_boost": 1.5},
        }
    },
    "production_elixir": {
        "name": "Producción de Elixir",
        "levels": {
            1: {"cost": {"gold": 100, "elixir": 100}, "time": 60, "production_boost": 1.1},
            2: {"cost": {"gold": 200, "elixir": 200}, "time": 120, "production_boost": 1.2},
            3: {"cost": {"gold": 400, "elixir": 400}, "time": 240, "production_boost": 1.3},
            4: {"cost": {"gold": 800, "elixir": 800}, "time": 480, "production_boost": 1.4},
            5: {"cost": {"gold": 1600, "elixir": 1600}, "time": 960, "production_boost": 1.5},
        }
    },
    "defense": {
        "name": "Defensa",
        "levels": {
            1: {"cost": {"gold": 0, "elixir": 150}, "time": 60, "defense_boost": 1.1},
            2: {"cost": {"gold": 0, "elixir": 300}, "time": 120, "defense_boost": 1.2},
            3: {"cost": {"gold": 0, "elixir": 600}, "time": 240, "defense_boost": 1.3},
            4: {"cost": {"gold": 0, "elixir": 1200}, "time": 480, "defense_boost": 1.4},
            5: {"cost": {"gold": 0, "elixir": 2400}, "time": 960, "defense_boost": 1.5},
        }
    },
}

# Unlocked buildings and troops per townhall level
UNLOCKS = {
    1: {
        "buildings": ["townhall", "barracks", "wall", "storage_gold", "gold_mine"],
        "troops": ["barbarian"],
        "researches": []
    },
    2: {
        "buildings": ["townhall", "barracks", "wall", "storage_gold", "storage_elixir", "gold_mine", "elixir_collector"],
        "troops": ["barbarian", "archer"],
        "researches": ["troop_damage", "production_gold"]
    },
    3: {
        "buildings": ["townhall", "barracks", "laboratory", "wall", "storage_gold", "storage_elixir", "gold_mine", "elixir_collector", "defense_tower"],
        "troops": ["barbarian", "archer", "giant"],
        "researches": ["troop_damage", "troop_hp", "production_gold", "production_elixir", "defense"]
    },
    4: {
        "buildings": ["townhall", "barracks", "laboratory", "wall", "storage_gold", "storage_elixir", "gold_mine", "elixir_collector", "defense_tower"],
        "troops": ["barbarian", "archer", "giant", "goblin"],
        "researches": ["troop_damage", "troop_hp", "production_gold", "production_elixir", "defense"]
    },
    5: {
        "buildings": ["townhall", "barracks", "laboratory", "wall", "storage_gold", "storage_elixir", "gold_mine", "elixir_collector", "defense_tower"],
        "troops": ["barbarian", "archer", "giant", "goblin"],
        "researches": ["troop_damage", "troop_hp", "production_gold", "production_elixir", "defense"]
    },
}

# Game Constants
INITIAL_GOLD = 1000
INITIAL_ELIXIR = 500
INITIAL_GOLD_STORAGE = 10000
INITIAL_ELIXIR_STORAGE = 5000

# Combat
DAMAGE_VARIANCE = 0.1  # 10% variance in damage
MIN_STARS = 0
MAX_STARS = 3

# Resource generation per hour
GOLD_PER_HOUR = 100
ELIXIR_PER_HOUR = 50
