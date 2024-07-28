import sqlite3
import pandas as pd

def init_db():
    conn = sqlite3.connect('uptime_monitor.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS uptime (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            domain TEXT,
            status TEXT,
            checked_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    return conn, cursor

def log_status(domain, status):
    conn = sqlite3.connect('uptime_monitor.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO uptime (domain, status) VALUES (?, ?)', (domain, status))
    conn.commit()
    conn.close()

def fetch_data():
    conn = sqlite3.connect('uptime_monitor.db')
    df = pd.read_sql_query("SELECT * FROM uptime", conn)
    conn.close()
    return df
