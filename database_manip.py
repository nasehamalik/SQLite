import sqlite3
db = sqlite3.connect('data/pythonprogramming_db')
cursor = db.cursor()

# Create a table called python_programming
cursor.execute('''
    CREATE TABLE python_programming(id INTEGER PRIMARY KEY, name TEXT, grade INTEGER)
'''
)

cursor = db.cursor()
# Create variables storing the id, name and grade for each student
id1 = 55
name1 = 'Carl Davis'
grade1 = 61

id2 = 66
name2 = 'Dennis Fredrickson'
grade2 = 88

id3 = 77
name3 = 'Jane Richards'
grade3 = 78

id4 = 12
name4 = 'Peyton Sawyer'
grade4 = 45

id5 = 2
name5 = 'Lucas Brooke'
grade5 = 99

# Create a list containing each student's id, name anf grade
studentinfo = [(id1,name1,grade1),(id2,name2,grade2),(id3,name3,grade3),(id4,name4,grade4),(id5,name5,grade5)]

# Insert student info into table
cursor.executemany(''' INSERT INTO python_programming(id, name, grade) VALUES(?,?,?)''',
studentinfo)
db.commit()

# Select all records with a grade between 60 and 80.
cursor.execute('''SELECT id, name FROM studentinfo WHERE grade BETWEEN 60 AND 80''',
studentinfo)
python_programming = cursor.fetchall()
print(python_programming)

# Update Carl Davis’s grade to 65
grade = 65
name = 'Carl Davis'
cursor.execute('''UPDATE python_programming SET grade = ? WHERE name = ? ''', 
(grade, name))
db.commit

# Delete Dennis Fredrickson’s row
name = 'Dennis Fredrickson'
cursor.execute('''DELETE FROM python_programming WHERE name = ? ''', (name,))
cursor.execute('''DROP TABLE python_programming''')
db.commit

# Update the grade of all people with an id below than 55
cursor.execute('''UPDATE python_programming SET grade = 78 WHERE id<55''')
db.commit

db.close()