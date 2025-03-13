from pydantic import BaseModel

class LoginFormData(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str