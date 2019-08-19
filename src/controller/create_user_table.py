""" Quick script to create associated tables
"""
import sqlite3 as s

open("./model/database.db", "x").close()

db = s.connect("./model/database.db")

cursor = db.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients(
        id_client INTEGER,
        name TEXT,
        street TEXT,
        ZIP INTEGER, 
        city TEXT
    )''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS bills(
        id_bill TEXT,
        id_client INTEGER,
        date TEXT,
        hourly_rate INTEGER,
        qty INTEGER,
        pay TEXT
    )
''')

db.commit()
db.close()
