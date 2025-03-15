from fastapi import Depends
from sqlalchemy.orm import Session
from ..database.database import get_db
from ..models.expense import Expense
from ..schemas.expense import ExpenseRequest

class ExpenseService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
        
    # do pagination and filtering later
    # filter by user id and date range later
    # filter by category later
    def get_expenses(self) -> list[Expense]:
        return self.db.query(Expense).all()
    
    def get_expense_by_id(self, expense_id: int) -> Expense:
        return self.db.query(Expense).filter(Expense.id == expense_id).first()
    
    def create_expense(self, expense_form_data: ExpenseRequest) -> Expense:
        new_expense = Expense(**expense_form_data.model_dump())
        self.db.add(new_expense)
        self.db.commit()
        self.db.refresh(new_expense)
        return new_expense
    
    def update_expense(self, expense_id: int, expense_form_data: ExpenseRequest) -> Expense:
        expense = self.get_expense_by_id(expense_id)
        expense.update(expense_form_data.model_dump())
        self.db.commit()
        self.db.refresh(expense)
        return expense
    
    def delete_expense(self, expense_id: int) -> Expense:
        expense = self.get_expense_by_id(expense_id)
        self.db.delete(expense)
        self.db.commit()
        return expense

