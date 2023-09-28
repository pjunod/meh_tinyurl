from db import get_db


def get_url(short):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT url FROM urls WHERE short_url = ?"
    cursor.execute(statement, [short])
    return cursor.fetchall()


def create_url(url, short_url):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT into urls(url, short_url) VALUES(?, ?)"
    try:
        cursor.execute(statement, [url, short_url])
        db.commit()
    except:
        return False
    return True


def get_urllist():
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT * FROM urls"
    cursor.execute(statement)
    return cursor.fetchall()
