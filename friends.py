# We connect to a new db and create a single table.

# We will use the sqlite3 module.
import sqlite3
conn = sqlite3.connect('my_friends.db') # Create the connection to a db.

# Create cursor object.
c = conn.cursor()

# Execute a line of SQL with the cursor.
c.execute('CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);')

# Commit change.
conn.commit()
conn.close()