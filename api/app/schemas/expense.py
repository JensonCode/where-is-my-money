from pydantic import BaseModel
from datetime import datetime

class Expense(BaseModel):
    id: int
    amount: float
    currency: str
    description: str
    incurred_at: datetime
    paid_by: int
    split: bool
    split_amount: float
    split_with: int
    created_at: datetime
    updated_at: datetime
    
class ExpenseRequest(BaseModel):
    description: str
    currency: str
    amount: float
    split: bool
    split_amount: float
    incurred_at: datetime
    paid_by: int
    
