import sqlite3 as sql

db = sql.connect("../model/db_testing")

cursor = db.cursor()
cursor.execute('''
    INSERT INTO users(name, phone, email, password) VALUES(?,?,?,?)''', ("a", "b", "c", "d"))
db.commit()

cursor.execute('''SELECT name, email, phone FROM users''')
db.commit()
user1 = cursor.fetchone() #retrieve the first row
print(user1[0]) #Print the first column retrieved(user's name)
all_rows = cursor.fetchall()
for row in all_rows:
    # row[0] returns the first column in the query (name), row[1] returns email column.
    print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))

db.close()