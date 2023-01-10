import sqlite3
connection=sqlite3.connect("data.db")
cursor=connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS user_details(user_name VARCHAR(20), password VARCHAR(20))")
cursor.execute("INSERT INTO user_details VALUES('Saurabh', 'silky0305')")
connection.commit()