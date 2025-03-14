
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from ..services.user import UserService
from ..internal.jwt import create_access_token
from ..schemas.user import LoginResponse, LoginFormData

router = APIRouter(prefix="/expenses", tags=["expenses"])

@router.get("/")
async def get_expenses():
    return {"hello": "world"}
