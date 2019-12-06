import sqlite3

class Employee:
    def __init__(self, id, name, age, address, salary):
        self.id = id
        self.name = name
        self.age = age
        self.address = address
        self.salary = salary
    def __str__(self):
        return f'{self.id} {self.name} {self.age} {self.address} '+\
               f'{self.salary}'
    def __repr__(self):
        return f'*{self.id} {self.name} {self.age} {self.address} '+\
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
        # create employee object with fields
        # add into result
        e = Employee(row[0], row[1], row[2], row[3], row[4])
        result.append(e)
    return result

def read_one_row(conn, id):
    # return employee instance with this id
    # id not found - return None
    rows = conn.execute(f'SELECT * FROM COMPANY WHERE ID={id}')  # cursor
    for row in rows:
        e = Employee(row[0], row[1], row[2], row[3], row[4])
        return e
    return None

def remove_row_by_id(conn, id):
    conn.execute(f'DELETE FROM COMPANY WHERE ID = {id}')  # cursor
    conn.commit()

def update_row(conn, e):
     conn.execute(f'UPDATE COMPANY SET NAME='+ "'" +f'{e.name}'+ "'" + f',AGE={e.age},'+\
                  f'ADDRESS=' + '"' + f'{e.address}' + '"' + f',SALARY={e.salary}'+\
                  f' WHERE ID={e.id}')
     conn.commit();
     print("record update...")

def main:
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
    e4 = read_one_row(conn, 1)
    print("employee id=1",e4)

    print('------------------ before update')
    employees = read_all_rows(conn)
    print(employees)
    print('------------------ after update')
    employees[0].name="Ginny"
    employees[0].age =28
    update_row(conn, employees[0])
    print(employees)
    print('------------------ before deletion')
    employees = read_all_rows(conn)
    print(employees)
    print(f'Now deleting {employees[0]}...')
    remove_row_by_id(conn, employees[0].id)
    print('------------------ after deletion')
    employees = read_all_rows(conn)
    print(employees)
    conn.close()

