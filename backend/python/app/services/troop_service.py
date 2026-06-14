"""Troop Service - Logic for troop training and management"""
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.models.all_models import Troop, Village, Research
from app.config.game_constants import TROOPS_CONFIG, RESEARCH_CONFIG

class TroopService:
    
    @staticmethod
    def start_training(db: Session, village_id: int, troop_type: str, quantity: int) -> dict:
        """Start training troops"""
        village = db.query(Village).filter(Village.id == village_id).first()
        if not village:
            return {"success": False, "message": "Village not found"}
        
        if troop_type not in TROOPS_CONFIG:
            return {"success": False, "message": "Invalid troop type"}
        
        if quantity <= 0:
            return {"success": False, "message": "Quantity must be positive"}
        
        troop_config = TROOPS_CONFIG[troop_type]["levels"][1]
        total_cost = {
            "gold": troop_config["cost"]["gold"] * quantity,
            "elixir": troop_config["cost"]["elixir"] * quantity
        }
        
        # Check resources
        if village.gold < total_cost["gold"] or village.elixir < total_cost["elixir"]:
            return {"success": False, "message": "Insufficient resources"}
        
        # Deduct resources
        village.gold -= total_cost["gold"]
        village.elixir -= total_cost["elixir"]
        
        # Get or create troop
        troop = db.query(Troop).filter(
            Troop.village_id == village_id,
            Troop.troop_type == troop_type
        ).first()
        
        if not troop:
            troop = Troop(
                village_id=village_id,
                troop_type=troop_type,
                quantity=0,
                level=1
            )
            db.add(troop)
        
        # Calculate training time
        training_time = troop_config["time"] * quantity
        
        troop.quantity_training = quantity
        troop.is_training = True
        troop.training_start = datetime.utcnow()
        troop.training_end = datetime.utcnow() + timedelta(seconds=training_time)
        
        db.commit()
        
        return {
            "success": True,
            "message": "Training started",
            "troop": {
                "type": troop.troop_type,
                "quantity": quantity,
                "training_time": training_time,
                "training_end": troop.training_end.isoformat()
            }
        }
    
    @staticmethod
    def complete_training(db: Session, village_id: int, troop_type: str) -> dict:
        """Complete troop training"""
        troop = db.query(Troop).filter(
            Troop.village_id == village_id,
            Troop.troop_type == troop_type
        ).first()
        
        if not troop:
            return {"success": False, "message": "Troop not found"}
        
        if not troop.is_training:
            return {"success": False, "message": "Troop is not training"}
        
        troop.quantity += troop.quantity_training
        troop.quantity_training = 0
        troop.is_training = False
        troop.training_start = None
        troop.training_end = None
        
        db.commit()
        
        return {"success": True, "message": "Training completed", "quantity": troop.quantity}
    
    @staticmethod
    def get_troop_damage(db: Session, village_id: int, troop_type: str) -> float:
        """Get total damage for a troop type with research bonuses"""
        troop_config = TROOPS_CONFIG[troop_type]["levels"][1]
        base_damage = troop_config["damage"]
        
        # Apply research bonus
        research = db.query(Research).filter(
            Research.village_id == village_id,
            Research.research_type == "troop_damage"
        ).first()
        
        if research and research.level > 0:
            boost = RESEARCH_CONFIG["troop_damage"]["levels"][research.level].get("damage_boost", 1.0)
            base_damage *= boost
        
        return base_damage
    
    @staticmethod
    def get_troop_hp(db: Session, village_id: int, troop_type: str) -> float:
        """Get total HP for a troop type with research bonuses"""
        troop_config = TROOPS_CONFIG[troop_type]["levels"][1]
        base_hp = troop_config["hp"]
        
        # Apply research bonus
        research = db.query(Research).filter(
            Research.village_id == village_id,
            Research.research_type == "troop_hp"
        ).first()
        
        if research and research.level > 0:
            boost = RESEARCH_CONFIG["troop_hp"]["levels"][research.level].get("hp_boost", 1.0)
            base_hp *= boost
        
        return base_hp
    
    @staticmethod
    def get_troops(db: Session, village_id: int) -> list:
        """Get all troops in a village"""
        troops = db.query(Troop).filter(Troop.village_id == village_id).all()
        return [
            {
                "id": t.id,
                "type": t.troop_type,
                "quantity": t.quantity,
                "level": t.level,
                "is_training": t.is_training,
                "quantity_training": t.quantity_training,
                "training_end": t.training_end.isoformat() if t.training_end else None
            }
            for t in troops
        ]
    
    @staticmethod
    def check_and_complete_trainings(db: Session, village_id: int) -> list:
        """Check and complete any finished trainings"""
        now = datetime.utcnow()
        troops = db.query(Troop).filter(
            Troop.village_id == village_id,
            Troop.is_training == True,
            Troop.training_end <= now
        ).all()
        
        completed = []
        for troop in troops:
            troop.quantity += troop.quantity_training
            troop.quantity_training = 0
            troop.is_training = False
            troop.training_start = None
            troop.training_end = None
            completed.append(troop.troop_type)
        
        if completed:
            db.commit()
        
        return completed
