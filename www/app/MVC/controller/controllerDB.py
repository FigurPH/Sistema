import eel
import sys
import sqlite3
import json

@eel.expose
def sql():
    db = sqlite3.connect('www/app/db/database.db')
    cursor = db.cursor()
    cursor.execute("select * from produtos")
    print(cursor.fetchall())
