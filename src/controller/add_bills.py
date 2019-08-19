""" Add bills to the database ; by weld
"""

import sqlite3 as s

def add_client(id, name, street, ZIP, city):
    db = s.connect("./model/database.db")
    cursor = db.cursor()
    cursor.execute('''
        INSERT INTO clients(id_client, name, street, ZIP, city)
        VALUES(?,?,?,?,?)
    ''', (id, name, street, ZIP, city))
    db.commit()
    db.close()

def add_bill(id_client, date, hourly_rate, quantity, paymeth):
    db = s.connect("./model/database.db")
    cursor = db.cursor()

    def generate_id_bill(date, id_client):
        """
            year + id_client + index of bills regarding the current client
        """
        year = date[-4:]
        month = date[3:5]
        cursor.execute('''
            SELECT COUNT(id_bill)
            FROM bills
            GROUP BY id_client
            HAVING id_client = ?
        ''', (str(id_client),))

        result = cursor.fetchall()

        i = str(id_client)
        if len(i) == 1:
            i = "00" + i
        elif len(i) == 2:
            i = "0"+ i

        if len(result) == 0:
            return year + "-" + month + "-"  + i + "001"
        else:

            r = result[0][0]
            r = str(r+1)
            if len(r) == 1:
                r = "00" + r
            elif len(r) == 2:
                r = "0"+r
            return year + "-" + month + "-" + i + r

    cursor.execute('''
        INSERT INTO bills(id_bill, id_client, date, hourly_rate, qty, pay)
        VALUES(?,?,?,?,?,?)
    ''', (generate_id_bill(date, id_client), id_client, date, hourly_rate, quantity, paymeth))
    db.commit()
    db.close()
 
def print_client(list):
    for x in list:
        print(x.get())


