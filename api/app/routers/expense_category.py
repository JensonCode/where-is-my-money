from fastapi import APIRouter, Depends, HTTPException
from ..services.expense_category import ExpenseCategoryService
from ..schemas.expense_category import ExpenseCategoryRequest

router = APIRouter(prefix="/expense-categories", tags=["expense-categories"])

@router.get("/")
async def get_expense_categories(expense_category_service: ExpenseCategoryService = Depends()):
    return expense_category_service.get_expense_categories()

@router.get("/{expense_category_id}")
async def get_expense_category(expense_category_id: int, expense_category_service: ExpenseCategoryService = Depends()):
    return expense_category_service.get_expense_category_by_id(expense_category_id)
