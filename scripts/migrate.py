# Loads the database from the old reward points system and outputs a CSV file.

import sqlite3
import csv

old = sqlite3.connect('old.db')
new = sqlite3.connect('../instance/users.db')

c_old = old.cursor()
c_new = new.cursor()

c_old.execute('SELECT email, rp FROM student')
students = c_old.fetchall()

for student in students:
    c_new.execute('INSERT INTO legacy_points VALUES (?, ?)', (student[0], student[1]))

new.commit()

old.close()
new.close()
