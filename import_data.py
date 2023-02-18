import sqlite3

# Connect to the database
conn = sqlite3.connect('pos.sqlite')

# Open a cursor to execute SQL commands
c = conn.cursor()

# Execute the SQL script to create the tables and insert sample data
with open('pos.sql') as f:
    script = f.read()
    c.executescript(script)

# Commit the changes and close the connection
conn.commit()
conn.close()
