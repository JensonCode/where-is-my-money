from fastapi import Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.user import User
from ..internal.bcrypt import Bcrypt

DEFAULT_USERS = [
    {
        "username": "admin",
        "password": "admin",
        "nickname": "Admin"
    }
]

class UserService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
        
    def get_password_hash(self, password: str) -> str:
        return Bcrypt.hash_password(password)
        
    def init_default_users(self):
        print("Initializing default users")
        # Check if users already exist
        if self.db.query(User).count() > 0:
            print("Users were already initialized")
            return
	
        for user in DEFAULT_USERS:
            user = User(
                username=user["username"],
                password=self.get_password_hash(user["password"]),
                nickname=user["nickname"]
            )
            self.db.add(user)
        
        self.db.commit() 

    def authenticate_user(self, username: str, password: str) -> User:
        user = self.db.query(User).filter(User.username == username).first()
        if not user:
            return None
        if not Bcrypt.verify_password(password, user.password):
            return None
        return user


