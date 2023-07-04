import mysql.connector
import json
from datetime import datetime

class jdict(dict):
    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value

class dbConnector:
    secdb = None
    cursor = None

    def __init__(self):
        self.secdb = mysql.connector.connect(
            host="localhost",
            user="root",   
            password="Berserker2046",
            database="secretary"
        )
        self.cursor = self.secdb.cursor()

    def select(self, choise):
        match choise:
            case "note":
                return self.selectnotes()
            case "teachers":
                return self.selectteachers()
            case _:
                return
        return

    def insert(self, data):
        data2 = data[data["put"]]
        str = f"INSERT INTO {data['put']} VALUES(0, \'{data2['sender']}\', \'{data2['group']}\', \'{data2['text']}\', \'{data2['date']}\')"
        self.cursor.execute(str)
        self.secdb.commit()
        return

    def selectnotes(self):
        self.secdb.commit()
        self.cursor.execute("SELECT * FROM note")
        con = []
        res = self.cursor.fetchall()
        for i in res:
            con.append({"id":i[0], "sender":i[1], "group":i[2], "text":i[3], "date":i[4].strftime("%d.%m.%Y")})
        con_json = json.dumps({"notes":con}, indent=2, sort_keys=False, ensure_ascii=False)
        print(con_json)
        return con_json

    def selectteachers(self):
        self.secdb.commit()
        self.cursor.execute("SELECT * FROM teachers ORDER BY surname, name ASC")
        con = []
        res = self.cursor.fetchall()
        for i in res:
            con.append({"surname":i[2], "name":i[1]})
        con_json = json.dumps({"teachers":con}, indent=2, sort_keys=False, ensure_ascii=False)
        print(con_json)
        return con_json