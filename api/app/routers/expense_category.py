from fastapi import APIRouter, Depends, HTTPException
from ..services.expense_category import ExpenseCategoryService
from ..schemas.expense_category import ExpenseCategoryRequest, ExpenseCategoryResponse

router = APIRouter(prefix="/expense-categories", tags=["expense-categories"])

@router.get("/", response_model = list[ExpenseCategoryResponse])
async def get_expense_categories(expense_category_service: ExpenseCategoryService = Depends()):
   expense_categories = expense_category_service.get_expense_categories()
   return expense_categories

@router.get("/{expense_category_id}", response_model = ExpenseCategoryResponse)
async def get_expense_category(expense_category_id: int, expense_category_service: ExpenseCategoryService = Depends()):
    expense_category = expense_category_service.get_expense_category_by_id(expense_category_id)
    if not expense_category:
        raise HTTPException(status_code=404, detail="Expense category not found")
    
    return expense_category

@router.post("/", response_model = ExpenseCategoryResponse)
async def create_expense_category(expense_category_form_data: ExpenseCategoryRequest, expense_category_service: ExpenseCategoryService = Depends()):
    new_expense_category = expense_category_service.create_expense_category(expense_category_form_data)
    if not new_expense_category:
        raise HTTPException(status_code=404, detail="create Expense category failed")
    
    return new_expense_category

@router.put("/{expense_category_id}", response_model = ExpenseCategoryResponse)
async def update_expense_category(expense_category_id: int, expense_category_form_data: ExpenseCategoryRequest, expense_category_service: ExpenseCategoryService = Depends()):
    if not expense_category_service.get_expense_category_by_id(expense_category_id):
        raise HTTPException(status_code=404, detail="Expense category not found")
    
    updated_expense_category = expense_category_service.update_expense_category(expense_category_id, expense_category_form_data)
    if not updated_expense_category:
        raise HTTPException(status_code=404, detail="update Expense category failed")
    
    return updated_expense_category

@router.delete("/{expense_category_id}")
async def delete_expense_category(expense_category_id: int, expense_category_service: ExpenseCategoryService = Depends()):
    if not expense_category_service.get_expense_category_by_id(expense_category_id):
        raise HTTPException(status_code=404, detail="Expense category not found")
    
    deleted_expense_category_id = expense_category_service.delete_expense_category(expense_category_id)
    if not deleted_expense_category_id:
        raise HTTPException(status_code=404, detail="delete Expense category failed")
    
    return {"message": "Expense category deleted successfully"}
