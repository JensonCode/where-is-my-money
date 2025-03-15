
from fastapi import APIRouter, Depends, HTTPException
from ..services.expense import ExpenseService
from ..schemas.expense import ExpenseRequest
from datetime import datetime

router = APIRouter(prefix="/expenses", tags=["expenses"])

def fake_expenses():
    return [
        Expense(id=1, amount=100, currency="CAD", description="Test Expense", incurred_at=datetime.now(), paid_by=1),
        Expense(id=2, amount=200, currency="CAD", description="Test Expense 2", incurred_at=datetime.now(), paid_by=1, split=True, split_amount=100),
    ]


@router.get("/")
async def get_expenses(expense_service: ExpenseService = Depends()):
    expenses = expense_service.get_expenses()
    
    # do pagination and filtering later
    # filter by user id and date range later
    # filter by category later

    return expenses

@router.get("/{expense_id}")
async def get_expense(expense_id: int, expense_service: ExpenseService = Depends()):
    expense = expense_service.get_expense_by_id(expense_id)
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    return expense

@router.post("/")
async def create_expense(expense_form_data: ExpenseRequest, expense_service: ExpenseService = Depends()):
    new_expense = expense_service.create_expense(expense_form_data)
    if not new_expense:
        raise HTTPException(status_code=404, detail="create Expense failed")
    
    return new_expense

@router.put("/{expense_id}")
async def update_expense(expense_id: int, expense_form_data: ExpenseRequest, expense_service: ExpenseService = Depends()):
    expense = expense_service.get_expense_by_id(expense_id)
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    updated_expense = expense_service.update_expense(expense_id, expense_form_data)
    if not updated_expense:
        raise HTTPException(status_code=404, detail="update Expense failed")
    
    return updated_expense

@router.delete("/{expense_id}")
async def delete_expense(expense_id: int, expense_service: ExpenseService = Depends()):
    expense = expense_service.get_expense_by_id(expense_id)
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    deleted_expense = expense_service.delete_expense(expense_id)
    if not deleted_expense:
        raise HTTPException(status_code=404, detail="delete Expense failed")
    
    return deleted_expense
