import eel
import sys
import sqlite3
import json


@eel.expose
def sql():
    db = sqlite3.connect('www/app/db/database.db')
    cursor = db.cursor()
    cursor.execute("select * from produtos")
    cursor.close()
    print(cursor.fetchall())


class Run():

    def __init__(self, sql):
        self.db = sqlite3.connect('www/app/db/database.db')
        self.cursor = self.db.cursor()
        self.sql = sql

    def runQuery(self):
        sql=str(self.sql)
        self.cursor.execute(sql)
        self.db.commit()
        self.cursor.close()

    def testRun(self):
        print(self.sql)

    def runSelectID(self, id):
        self.id = id
        #self.cursor.execute("select * from ") \\TODO-Colocar SELECTS e INSERTS específicos
