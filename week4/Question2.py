import sqlite3

conn = sqlite3.connect('Hospital.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS DOCTOR")
cursor.execute("DROP TABLE IF EXISTS HOSPITAL")

# to create the table
cursor.execute("""CREATE TABLE HOSPITAL (Hospital_id INTEGER NOT NULL PRIMARY KEY,Hospital_Name TEXT,
                 Bed_Count INTEGER)""")
cursor.execute("""CREATE TABLE DOCTOR (Doctor_id INTEGER NOT NULL PRIMARY KEY, Doctor_Name TEXT,
                Hospital_id INTEGER,Joining_Date DATE, Speciality TEXT, Salary INTEGER, Experience TEXT,
                FOREIGN KEY(Hospital_id) REFERENCES HOSPITAL(Hospital_id))""")
print("Table Created")
conn.commit()

# to insert values

hos_values = [(1, 'Mayo Clinic', 200), (2, 'Cleveland Clinic', 400), (3, 'Johns Hopkins', 1000),
              (4, 'UCLA Medical Centre', 1500)]
cursor.executemany("INSERT  INTO HOSPITAL (Hospital_id,Hospital_Name,Bed_Count) VALUES (?,?,?)", hos_values)

doc_values = [(101, 'David', 1, '2005-20-10', 'Pediatric', 40000, 'NULL'),
              (102, 'Michael', 1, '2018-07-23', 'Oncologist', 20000, 'NULL'),
              (103, 'Susan', 2, '2016-05-19', 'Garnacologist', 25000, 'NULL'),
              (104, 'Robert', 2, '2017-12-28', 'Pediatric ', 28000, 'NULL'),
              (105, 'Linda', 3, '2004-06-04', 'Garnacologist', 42000, 'NULL'),
              (106, 'William', 3, '2012-09-11', 'Dermatologist', 30000, 'NULL'),
              (107, 'Richard', 4, '2014-08-21', 'Garnacologist', 32000, 'NULL'),
              (108, 'Karen', 4, '2011-10-17', 'Radiologist', 30000, 'NULL')]

cursor.executemany(
    "INSERT INTO DOCTOR(Doctor_Id, Doctor_Name, Hospital_Id, Joining_Date, Speciality, Salary,Experience)"
    "VALUES (?,?,?,?,?,?,?)", doc_values)
print("Value Inserted")
conn.commit()


def get_doctors(special, sal):
    cursor.execute("SELECT Doctor_Name  FROM DOCTOR WHERE Speciality =:special AND Salary >= :sal",
                   {"special": special, "sal": sal})
    print(f"{speciality} doctors with {salary} above are:\n")
    results = cursor.fetchall()
    for i in results:
        print(i[0])


def display_doctors(hospital_id):
    cursor.execute("SELECT Doctor_Name from DOCTOR where Hospital_id=:id ", {"id": hospital_id})
    results = cursor.fetchall()
    print(f"Doctors working in given {hospital_id} are:\n")
    for i in results:
        print(i[0])


def display_hospital_name(name):
    cursor.execute("SELECT * FROM DOCTOR WHERE Doctor_Name =:name", {"name": name})
    results = cursor.fetchone()
    a = results[2]
    cursor.execute("SELECT Hospital_Name FROM HOSPITAL WHERE Hospital_id=:id", {"id": a})
    print(f"{name} is working at Hospital:")
    value = cursor.fetchall()
    for i in value:
        print(i[0])


set_var = True
while set_var:
    print("\n1.List of doctors\n2.Hospital Name of doctor\n3.Doctors based on speciality and salary\n4.Exit")
    ch = int(input("Enter your choice:"))
    if ch == 1:
        h_id = int(input("Enter the hospital_id (1-4):"))
        display_doctors(h_id)
    elif ch == 2:
        doc_name = input("Enter the doctor name:")
        display_hospital_name(doc_name.capitalize())
    elif ch == 3:
        speciality = input("Enter the speciality:")
        salary = int(input("Enter the Salary:"))
        get_doctors(speciality.capitalize(), salary)
    elif ch == 4:
        set_var = False
