import sqlite3

# Connection
connection = sqlite3.connect("student.db")

# create a cursor
cursor = connection.cursor()

# create the table
table_info = """
create table STUDENT (NAME  VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARK INT)
"""

cursor.execute(table_info)

# Insert Some Records
student_records = [
    
    ("Arun", "Data Science", "A", 85),
    ("Sarat", "Machine Learning", "B", 90),
    ("Vijay", "Artificial Intelligence", "A", 78),
    ("Netha", "Data Science", "B", 88),
    ("Ramu", "Cyber Security", "A", 95),
    ("Sankar", "Machine Learning", "B", 82),
    ("Sumathi", "Artificial Intelligence", "A", 80),
    ("Sivakumar", "Data Science", "B", 76),
    ("Palu", "Cyber Security", "A", 92),
    ("Kamal", "Machine Learning", "B", 70),
    ("Rani", "Artificial Intelligence", "A", 89),
    ("Kanimozhi", "Data Science", "B", 91),
    ("Mohan", "Cyber Security", "A", 75),
    ("Venkatesan", "Machine Learning", "B", 84),
    ("Revathi", "Artificial Intelligence", "A", 79),
    ("Poovendhan", "Data Science", "B", 87),
    ("Asha", "Cyber Security", "A", 93),
    ("Kalyani", "Machine Learning", "B", 88),
    ("Madhan", "Artificial Intelligence", "A", 82),
    ("Jegan", "Data Science", "B", 90)
]

insert_query = "INSERT INTO STUDENT (NAME, CLASS, SECTION, MARK) VALUES (?, ?, ?, ?)"
cursor.executemany(insert_query, student_records)

# Display Record

print("Inserted Records")

data = cursor.execute("""SELECT * FROM STUDENT""")

for row in data:
    print(row)

# Commit the transaction
connection.commit()

# Close the connection
connection.close()