# Bulk inserts or multiple inserts to an existing db.

import sqlite3
conn = sqlite3.connect('my_friends.db') 

# Create cursor object.
c = conn.cursor()

people = [
	('Roald', 'Amundsen', 5),
	('Rosa', 'Parks', 8),
	('Henry', 'Hudson', 7),
	('Neil', 'Armstrong', 7),
	('Daniel', 'Boone', 3)]

# Pass in the query and then the data from the people tuple.
c.executemany('INSERT INTO friends VALUES (?, ?, ?)', people)

# Commit change.
conn.commit()
conn.close()