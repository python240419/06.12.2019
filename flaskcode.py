# first - import flask from Settings
from flask import Flask
from flask import render_template, request, redirect,url_for
from EmployeeDAO import *
import sqlite3

app = Flask(__name__)
user_name = ""

@app.route('/')
def home_page():
    name = 'itay'
    return f'<html><h1><b>Welcome to flask! {name}</b></h1></html>'

@app.route('/employees')
def show_employees():
    conn = sqlite3.connect('cars.db')
    emp = read_all_rows(conn)
    conn.close()
    return render_template('employees.html', list_emp = emp)


app.run()
