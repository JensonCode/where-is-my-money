from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from .database.database import create_db_and_tables, get_db
from .database.migrate import check_migrations
from .initializers.default_data import DefaultData
from .routers import user, expense, expense_category
from .deps.jwt import get_current_user

app = FastAPI(
    title="Where Is My Money API",
    description="API for Where Is My Money, the app that tracks personal finances",
    version="1.0.0",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
create_db_and_tables()
check_migrations()

# Initialize default users
db = next(get_db())
default_data = DefaultData(db)
default_data.init_default_users()
default_data.init_default_expense_categories()

# Include routers
app.include_router(user.router)
app.include_router(expense_category.router, dependencies=[Depends(get_current_user)])
app.include_router(expense.router, dependencies=[Depends(get_current_user)])


@app.get("/")
async def root():
    return {"message": "Welcome to Where Is My Money API"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
