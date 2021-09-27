import sqlite3

conn = sqlite3.connect("Car.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS CAR")
# To create the table
cursor.execute("""CREATE TABLE CAR (CAR_NAME TEXT, NAME TEXT)""")
print("Table created")
conn.commit()

# To insert values
values = [('BMW', 'JOHN'), ('AUDI', 'BEN'), ('FORD', 'KEN'), ('SUZUKI', 'PETER'),
          ('HYUNDAI', 'JIM'), ('BENZ', 'SMITH'), ('TOYOTA', 'HARRY'), ('VOLKSWAGEN', 'GEORGE'), ('CHEVROLET', 'PAUL'),
          ('NISSAN', 'SAMMY')]

cursor.executemany("INSERT INTO CAR(CAR_NAME, NAME) VALUES (?,?)", values)

print("Values Inserted")
conn.commit()

# to display the table
cursor.execute("SELECT CAR_NAME, NAME FROM CAR")
value = cursor.fetchall()
for i in value:
    print(i)
conn.commit()
conn.close()
