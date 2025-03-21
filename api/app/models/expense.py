from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database.database import Base


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    currency = Column(String, nullable=False, default="CAD")
    amount = Column(Float, nullable=False)
    incurred_at = Column(DateTime, nullable=False, default=datetime.now())

    split = Column(Boolean, default=False)
    split_amount = Column(Float, nullable=True)

    settled = Column(Boolean, default=False)
    settled_at = Column(DateTime, nullable=True, default=None)

    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    paid_by_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    paid_by = relationship("User", back_populates="expenses")

    expense_category_id = Column(
        Integer, ForeignKey("expense_categories.id"), nullable=False
    )
    expense_category = relationship("ExpenseCategory", back_populates="expenses")
