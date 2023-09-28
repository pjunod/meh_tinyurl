import sqlite3

DB_NAME = "app.db"


def get_db():
    conn = sqlite3.connect(DB_NAME)
    return conn


def create_tables():
    bootstrap = """CREATE TABLE IF NOT EXISTS urls (
    id INTEGER PRIMARY KEY,
    url TEXT NOT NULL,
    short_url TEXT NOT NULL UNIQUE
    )"""
    db = get_db()
    cursor = db.cursor()
    cursor.execute(bootstrap)
