""" Quick script to create associated tables
"""
import sqlite3 as s

db = s.connect("../model/database.db")

cursor = db.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS utilisateurs(
        id_client INTEGER,
        nom TEXT,
        voie TEXT,
        cp INTEGER, 
        ville TEXT
    )''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS factures(
        id_facture INTEGER,
        id_client INTEGER,
        date TEXT,
        taux_horaire INTEGER,
        qte INTEGER,
        reglement TEXT
    )
''')

db.commit()
db.close()
