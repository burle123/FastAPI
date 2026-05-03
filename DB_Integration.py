#SQLITE

import sqlite3
from fastapi import FastAPI

app = FastAPI()

# Create a connection to the SQLite database

conn = sqlite3.connect('mydb.db', check_same_thread=False)

# Create a cursor object to execute SQL commands

cursor = conn.cursor()

# Create a table

cursor.execute("""
CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    completed TEXT NOT NULL
)
""")

# Insert a todo into the table

cursor.execute("""
INSERT INTO todos (name, completed) VALUES ('Buy groceries', 'false')
""")

# Commit the changes and close the connection

conn.commit()
conn.close()

@app.get("/")
def home():
    return{
        "message":"Database Integrated Successfully!"
    }