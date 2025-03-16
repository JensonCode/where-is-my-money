from fastapi import Depends
from sqlalchemy.orm import Session
from ..database.database import get_db
from ..models.expense_category import ExpenseCategory
from ..schemas.expense_category import ExpenseCategoryRequest

class ExpenseCategoryService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_expense_categories(self) -> list[ExpenseCategory]:
        return self.db.query(ExpenseCategory).all()

    def get_expense_category_by_id(self, expense_category_id: int) -> ExpenseCategory:
        return self.db.query(ExpenseCategory).filter(ExpenseCategory.id == expense_category_id).first()

    def create_expense_category(self, expense_category_request: ExpenseCategoryRequest) -> ExpenseCategory:
        new_expense_category = ExpenseCategory(**expense_category_request.model_dump())
        self.db.add(new_expense_category)
        self.db.commit()
        self.db.refresh(new_expense_category)
        return new_expense_category

    def update_expense_category(self, expense_category_id: int, expense_category_request: ExpenseCategoryRequest) -> ExpenseCategory:
        expense_category = self.get_expense_category_by_id(expense_category_id)
        expense_category.update(expense_category_request.model_dump())

    def delete_expense_category(self, expense_category_id: int) -> ExpenseCategory:
        expense_category = self.get_expense_category_by_id(expense_category_id)
        self.db.delete(expense_category)
        self.db.commit()
        return expense_category
		