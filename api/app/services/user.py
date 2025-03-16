from fastapi import Depends
from sqlalchemy.orm import Session
from ..database.database import get_db
from ..models.user import User
from ..internal.bcrypt import Bcrypt
from fastapi.security import OAuth2PasswordRequestForm

class UserService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
        
    def get_password_hash(self, password: str) -> str:
        return Bcrypt.hash_password(password)
        
    def authenticate_user(self, login_form_data: OAuth2PasswordRequestForm) -> User:
        user = self.db.query(User).filter(User.username == login_form_data.username).first()
        if not user:
            return None
        if not Bcrypt.verify_password(login_form_data.password, user.password):
            return None
        return user


