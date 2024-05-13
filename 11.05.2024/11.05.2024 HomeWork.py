import sqlite3

with sqlite3.connect('11.05.2024.db') as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS worker(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    surname TEXT,
    name TEXT,
    patronymic TEXT,
    age INTEGER,
    [group] INTEGER,
    FOREIGN KEY ([group]) REFERENCES post(id) ON DELETE CASCADE 
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS post(
    id INTEGER PRIMARY KEY,
    post_name TEXT,
    experience Text
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS production(
    workshop_id INTEGER,
    profession_id INTEGER,
    FOREIGN KEY (workshop_id) REFERENCES workshop(id),
    FOREIGN KEY (workshop_id) REFERENCES post(id)
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS workshop(
    id PRIMARY KEY,
    division_id TEXT,
    area TEXT,
    flor TEXT,
    direction TEXT
    )
    """)