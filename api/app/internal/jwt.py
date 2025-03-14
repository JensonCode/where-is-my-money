import os
from jose import JWTError, jwt
from datetime import datetime, timedelta
from dotenv import load_dotenv
from fastapi import HTTPException,  Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from ..models.user import User
from ..database import get_db

load_dotenv()

SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 3000000

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")

def create_access_token( data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str) -> str | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        	return None


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    not_authenticated_exception = HTTPException(status_code=401, detail="Not authenticated")
    
    sub = verify_access_token(token)
    if not sub:
        raise not_authenticated_exception
    
    user = db.query(User).filter(User.username == sub).first()
    if not user:
        raise not_authenticated_exception
    
    return user
