from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base
class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    currency = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    
    incurred_at = Column(DateTime, nullable=False, default=datetime.now())
    
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="expenses")


