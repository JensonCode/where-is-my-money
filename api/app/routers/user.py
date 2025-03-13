
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from ..services.user import UserService
from ..internal.jwt import create_access_token
from ..schemas.user import LoginResponse, UserLogin

router = APIRouter(prefix="/users", tags=["users"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")

@router.post("/login", response_model=LoginResponse)
async def login(
    login_form_data: UserLogin = Depends(),
    user_service: UserService = Depends()
):
    user = user_service.authenticate_user(login_form_data)
    
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
        
    access_token = create_access_token(data={"sub": user.username, "nickname": user.nickname, "id": user.id})
    
    return {"access_token": access_token, "token_type": "bearer"}





