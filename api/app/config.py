import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load environment variables
load_dotenv()

# Database configuration
DEV_MODE = os.getenv("DEV_MODE")

def get_db_url():
    if DEV_MODE:
        return "sqlite:///dev.db"
    else:
        return os.getenv("SUPABASE_DB_CONNECTION_STRING")

def get_engine():
    print(f"DEV_MODE: {DEV_MODE}")
    
    db_url = get_db_url()
    print(f"DB_URL: {db_url}")
    
    if DEV_MODE:
        print("Using SQLite engine")
        return create_engine(db_url, echo=True)
    else:
        print("Using Supabase engine")
        return create_engine(db_url)
