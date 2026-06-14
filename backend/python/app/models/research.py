from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

class Research(Base):
    __tablename__ = "researches"
    
    id = Column(Integer, primary_key=True, index=True)
    village_id = Column(Integer, ForeignKey("villages.id"))
    research_type = Column(String, index=True)  # troop improvements, building improvements, etc.
    level = Column(Integer, default=1)
    is_researching = Column(Boolean, default=False)
    research_start = Column(DateTime, nullable=True)
    research_end = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship
    village = relationship("Village", back_populates="researches")