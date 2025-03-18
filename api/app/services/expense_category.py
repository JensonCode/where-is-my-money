from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from ..database.database import get_db
from ..models.expense_category import ExpenseCategory
from ..schemas.expense_category import ExpenseCategoryRequest


class ExpenseCategoryService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_expense_categories(self) -> list[ExpenseCategory]:
        return self.db.query(ExpenseCategory).all()

    def get_expense_category_by_id(
        self, expense_category_id: int
    ) -> ExpenseCategory | None:
        return (
            self.db.query(ExpenseCategory)
            .filter(ExpenseCategory.id == expense_category_id)
            .first()
        )

    def create_expense_category(
        self, expense_category_form_data: ExpenseCategoryRequest
    ) -> ExpenseCategory | None:
        new_expense_category = ExpenseCategory(
            **expense_category_form_data.model_dump()
        )
        self.db.add(new_expense_category)
        self.db.commit()
        self.db.refresh(new_expense_category)
        return new_expense_category

    def update_expense_category(
        self,
        expense_category_id: int,
        expense_category_form_data: ExpenseCategoryRequest,
    ) -> ExpenseCategory:
        updated_expense_category = expense_category_form_data.model_dump()
        self.db.query(ExpenseCategory).filter(
            ExpenseCategory.id == expense_category_id
        ).update(updated_expense_category)
        self.db.commit()
        self.db.refresh(updated_expense_category)
        return updated_expense_category

    def delete_expense_category(self, expense_category_id: int) -> int:
        self.db.query(ExpenseCategory).filter(
            ExpenseCategory.id == expense_category_id
        ).delete()
        self.db.commit()
        return expense_category_id
