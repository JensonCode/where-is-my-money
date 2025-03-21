from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship
from ..database.database import Base


class ExpenseCategory(Base):
    __tablename__ = "expense_categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    icon = Column(String, nullable=False, default="dummy-icon")
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    expenses = relationship("Expense", back_populates="expense_category")
