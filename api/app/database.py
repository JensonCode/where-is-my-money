from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from sqlalchemy.pool import NullPool
import os

# Load environment variables
load_dotenv()

def get_engine():
    # Database configuration
    DEV_MODE = os.getenv("DEV_MODE")
    print(f"DEV_MODE: {DEV_MODE}")

    connection_url = None
    
    if DEV_MODE:    
        connection_url = "sqlite:///dev.db"
        print("Using SQLite engine")
        return create_engine(connection_url, echo=True)
    else:
        connection_url = os.getenv("SUPABASE_DB_CONNECTION_STRING")
        print("Using Supabase engine")
        return create_engine(connection_url, client_encoding='utf8', poolclass=NullPool)

engine = get_engine()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_db_and_tables():
    """Initialize database and create all tables"""
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print(f"Failed to create database tables: {e}")
        raise