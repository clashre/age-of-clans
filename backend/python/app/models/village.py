from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class Village(Base):
    __tablename__ = "villages"
    
    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey("players.id"))
    name = Column(String, index=True)
    level = Column(Integer, default=1)
    gold = Column(Float, default=0)
    elixir = Column(Float, default=0)
    experience = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    player = relationship("Player", back_populates="village")
    buildings = relationship("Building", back_populates="village")
    troops = relationship("Troop", back_populates="village")
    researches = relationship("Research", back_populates="village")