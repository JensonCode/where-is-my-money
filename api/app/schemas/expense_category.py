from pydantic import BaseModel
from pydantic.config import ConfigDict
from datetime import datetime


class ExpenseCategoryBase(BaseModel):
    id: int
    name: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ExpenseCategoryRequest(BaseModel):
    name: str


class ExpenseCategoryResponse(BaseModel):
    id: int
    name: str
    created_at: datetime
    updated_at: datetime
