"""Battle Service - Combat system logic"""
import random
from datetime import datetime
from sqlalchemy.orm import Session
from app.models.all_models import Battle, Village, Troop, Building
from app.config.game_constants import BUILDINGS_CONFIG, TROOPS_CONFIG, DAMAGE_VARIANCE
from app.services.troop_service import TroopService

class BattleService:
    
    @staticmethod
    def calculate_troop_damage(db: Session, village_id: int, troops: dict) -> float:
        """Calculate total damage from attacking troops"""
        total_damage = 0
        
        for troop_type, quantity in troops.items():
            if troop_type not in TROOPS_CONFIG:
                continue
            
            troop_damage = TroopService.get_troop_damage(db, village_id, troop_type)
            troop_damage *= quantity
            
            # Add variance
            variance = random.uniform(1 - DAMAGE_VARIANCE, 1 + DAMAGE_VARIANCE)
            troop_damage *= variance
            
            total_damage += troop_damage
        
        return total_damage
    
    @staticmethod
    def calculate_defense_damage(db: Session, defender_village_id: int) -> tuple:
        """Calculate total defense from buildings"""
        buildings = db.query(Building).filter(
            Building.village_id == defender_village_id
        ).all()
        
        total_defense = 0
        tower_damage = 0
        
        for building in buildings:
            config = BUILDINGS_CONFIG.get(building.building_type, {})
            defense = config.get("defense", 0)
            total_defense += defense * building.level
            
            if building.building_type == "defense_tower":
                tower_config = BUILDINGS_CONFIG["defense_tower"]["levels"][building.level]
                tower_damage += tower_config.get("damage", 0)
        
        return total_defense, tower_damage
    
    @staticmethod
    def attack_village(db: Session, attacker_village_id: int, defender_village_id: int, troops: dict) -> dict:
        """Execute an attack between two villages"""
        attacker_village = db.query(Village).filter(Village.id == attacker_village_id).first()
        defender_village = db.query(Village).filter(Village.id == defender_village_id).first()
        
        if not attacker_village or not defender_village:
            return {"success": False, "message": "Village not found"}
        
        # Verify attacker has troops
        for troop_type, quantity in troops.items():
            troop = db.query(Troop).filter(
                Troop.village_id == attacker_village_id,
                Troop.troop_type == troop_type
            ).first()
            if not troop or troop.quantity < quantity:
                return {"success": False, "message": f"Not enough {troop_type}"}
        
        # Calculate damages
        attacker_damage = BattleService.calculate_troop_damage(db, attacker_village_id, troops)
        defender_defense, tower_damage = BattleService.calculate_defense_damage(db, defender_village_id)
        
        # Apply defense reduction
        if defender_defense > 0:
            damage_reduction = min(0.5, defender_defense / 100)
            attacker_damage *= (1 - damage_reduction)
        
        # Defender counter-attack
        defender_damage = tower_damage * random.uniform(0.8, 1.2)
        
        # Calculate gold/elixir stolen (max 20% of storage, capped by damage dealt)
        steal_percentage = min(0.2, attacker_damage / 1000)
        gold_stolen = min(
            defender_village.gold * steal_percentage,
            max(0, attacker_damage - defender_damage) / 100
        )
        elixir_stolen = min(
            defender_village.elixir * steal_percentage,
            max(0, attacker_damage - defender_damage) / 200
        )
        
        # Determine winner and stars
        attacker_won = attacker_damage > defender_damage
        stars = 0
        
        if attacker_won:
            stars = 1
            if attacker_damage > defender_damage * 2:
                stars = 2
            if attacker_damage > defender_damage * 3:
                stars = 3
            
            # Transfer resources
            attacker_village.gold += gold_stolen
            defender_village.gold -= gold_stolen
            attacker_village.elixir += elixir_stolen
            defender_village.elixir -= elixir_stolen
            
            # Ensure resources don't go negative
            defender_village.gold = max(0, defender_village.gold)
            defender_village.elixir = max(0, defender_village.elixir)
        
        # Remove troops from attacker
        for troop_type, quantity in troops.items():
            troop = db.query(Troop).filter(
                Troop.village_id == attacker_village_id,
                Troop.troop_type == troop_type
            ).first()
            if troop:
                troop.quantity -= quantity
        
        # Create battle record
        battle = Battle(
            attacker_village_id=attacker_village_id,
            defender_village_id=defender_village_id,
            is_pvp=True,
            attacker_damage=round(attacker_damage, 2),
            defender_damage=round(defender_damage, 2),
            gold_stolen=round(gold_stolen, 2),
            elixir_stolen=round(elixir_stolen, 2),
            attacker_won=attacker_won,
            stars=stars
        )
        
        db.add(battle)
        db.commit()
        
        return {
            "success": True,
            "attacker_damage": round(attacker_damage, 2),
            "defender_damage": round(defender_damage, 2),
            "attacker_won": attacker_won,
            "gold_stolen": round(gold_stolen, 2),
            "elixir_stolen": round(elixir_stolen, 2),
            "stars": stars,
            "battle_id": battle.id
        }
    
    @staticmethod
    def get_battle_history(db: Session, village_id: int, limit: int = 20) -> list:
        """Get battle history for a village"""
        battles = db.query(Battle).filter(
            Battle.attacker_village_id == village_id
        ).order_by(Battle.created_at.desc()).limit(limit).all()
        
        return [
            {
                "id": b.id,
                "defender_village_id": b.defender_village_id,
                "attacker_damage": b.attacker_damage,
                "defender_damage": b.defender_damage,
                "gold_stolen": b.gold_stolen,
                "elixir_stolen": b.elixir_stolen,
                "attacker_won": b.attacker_won,
                "stars": b.stars,
                "created_at": b.created_at.isoformat()
            }
            for b in battles
        ]
