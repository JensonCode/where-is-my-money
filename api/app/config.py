import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load environment variables
load_dotenv()

# Database configuration
DEV_MODE = os.getenv("DEV_MODE")

def get_engine():
    print(f"DEV_MODE: {DEV_MODE}")
    
    if DEV_MODE:
        print("Using SQLite engine")
        return create_engine("sqlite:///dev.db", echo=True)
    else:
        print("Using Supabase engine")
        return create_engine(os.getenv("SUPABASE_DB_CONNECTION_STRING"))

