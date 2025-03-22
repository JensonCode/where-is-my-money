from sqlalchemy.orm import Session
from fastapi import Depends
from ..database.database import get_db
from ..models.user import User
from ..models.expense_category import ExpenseCategory
from ..deps.bcrypt import Bcrypt


class DefaultData:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

        self.users = [{"username": "admin", "password": "admin", "nickname": "Admin"}]

        self.expense_categories = [
            {"name": "Groceries", "icon": "dummy-icon"},
            {"name": "Restaurants", "icon": "dummy-icon"},
            {"name": "Healthcare", "icon": "dummy-icon"},
            {"name": "Shopping", "icon": "dummy-icon"},
            {"name": "Transportation", "icon": "dummy-icon"},
            {"name": "Entertainment", "icon": "dummy-icon"},
            {"name": "Gifts", "icon": "dummy-icon"},
            {"name": "Luxury", "icon": "dummy-icon"},
            {"name": "Other", "icon": "dummy-icon"},
        ]

    def init_default_users(self):
        print("Initializing default users")
        if self.db.query(User).count() >= len(self.users):
            print("Users were already initialized")
            return

        for user in self.users:
            hashed_password = Bcrypt.hash_password(user["password"])
            user["password"] = hashed_password

            new_user = User(**user)
            self.db.add(new_user)
            self.db.commit()

    def init_default_expense_categories(self):
        print("Initializing default expense categories")
        if self.db.query(ExpenseCategory).count() >= len(self.expense_categories):
            print("Expense categories were already initialized")
            return

        for expense_category in self.expense_categories:
            new_expense_category = ExpenseCategory(**expense_category)
            self.db.add(new_expense_category)
            self.db.commit()
