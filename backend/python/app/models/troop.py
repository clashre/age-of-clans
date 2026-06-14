from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class Troop(Base):
    __tablename__ = "troops"
    
    id = Column(Integer, primary_key=True, index=True)
    village_id = Column(Integer, ForeignKey("villages.id"))
    troop_type = Column(String, index=True)  # barbarian, archer, giant, etc.
    quantity = Column(Integer, default=0)
    level = Column(Integer, default=1)
    is_training = Column(Boolean, default=False)
    training_start = Column(DateTime, nullable=True)
    training_end = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship
    village = relationship("Village", back_populates="troops")