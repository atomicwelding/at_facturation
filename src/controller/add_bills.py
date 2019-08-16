""" Add bills to the database ; by weld
"""

import sqlite3 as s

def add_user(id, name, street, ZIP, city):
    db = s.connect("./model/database.db")
    cursor = db.cursor()
    cursor.execute('''
        INSERT INTO users(id_user, name, street, ZIP, city)
        VALUES(?,?,?,?,?)
    ''', (id, name, street, ZIP, city))
    db.commit()
    db.close()
 


