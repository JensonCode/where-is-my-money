from alembic.config import Config
from alembic import command
from alembic.util.exc import CommandError
import os


def check_migrations():
    try:
        alembic_cfg = Config(os.path.join(os.path.dirname(__file__), "../../alembic.ini"))
        
        try:
            # Try to check if migrations are up to date
            command.check(alembic_cfg)
            print("Migrations are up to date")
        except CommandError as e:
            if "Target database is not up to date" in str(e):
                print("Database is not up to date. Applying migrations...")
                # Apply migrations automatically
                command.upgrade(alembic_cfg, "head")
                print("Migrations applied successfully")
            else:
                # For other errors, just print and continue
                print(f"Migration check warning: {e}")
    except Exception as e:
        print(f"Migration check failed: {e}")
        print("Continuing without migrations")
