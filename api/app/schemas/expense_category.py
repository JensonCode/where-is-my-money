from pydantic import BaseModel

class ExpenseCategory(BaseModel):
    id: int
    name: str

class ExpenseCategoryRequest(BaseModel):
    name: str


