import sqlite3
from contextlib import contextmanager
from .config import Config

config = Config()

@contextmanager
def get_db():
    """Context manager that yields a DB connection and closes automatically."""
    conn = sqlite3.connect(config.db_path)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()
