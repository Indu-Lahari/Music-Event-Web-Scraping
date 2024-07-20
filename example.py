import sqlite3

# Establish a connection and a cursor
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# Query all data
cursor.execute("SELECT * FROM events WHERE Date='2024.10.25'")
rows = cursor.fetchall()
print(rows)

# Query certain columns
cursor.execute("SELECT Band, City FROM events WHERE Date='2024.10.30'")
rows = cursor.fetchall()
print(rows)

# Insert new rows
new_rows = [('Sabrina Carpenter', 'Boston', '2024.10.28'),
            ('Jennie Kim', 'Coachella', '2024.10.28')]

cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
connection.commit()


# Query all data
cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)