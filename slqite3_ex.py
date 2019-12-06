import sqlite3

class Employee:
    def __init__(self, id, name, age, address, salary):
        self.id = id
        self.name = name
        self.age = age
        self.address = address
        self.salary = salary
    def __str__(self):
        return f'{self.id} {self.name} {self.age} {self.address}'+\
               f'{self.salary}'

def create_table(conn):
    try:
        conn.execute("CREATE TABLE COMPANY("+\
                    "ID INT PRIMARY KEY NOT NULL,"+\
                    "NAME TEXT NOT NULL,"+\
                    "AGE INT NOT NULL,"+\
                    "ADDRESS CHAR(50),"+\
                    "SALARY REAL"");")
        print("table created...")
    except:
        print("table already exist")

def insert_into_table(conn, e):
    try:
        conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)"+\
                    "VALUES ({}, '{}', {}, '{}', {} );"\
                     .format(e.id, e.name, e.age, e.address, e.salary));
        conn.commit()
        print("record inserted...")
    except:
        print("cannot insert record")


# create conn to existing db
# if db does not exist -- it will be created
conn = sqlite3.connect('cars.db')
create_table(conn)
e1 = Employee(1, 'Allen', 25, 'Texas', 15000.00 )
insert_into_table(conn, e1)
conn.close()
