import sqlite3

conn = sqlite3.connect("Employee.db")
cursor = conn.cursor()

cursor.execute("Drop table if exists Departments")
# a) Create one more Table called Departments with two columns Department_id and Department_name.
cursor.execute("""Create table Departments (Department_id integer , Department_name Text , Foreign key(Department_id)
                References EMPLOYEE (DEPARTMENT_ID))""")
print("Table created")

# b) Insert 5 records into this table.
values = [(1, 'Finance'), (2, 'Developer'), (3, 'Human-Resources')]
cursor.executemany("INSERT INTO Departments VALUES (?,?)", values)
print("Values Inserted")

# c)Print the details of all the employees in a particular department (Department_id is input by the user)
d = 'y'
while d == 'y':
    d_id = int(input("Enter the ID:"))
    cursor.execute("SELECT Department_name from Departments where Department_id=:id", {"id": d_id})
    result = cursor.fetchone()
    print(f"\nEmployees Working in {result[0]} are:")
    cursor.execute("Select E.NAME,E.ID,E.SALARY,E.CITY,E.DEPARTMENT_id,D.Department_name from EMPLOYEE E,Departments D "
                   "where E.DEPARTMENT_id=:id AND D.Department_id=:id", {"id": d_id})
    record = cursor.fetchall()
    for row in record:
        print("\nName:", row[0])
        print("ID:", row[1])
        print("Salary:", row[2])
        print("City:", row[3])
        print("Department:", row[4])
        print("Department:", result[0])
    d = input("Do you want to Continue Y or N:")
conn.commit()
conn.close()