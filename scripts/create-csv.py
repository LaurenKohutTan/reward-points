# Loads the database from the old reward points system and outputs a CSV file.

import sqlite3
import csv

conn = sqlite3.connect('../users.db')
c = conn.cursor()

c.execute('SELECT * FROM student')
students = c.fetchall()

file = open('students.csv', 'w', newline='')
writer = csv.writer(file)
writer.writerow(['id', 'name', 'period', 'email', 'password', 'rp'])
for student in students:
    writer.writerow(student)

file.close()
conn.close()
