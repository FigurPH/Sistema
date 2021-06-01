import sys
import sqlite3
import json

db = sqlite3.connect('www/app/db/database.db')

cursor = db.cursor()


#cursor.execute('create table IF NOT EXISTS teste(nome text, idade integer)')
#cursor.execute("insert into teste values('Pedro', 31)")
#db.commit()
cursor.execute("select * from produtos")
print(cursor.fetchall()) 


##aqui a baixo é com with. que abre e fecha automaticamente
""" def db_to_json(json_str = True):
    with sqlite3.connect('www/app/db/database.db') as db:
        cursor = db.cursor()
        cursor.execute("select * from teste")
        data = cursor.fetchall()
        return json.dumps(data)

print(json.dumps(db_to_json())) """
