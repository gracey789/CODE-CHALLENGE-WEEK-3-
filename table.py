import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('concerts.db')
cur = conn.cursor()

# Create the bands table
cur.execute('''
    CREATE TABLE IF NOT EXISTS bands (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        hometown TEXT
    )
''')

# Create the venues table
cur.execute('''
    CREATE TABLE IF NOT EXISTS venues (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        city TEXT
    )
''')

# Create the concerts table
cur.execute('''
    CREATE TABLE IF NOT EXISTS concerts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        band_id INTEGER,
        venue_id INTEGER,
        date TEXT,
        FOREIGN KEY (band_id) REFERENCES bands(id),
        FOREIGN KEY (venue_id) REFERENCES venues(id)
    )
''')

# Commit the transaction and close the connection
conn.commit()
conn.close()

print("Database and tables created successfully.")