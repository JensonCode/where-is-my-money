from pydantic import BaseModel, Field
from pydantic.config import ConfigDict
from datetime import datetime


class ExpenseCategoryBase(BaseModel):
    id: int
    name: str
    icon: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ExpenseCategoryRequest(BaseModel):
    name: str
    icon: str = Field(default="dummy-icon")


class ExpenseCategoryResponse(BaseModel):
    id: int
    name: str
    icon: str
    created_at: datetime
    updated_at: datetime
