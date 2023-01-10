from flask import  Flask, render_template, request
import sqlite3
app=Flask(__name__)
@app.route('/',method=['GET','POST'])
def index():
    if request.method=='POST':
        connection=sqlite3.connect('data.db')
        cursor=connection.cursor()
        name=request.form['name']
        password=request.form['password']
        print(name,password)
        query="SELECT name.password FROM users where name '"+name+"' and password='"+password+"'"
        cursor.execute(query)
        result=cursor.fetchall()
        if len(result)==0:
            print("Sorry Incorrect credential. Try again")
        else:
            return render_template("login.html"),render_template("main.html")
    return render_template("index.html")