import sqlite3

# Reuse the database connection
conn = sqlite3.connect('concerts.db')
cur = conn.cursor()

class Band:
    def __init__(self, band_id):
        self.band_id = band_id

    def concerts(self):
        cur.execute('''
            SELECT * FROM concerts WHERE band_id = ?
        ''', (self.band_id,))
        return cur.fetchall()

    def venues(self):
        cur.execute('''
            SELECT DISTINCT venues.id, venues.title, venues.city
            FROM venues
            JOIN concerts ON concerts.venue_id = venues.id
            WHERE concerts.band_id = ?
        ''', (self.band_id,))
        return cur.fetchall()

    def play_in_venue(self, venue_id, date):
        cur.execute('''
            INSERT INTO concerts (band_id, venue_id, date)
            VALUES (?, ?, ?)
        ''', (self.band_id, venue_id, date))
        conn.commit()

    def all_introductions(self):
        cur.execute('''
            SELECT bands.name, bands.hometown, venues.city
            FROM concerts
            JOIN bands ON concerts.band_id = bands.id
            JOIN venues ON concerts.venue_id = venues.id
            WHERE concerts.band_id = ?
        ''', (self.band_id,))
        introductions = []
        for band_name, band_hometown, venue_city in cur.fetchall():
            introductions.append(f"Hello {venue_city}!!!!! We are {band_name} and we're from {band_hometown}")
        return introductions

    @staticmethod
    def most_performances():
        cur.execute('''
            SELECT bands.name, COUNT(concerts.id) AS performance_count
            FROM concerts
            JOIN bands ON concerts.band_id = bands.id
            GROUP BY bands.id
            ORDER BY performance_count DESC
            LIMIT 1
        ''')
        return cur.fetchone()