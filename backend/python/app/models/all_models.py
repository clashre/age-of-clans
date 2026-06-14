from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.db import Base

class Player(Base):
    """Player model"""
    __tablename__ = "players"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    level = Column(Integer, default=1)
    experience = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    village = relationship("Village", back_populates="player", uselist=False)

class Village(Base):
    """Village model"""
    __tablename__ = "villages"
    
    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey("players.id"), unique=True)
    name = Column(String, index=True)
    level = Column(Integer, default=1)
    gold = Column(Float, default=1000)
    elixir = Column(Float, default=500)
    experience = Column(Integer, default=0)
    gold_per_hour = Column(Float, default=100)
    elixir_per_hour = Column(Float, default=50)
    gold_storage_capacity = Column(Float, default=10000)
    elixir_storage_capacity = Column(Float, default=10000)
    last_resource_update = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    player = relationship("Player", back_populates="village")
    buildings = relationship("Building", back_populates="village", cascade="all, delete-orphan")
    troops = relationship("Troop", back_populates="village", cascade="all, delete-orphan")
    researches = relationship("Research", back_populates="village", cascade="all, delete-orphan")
    battles = relationship("Battle", back_populates="attacker_village", foreign_keys="Battle.attacker_village_id")

class Building(Base):
    """Building model"""
    __tablename__ = "buildings"
    
    id = Column(Integer, primary_key=True, index=True)
    village_id = Column(Integer, ForeignKey("villages.id"))
    building_type = Column(String, index=True)  # townhall, barracks, laboratory, etc.
    level = Column(Integer, default=1)
    x = Column(Integer)
    y = Column(Integer)
    is_constructing = Column(Boolean, default=False)
    construction_start = Column(DateTime, nullable=True)
    construction_end = Column(DateTime, nullable=True)
    hp = Column(Integer, default=100)
    max_hp = Column(Integer, default=100)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship
    village = relationship("Village", back_populates="buildings")

class Troop(Base):
    """Troop model"""
    __tablename__ = "troops"
    
    id = Column(Integer, primary_key=True, index=True)
    village_id = Column(Integer, ForeignKey("villages.id"))
    troop_type = Column(String, index=True)  # barbarian, archer, giant, goblin
    quantity = Column(Integer, default=0)
    quantity_training = Column(Integer, default=0)
    level = Column(Integer, default=1)
    is_training = Column(Boolean, default=False)
    training_start = Column(DateTime, nullable=True)
    training_end = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship
    village = relationship("Village", back_populates="troops")

class Research(Base):
    """Research model"""
    __tablename__ = "researches"
    
    id = Column(Integer, primary_key=True, index=True)
    village_id = Column(Integer, ForeignKey("villages.id"))
    research_type = Column(String, index=True)  # troop_damage, building_hp, production, etc.
    level = Column(Integer, default=0)
    is_researching = Column(Boolean, default=False)
    research_start = Column(DateTime, nullable=True)
    research_end = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship
    village = relationship("Village", back_populates="researches")

class Battle(Base):
    """Battle record model"""
    __tablename__ = "battles"
    
    id = Column(Integer, primary_key=True, index=True)
    attacker_village_id = Column(Integer, ForeignKey("villages.id"))
    defender_village_id = Column(Integer, ForeignKey("villages.id"), nullable=True)  # None for PvE
    is_pvp = Column(Boolean, default=False)
    attacker_damage = Column(Float, default=0)
    defender_damage = Column(Float, default=0)
    gold_stolen = Column(Float, default=0)
    elixir_stolen = Column(Float, default=0)
    attacker_won = Column(Boolean, default=False)
    stars = Column(Integer, default=0)  # 0-3 stars
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    attacker_village = relationship("Village", back_populates="battles", foreign_keys=[attacker_village_id])
