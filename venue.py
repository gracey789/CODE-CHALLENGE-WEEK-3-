import sqlite3

# Establish database connection
conn = sqlite3.connect('concerts.db')
cur = conn.cursor()

class Venue:
    def __init__(self, venue_id):
        # Initialize Venue with venue_id
        self.venue_id = venue_id

    def get_concerts(self):
        # Fetch all concerts for this venue
        cur.execute('SELECT * FROM concerts WHERE venue_id = ?', (self.venue_id,))
        return cur.fetchall()

    def get_bands(self):
        # Fetch all unique bands that played at this venue
        cur.execute('''
            SELECT DISTINCT b.id, b.name, b.hometown
            FROM bands AS b
            JOIN concerts AS c ON c.band_id = b.id
            WHERE c.venue_id = ?
        ''', (self.venue_id,))
        return cur.fetchall()

    def get_concert_on(self, date):
        # Fetch concert held on a specific date
        cur.execute('SELECT * FROM concerts WHERE venue_id = ? AND date = ? LIMIT 1', (self.venue_id, date))
        return cur.fetchone()

    def get_most_frequent_band(self):
        # Find the band that played the most at this venue
        cur.execute('''
            SELECT b.name, COUNT(c.id) AS performance_count
            FROM concerts AS c
            JOIN bands AS b ON c.band_id = b.id
            WHERE c.venue_id = ?
            GROUP BY b.id
            ORDER BY performance_count DESC
            LIMIT 1
        ''', (self.venue_id,))
        return cur.fetchone()


conn.close()  # Close database connection
