from tkinter import *
import sqlite3
conn = sqlite3.connect('database.db')
c = conn.cursor()
number = []
patients = []
sql = "SELECT * FROM appointments"
res = c.execute(sql)
for r in res:
    ids = r[0]
    name = r[1]
    number.append(ids)
    patients.append(name)


root = Tk()
b = Application(root)
root.geometry("1366x768+0+0")
root.resizable(False, False)
root.mainloop()

