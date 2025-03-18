from fastapi import Depends
from sqlalchemy.orm import Session, joinedload
from ..database.database import get_db
from ..models.expense import Expense
from ..schemas.expense import ExpenseRequest
from ..services.user import UserService
from ..services.expense_category import ExpenseCategoryService

class ExpenseService:
    def __init__(self, db: Session = Depends(get_db), user_service: UserService = Depends(UserService), expense_category_service: ExpenseCategoryService = Depends(ExpenseCategoryService)):
        self.db = db
        self.user_service = user_service
        self.expense_category_service = expense_category_service
    # do pagination and filtering later
    # filter by user id and date range later
    # filter by category later
    def get_expenses(self) -> list[Expense]:
        return self.db.query(Expense).\
            options(joinedload(Expense.paid_by), joinedload(Expense.expense_category))\
            .all()
    
    def get_expense_by_id(self, expense_id: int) -> Expense | None:
        return self.db.query(Expense).\
            options(joinedload(Expense.paid_by), joinedload(Expense.expense_category))\
            .filter(Expense.id == expense_id)\
            .first()
    
    def create_expense(self, expense_form_data: ExpenseRequest) -> Expense | None:
        new_expense = Expense(**expense_form_data.model_dump())
        self.db.add(new_expense)
        self.db.commit()
        self.db.refresh(new_expense)
        return new_expense
    
    def update_expense(self, expense_id: int, expense_form_data: ExpenseRequest) -> Expense | None:
        updated_expense = expense_form_data.model_dump()
        self.db.query(Expense).filter(Expense.id == expense_id).update(updated_expense)
        self.db.commit()
        return self.get_expense_by_id(expense_id)
    
    def delete_expense(self, expense_id: int) -> int:
        self.db.query(Expense).filter(Expense.id == expense_id).delete()
        self.db.commit()
        return expense_id

