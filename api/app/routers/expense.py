
from fastapi import APIRouter, Depends, HTTPException
from ..services.expense import ExpenseService
from ..schemas.expense import  ExpenseRequest

router = APIRouter(prefix="/expenses", tags=["expenses"])

@router.get("/")
async def get_expenses(expense_service: ExpenseService = Depends()):
    expenses = expense_service.get_expenses()
    if expenses is None:
        raise HTTPException(status_code=404, detail="Expenses not found")
    
    return expenses

@router.get("/{expense_id}")
async def get_expense(expense_id: int, expense_service: ExpenseService = Depends()):
    expense = expense_service.get_expense_by_id(expense_id)
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    return expense

@router.post("/",)
async def create_expense(expense_form_data: ExpenseRequest, expense_service: ExpenseService = Depends()):
    if not expense_service.user_service.get_user_by_id(expense_form_data.paid_by_id):
        raise HTTPException(status_code=404, detail="User not found")
    
    if not expense_service.expense_category_service.get_expense_category_by_id(expense_form_data.expense_category_id):
        raise HTTPException(status_code=404, detail="Expense category not found")
    
    new_expense = expense_service.create_expense(expense_form_data)
    if not new_expense:
        raise HTTPException(status_code=404, detail="create Expense failed")

    return new_expense

@router.put("/{expense_id}")
async def update_expense(expense_id: int, expense_form_data: ExpenseRequest, expense_service: ExpenseService = Depends()):   
    if not expense_service.get_expense_by_id(expense_id):
        raise HTTPException(status_code=404, detail="Expense not found")
    
    if not expense_service.user_service.get_user_by_id(expense_form_data.paid_by_id):
        raise HTTPException(status_code=404, detail="User not found")
    
    if not expense_service.expense_category_service.get_expense_category_by_id(expense_form_data.expense_category_id):
        raise HTTPException(status_code=404, detail="Expense category not found")
    
    updated_expense = expense_service.update_expense(expense_id, expense_form_data)
    if not updated_expense:
        raise HTTPException(status_code=404, detail="update Expense failed")
    
    return updated_expense

@router.delete("/{expense_id}")
async def delete_expense(expense_id: int, expense_service: ExpenseService = Depends()):
    deleted_expense_id = expense_service.delete_expense(expense_id)
    if deleted_expense_id is None:
        raise HTTPException(status_code=404, detail="delete Expense failed")
    
    return {"message": "Expense deleted successfully"}
