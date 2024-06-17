import sqlite3
import datetime

class User:
    def __init__(self):
        db = sqlite3.connect('use.db')
        c = db.cursor()

    def check_user(self,id) -> bool:
        res = self.c.execute('SELECT * FROM users WHERE id = ?',(id,)).fetchone()
        return True if res else False

    def check_start_time(self,id):
        res = self.c.execute('SELECT time FROM users WHERE id = ?',(id,)).fetchone()
        return res[0]


