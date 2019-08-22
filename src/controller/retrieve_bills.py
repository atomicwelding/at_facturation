""" Few utilies to deal with BILLS database  ; by weld
"""

import sqlite3 as s

def retrieve_all_bills():
    db = s.connect('./model/database.db')
    cursor = db.cursor()
    cursor.execute('''
        SELECT *
        FROM BILLS
        ORDER BY date DESC
    ''') ## Need to be fixed : date are ordered by the first number, not the complete date ( 19 / 01 > 10 / 02)
    r = cursor.fetchall()
    db.commit()
    db.close()
    return r

def replace_id_by_name(id_client):
    db = s.connect('./model/database.db')
    cursor = db.cursor()
    cursor.execute('''
        SELECT name
        FROM clients
        WHERE id_client = ?
    ''', (id_client,))
    r = cursor.fetchone()
    db.commit()
    db.close()
    return r[0]