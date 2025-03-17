from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from ..database.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    nickname = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    expenses = relationship("Expense", back_populates="paid_by")
