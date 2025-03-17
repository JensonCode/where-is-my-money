from pydantic import BaseModel
from pydantic.config import ConfigDict
from datetime import datetime

class UserBase(BaseModel):
    id: int
    username: str
    nickname: str
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

class LoginFormData(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str