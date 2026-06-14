from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

class Building(Base):
    __tablename__ = "buildings"
    
    id = Column(Integer, primary_key=True, index=True)
    village_id = Column(Integer, ForeignKey("villages.id"))
    building_type = Column(String, index=True)  # townhall, barracks, laboratory, etc.
    level = Column(Integer, default=1)
    x = Column(Integer)  # Position in grid
    y = Column(Integer)
    is_constructing = Column(Boolean, default=False)
    construction_start = Column(DateTime, nullable=True)
    construction_end = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship
    village = relationship("Village", back_populates="buildings")