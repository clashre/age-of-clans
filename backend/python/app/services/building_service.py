"""Building Service - Logic for buildings"""
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.models.all_models import Building, Village
from app.config.game_constants import BUILDINGS_CONFIG

class BuildingService:
    
    @staticmethod
    def start_construction(db: Session, village_id: int, building_type: str, x: int, y: int) -> dict:
        """Start building a new construction"""
        village = db.query(Village).filter(Village.id == village_id).first()
        if not village:
            return {"success": False, "message": "Village not found"}
        
        if building_type not in BUILDINGS_CONFIG:
            return {"success": False, "message": "Invalid building type"}
        
        building_config = BUILDINGS_CONFIG[building_type]["levels"][1]
        cost = building_config["cost"]
        
        # Check resources
        if village.gold < cost["gold"] or village.elixir < cost["elixir"]:
            return {"success": False, "message": "Insufficient resources"}
        
        # Check if position is occupied
        existing = db.query(Building).filter(
            Building.village_id == village_id,
            Building.x == x,
            Building.y == y
        ).first()
        if existing:
            return {"success": False, "message": "Position already occupied"}
        
        # Deduct resources
        village.gold -= cost["gold"]
        village.elixir -= cost["elixir"]
        
        # Create building
        construction_time = building_config["time"]
        building = Building(
            village_id=village_id,
            building_type=building_type,
            level=1,
            x=x,
            y=y,
            is_constructing=True,
            construction_start=datetime.utcnow(),
            construction_end=datetime.utcnow() + timedelta(seconds=construction_time),
            hp=building_config["hp"],
            max_hp=building_config["hp"]
        )
        
        db.add(building)
        db.commit()
        
        return {
            "success": True,
            "message": "Construction started",
            "building": {
                "id": building.id,
                "type": building.building_type,
                "level": building.level,
                "construction_time": construction_time,
                "construction_end": building.construction_end.isoformat()
            }
        }
    
    @staticmethod
    def upgrade_building(db: Session, building_id: int) -> dict:
        """Upgrade a building to next level"""
        building = db.query(Building).filter(Building.id == building_id).first()
        if not building:
            return {"success": False, "message": "Building not found"}
        
        if building.is_constructing:
            return {"success": False, "message": "Building is already under construction"}
        
        village = db.query(Village).filter(Village.id == building.village_id).first()
        
        next_level = building.level + 1
        if building.building_type not in BUILDINGS_CONFIG or next_level > 5:
            return {"success": False, "message": "Cannot upgrade further"}
        
        upgrade_config = BUILDINGS_CONFIG[building.building_type]["levels"][next_level]
        cost = upgrade_config["cost"]
        
        if village.gold < cost["gold"] or village.elixir < cost["elixir"]:
            return {"success": False, "message": "Insufficient resources"}
        
        # Deduct resources
        village.gold -= cost["gold"]
        village.elixir -= cost["elixir"]
        
        # Start upgrade
        construction_time = upgrade_config["time"]
        building.is_constructing = True
        building.construction_start = datetime.utcnow()
        building.construction_end = datetime.utcnow() + timedelta(seconds=construction_time)
        building.level = next_level
        building.max_hp = upgrade_config["hp"]
        building.hp = upgrade_config["hp"]
        
        db.commit()
        
        return {
            "success": True,
            "message": "Upgrade started",
            "building": {
                "id": building.id,
                "level": building.level,
                "construction_time": construction_time,
                "construction_end": building.construction_end.isoformat()
            }
        }
    
    @staticmethod
    def complete_construction(db: Session, building_id: int) -> dict:
        """Complete a building construction"""
        building = db.query(Building).filter(Building.id == building_id).first()
        if not building:
            return {"success": False, "message": "Building not found"}
        
        if not building.is_constructing:
            return {"success": False, "message": "Building is not under construction"}
        
        building.is_constructing = False
        building.construction_start = None
        building.construction_end = None
        
        db.commit()
        
        return {"success": True, "message": "Construction completed"}
    
    @staticmethod
    def get_buildings(db: Session, village_id: int) -> list:
        """Get all buildings in a village"""
        buildings = db.query(Building).filter(Building.village_id == village_id).all()
        return [
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
        ]
    
    @staticmethod
    def check_and_complete_constructions(db: Session, village_id: int) -> list:
        """Check and complete any finished constructions"""
        now = datetime.utcnow()
        buildings = db.query(Building).filter(
            Building.village_id == village_id,
            Building.is_constructing == True,
            Building.construction_end <= now
        ).all()
        
        completed = []
        for building in buildings:
            building.is_constructing = False
            building.construction_start = None
            building.construction_end = None
            completed.append(building.building_type)
        
        if completed:
            db.commit()
        
        return completed
