import sqlite3
conn = sqlite3.connect('example.db')
print("opened database successfully")
conn.execute("INSERT INTO EMPLOYEES VALUES (11,'FAITH KARIMI',23,34544.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (12,'MOSES KARANJA',23,15000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (13,'COLLINS KAMAU',23,34500.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (14,'JOHN KAMUNYA',23,34635.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (15,'FANUEL KAMAU',23,20854.00)")

conn.commit()
print("Record inserted successfully")
conn.close()
