import sqlite3

def init_db():
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS jobs (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      title TEXT,
                      salary TEXT,
                      location TEXT,
                      link TEXT,
                      source TEXT)''')
    conn.commit()
    conn.close()