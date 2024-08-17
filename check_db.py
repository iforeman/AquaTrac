import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect('instance/aquatrac.db')
cursor = connection.cursor()

# Query to get the list of tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Print the list of tables
print("Tables in the database:")
for table in tables:
    print(table[0])

# Close the connection
connection.close()
