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
    def __repr__(self):
        return f'*{self.id} {self.name} {self.age} {self.address}'+\
               f'{self.salary}'

def create_table(conn):
    try:
        conn.execute("CREATE TABLE COMPANY("+\
                    "ID INTEGER PRIMARY KEY AUTOINCREMENT,"+\
                    "NAME TEXT UNIQUE NOT NULL,"+\
                    "AGE INT NOT NULL,"+\
                    "ADDRESS CHAR(50),"+\
                    "SALARY REAL"");")
        print("table created...")
    except:
        print("table already exist")

def insert_into_table(conn, e):
    try:
        conn.execute("INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY)"+\
                    "VALUES ( '{}', {}, '{}', {} );"\
                     .format(e.name, e.age, e.address, e.salary));
        conn.commit()
        print("record inserted...")
    except:
        print("cannot insert record")

def read_all_rows(conn):
    rows = conn.execute("SELECT * FROM COMPANY") # cursor
    result = []
    for row in rows:
        print(row)
        # create employee object with fields
        # add into result
        e = Employee(row[0], row[1], row[2], row[3], row[4])
        result.append(e)
    return result

def read_one_row(conn, id):
    # return employee instance with this id
    # id not found - return None
    row = conn.execute("SELECT * FROM COMPANY WHERE ID=...")  # cursor

def remove_row_by_id(conn, id):
    conn.execute("DELETE FROM COMPANY WHERE ID = ...")  # cursor
    conn.commit()

# create conn to existing db
# if db does not exist -- it will be created
conn = sqlite3.connect('cars.db')
create_table(conn)
e1 = Employee(None, 'Allen', 25, 'Texas', 15000.00 )
e2 = Employee(None, 'Teddy', 23, 'Norway', 20000.0)
e3 = Employee(None, 'Mark', 25, 'Rich-Mond', 65000.0)
insert_into_table(conn, e1)
insert_into_table(conn, e2)
insert_into_table(conn, e3)
employees = read_all_rows(conn)
print(employees)
print("employee 1 name =",employees[0].name)
conn.close()
