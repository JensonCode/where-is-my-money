
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.expense import Expense
from datetime import datetime
router = APIRouter(prefix="/expenses", tags=["expenses"])

def fake_expenses():
    return [
        Expense(id=1, amount=100, currency="USD", description="Test Expense", incurred_at=datetime.now(), user_id=1),
        Expense(id=2, amount=200, currency="EUR", description="Test Expense 2", incurred_at=datetime.now(), user_id=1),
    ]


@router.get("/")
async def get_expenses(db: Session = Depends(get_db)):
    expenses = fake_expenses()
    return expenses

@router.get("/{expense_id}")
async def get_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = fake_expenses()[expense_id - 1]
    return expense

@router.post("/")
async def create_expense(db: Session = Depends(get_db)):
    return {"hello": "world"}

@router.put("/{expense_id}")
async def update_expense(expense_id: int, db: Session = Depends(get_db)):
    return {"hello": "world"}

@router.delete("/{expense_id}")
async def delete_expense(expense_id: int, db: Session = Depends(get_db)):
    return {"hello": "world"}
