from pydantic import BaseModel, Field
from pydantic.config import ConfigDict
from datetime import datetime
from typing import Optional
from .user import UserBase
from .expense_category import ExpenseCategoryBase

class ExpenseBase(BaseModel):
    id: int
    
    amount: float
    currency: str
    description: str
    incurred_at: datetime
    
    split: bool
    split_amount: float | None = None
    
    expense_category_id: int
    paid_by_id: int
    
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
    
class ExpenseRequest(BaseModel):
    description: str
    currency: str = Field(default="CAD")
    amount: float
    incurred_at: datetime
    
    split: bool
    split_amount: Optional[float] = None
    
    settled: bool
    settled_at: Optional[datetime] = None
    
    paid_by_id: int = Field(gt=0)
    expense_category_id: int = Field(gt=0)
    
class ExpenseResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    description: str
    currency: str
    amount: float
    incurred_at: datetime
    
    split: bool
    split_amount: Optional[float] = None
    
    settled: bool
    settled_at: Optional[datetime] = None
    
    created_at: datetime
    updated_at: datetime
        
    paid_by: UserBase
    expense_category: ExpenseCategoryBase
