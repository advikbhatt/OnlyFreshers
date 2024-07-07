import sqlite3

# Connect to the database
conn = sqlite3.connect('db.sqlite3')

# Create a cursor object
cursor = conn.cursor()

# Execute SQL to create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS quiz_quizresponse (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        question1 TEXT,
        question2 TEXT
        question3 TEXT
        question4 TEXT
        question5 TEXT
        question6 TEXT
        question7 TEXT
        question8 TEXT
        question9 TEXT
        question10 TEXT
        question11 TEXT
        question12 TEXT
        question13 TEXT
        question14 TEXT
        question15 TEXT
        question16 TEXT
        question17 TEXT
        question18 TEXT
        question19 TEXT
        question20 TEXT
    )
''')

# Commit the transaction
conn.commit()

# Close the connection
conn.close()
