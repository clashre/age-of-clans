"""Research Service - Logic for research and upgrades"""
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.models.all_models import Research, Village
from app.config.game_constants import RESEARCH_CONFIG

class ResearchService:
    
    @staticmethod
    def start_research(db: Session, village_id: int, research_type: str) -> dict:
        """Start a research in the laboratory"""
        village = db.query(Village).filter(Village.id == village_id).first()
        if not village:
            return {"success": False, "message": "Village not found"}
        
        if research_type not in RESEARCH_CONFIG:
            return {"success": False, "message": "Invalid research type"}
        
        research = db.query(Research).filter(
            Research.village_id == village_id,
            Research.research_type == research_type
        ).first()
        
        if not research:
            return {"success": False, "message": "Research not available"}
        
        if research.is_researching:
            return {"success": False, "message": "Research already in progress"}
        
        next_level = research.level + 1
        if next_level > 5:
            return {"success": False, "message": "Research already maxed"}
        
        research_config = RESEARCH_CONFIG[research_type]["levels"][next_level]
        cost = research_config["cost"]
        
        # Check resources
        if village.gold < cost["gold"] or village.elixir < cost["elixir"]:
            return {"success": False, "message": "Insufficient resources"}
        
        # Deduct resources
        village.gold -= cost["gold"]
        village.elixir -= cost["elixir"]
        
        # Start research
        research_time = research_config["time"]
        research.is_researching = True
        research.research_start = datetime.utcnow()
        research.research_end = datetime.utcnow() + timedelta(seconds=research_time)
        
        db.commit()
        
        return {
            "success": True,
            "message": "Research started",
            "research": {
                "type": research.research_type,
                "next_level": next_level,
                "research_time": research_time,
                "research_end": research.research_end.isoformat()
            }
        }
    
    @staticmethod
    def complete_research(db: Session, village_id: int, research_type: str) -> dict:
        """Complete a research"""
        research = db.query(Research).filter(
            Research.village_id == village_id,
            Research.research_type == research_type
        ).first()
        
        if not research:
            return {"success": False, "message": "Research not found"}
        
        if not research.is_researching:
            return {"success": False, "message": "Research is not in progress"}
        
        research.level += 1
        research.is_researching = False
        research.research_start = None
        research.research_end = None
        
        db.commit()
        
        return {"success": True, "message": "Research completed", "level": research.level}
    
    @staticmethod
    def get_researches(db: Session, village_id: int) -> list:
        """Get all researches in a village"""
        researches = db.query(Research).filter(Research.village_id == village_id).all()
        return [
            {
                "id": r.id,
                "type": r.research_type,
                "level": r.level,
                "is_researching": r.is_researching,
                "research_end": r.research_end.isoformat() if r.research_end else None
            }
            for r in researches
        ]
    
    @staticmethod
    def check_and_complete_researches(db: Session, village_id: int) -> list:
        """Check and complete any finished researches"""
        now = datetime.utcnow()
        researches = db.query(Research).filter(
            Research.village_id == village_id,
            Research.is_researching == True,
            Research.research_end <= now
        ).all()
        
        completed = []
        for research in researches:
            research.level += 1
            research.is_researching = False
            research.research_start = None
            research.research_end = None
            completed.append(research.research_type)
        
        if completed:
            db.commit()
        
        return completed
