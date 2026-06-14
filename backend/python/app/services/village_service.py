"""Village Service - Main game logic for villages"""
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.models.all_models import Village, Player, Building, Troop, Research
from app.config.game_constants import (
    INITIAL_GOLD, INITIAL_ELIXIR, INITIAL_GOLD_STORAGE, INITIAL_ELIXIR_STORAGE,
    BUILDINGS_CONFIG, UNLOCKS
)

class VillageService:
    
    @staticmethod
    def create_village(db: Session, player_id: int, village_name: str) -> Village:
        """Create a new village for a player"""
        village = Village(
            player_id=player_id,
            name=village_name,
            level=1,
            gold=INITIAL_GOLD,
            elixir=INITIAL_ELIXIR,
            gold_storage_capacity=INITIAL_GOLD_STORAGE,
            elixir_storage_capacity=INITIAL_ELIXIR_STORAGE,
            gold_per_hour=100,
            elixir_per_hour=50
        )
        db.add(village)
        db.commit()
        
        # Create initial townhall
        townhall = Building(
            village_id=village.id,
            building_type="townhall",
            level=1,
            x=9,
            y=7,
            hp=200,
            max_hp=200
        )
        db.add(townhall)
        
        # Initialize troops
        for troop_type in ["barbarian", "archer", "giant", "goblin"]:
            troop = Troop(
                village_id=village.id,
                troop_type=troop_type,
                quantity=0,
                level=1
            )
            db.add(troop)
        
        # Initialize researches
        for research_type in ["troop_damage", "troop_hp", "production_gold", "production_elixir", "defense"]:
            research = Research(
                village_id=village.id,
                research_type=research_type,
                level=0
            )
            db.add(research)
        
        db.commit()
        return village
    
    @staticmethod
    def get_village(db: Session, village_id: int) -> Village:
        """Get village by ID"""
        return db.query(Village).filter(Village.id == village_id).first()
    
    @staticmethod
    def get_village_by_player(db: Session, player_id: int) -> Village:
        """Get village by player ID"""
        return db.query(Village).filter(Village.player_id == player_id).first()
    
    @staticmethod
    def update_resources(db: Session, village_id: int) -> Village:
        """Update village resources based on time elapsed"""
        village = VillageService.get_village(db, village_id)
        if not village:
            return None
        
        now = datetime.utcnow()
        last_update = village.last_resource_update
        hours_elapsed = (now - last_update).total_seconds() / 3600
        
        # Calculate production
        production_multiplier = 1.0
        prod_research = db.query(Research).filter(
            Research.village_id == village_id,
            Research.research_type == "production_gold"
        ).first()
        if prod_research and prod_research.level > 0:
            from app.config.game_constants import RESEARCH_CONFIG
            boost = RESEARCH_CONFIG["production_gold"]["levels"][prod_research.level].get("production_boost", 1.0)
            production_multiplier *= boost
        
        gold_production = village.gold_per_hour * hours_elapsed * production_multiplier
        elixir_production = village.elixir_per_hour * hours_elapsed * production_multiplier
        
        # Add resources (capped at storage)
        village.gold = min(village.gold + gold_production, village.gold_storage_capacity)
        village.elixir = min(village.elixir + elixir_production, village.elixir_storage_capacity)
        village.last_resource_update = now
        
        db.commit()
        return village
    
    @staticmethod
    def upgrade_townhall(db: Session, village_id: int) -> dict:
        """Upgrade townhall to next level"""
        village = VillageService.get_village(db, village_id)
        if not village:
            return {"success": False, "message": "Village not found"}
        
        current_level = village.level
        next_level = current_level + 1
        
        if next_level > 5:
            return {"success": False, "message": "Already at max level"}
        
        townhall_config = BUILDINGS_CONFIG["townhall"]["levels"][next_level]
        cost = townhall_config["cost"]
        
        if village.gold < cost["gold"] or village.elixir < cost["elixir"]:
            return {"success": False, "message": "Insufficient resources"}
        
        # Deduct resources
        village.gold -= cost["gold"]
        village.elixir -= cost["elixir"]
        village.level = next_level
        
        # Update production multiplier
        production_mult = townhall_config.get("production_multiplier", 1.0)
        village.gold_per_hour = 100 * production_mult
        village.elixir_per_hour = 50 * production_mult
        
        db.commit()
        return {"success": True, "message": "Townhall upgraded", "level": next_level}
    
    @staticmethod
    def get_village_data(db: Session, village_id: int) -> dict:
        """Get complete village data"""
        village = VillageService.update_resources(db, village_id)
        if not village:
            return None
        
        buildings = db.query(Building).filter(Building.village_id == village_id).all()
        troops = db.query(Troop).filter(Troop.village_id == village_id).all()
        researches = db.query(Research).filter(Research.village_id == village_id).all()
        
        return {
            "village": {
                "id": village.id,
                "name": village.name,
                "level": village.level,
                "gold": round(village.gold, 2),
                "elixir": round(village.elixir, 2),
                "experience": village.experience,
                "gold_per_hour": village.gold_per_hour,
                "elixir_per_hour": village.elixir_per_hour,
                "gold_storage_capacity": village.gold_storage_capacity,
                "elixir_storage_capacity": village.elixir_storage_capacity,
            },
            "buildings": [
                {
                    "id": b.id,
                    "type": b.building_type,
                    "level": b.level,
                    "x": b.x,
                    "y": b.y,
                    "hp": b.hp,
                    "max_hp": b.max_hp,
                    "is_constructing": b.is_constructing,
                    "construction_end": b.construction_end.isoformat() if b.construction_end else None
                }
                for b in buildings
            ],
            "troops": [
                {
                    "id": t.id,
                    "type": t.troop_type,
                    "quantity": t.quantity,
                    "level": t.level,
                    "is_training": t.is_training,
                    "training_end": t.training_end.isoformat() if t.training_end else None
                }
                for t in troops
            ],
            "researches": [
                {
                    "id": r.id,
                    "type": r.research_type,
                    "level": r.level,
                    "is_researching": r.is_researching,
                    "research_end": r.research_end.isoformat() if r.research_end else None
                }
                for r in researches
            ]
        }
