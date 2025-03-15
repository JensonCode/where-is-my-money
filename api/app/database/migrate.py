from alembic.config import Config
from alembic import command
import os


def check_migrations():
    alembic_cfg = Config(os.path.join(os.path.dirname(__file__), "../../alembic.ini"))
    command.check(alembic_cfg)
    print("Migrations checked")
