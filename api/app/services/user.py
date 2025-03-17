from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from ..database.database import get_db
from ..models.user import User
from ..deps.bcrypt import Bcrypt

class UserService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
        
    def get_user_by_id(self, user_id: int) -> User | None:
        return self.db.query(User).filter(User.id == user_id).first()
        
    def get_password_hash(self, password: str) -> str:
        return Bcrypt.hash_password(password)
        
    def authenticate_user(self, login_form_data: OAuth2PasswordRequestForm) -> User | None:
        user = self.db.query(User).filter(User.username == login_form_data.username).first()
        if not user:
            return None
        if not Bcrypt.verify_password(login_form_data.password, user.password):
            return None
        return user


