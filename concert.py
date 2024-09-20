import sqlite3

# Reuse the database connection
conn = sqlite3.connect('concerts.db')
cur = conn.cursor()

class Concert:
    def __init__(self, concert_id):
        self.concert_id = concert_id

    def band(self):
        cur.execute('''
            SELECT bands.id, bands.name, bands.hometown
            FROM bands
            JOIN concerts ON concerts.band_id = bands.id
            WHERE concerts.id = ?
        ''', (self.concert_id,))
        return cur.fetchone()

    def venue(self):
        cur.execute('''
            SELECT venues.id, venues.title, venues.city
            FROM venues
            JOIN concerts ON concerts.venue_id = venues.id
            WHERE concerts.id = ?
        ''', (self.concert_id,))
        return cur.fetchone()

    def hometown_show(self):
        cur.execute('''
            SELECT bands.hometown, venues.city
            FROM concerts
            JOIN bands ON concerts.band_id = bands.id
            JOIN venues ON concerts.venue_id = venues.id
            WHERE concerts.id = ?
        ''', (self.concert_id,))
        result = cur.fetchone()
        return result[0] == result[1]

    def introduction(self):
        cur.execute('''
            SELECT bands.name, bands.hometown, venues.city
            FROM concerts
            JOIN bands ON concerts.band_id = bands.id
            JOIN venues ON concerts.venue_id = venues.id
            WHERE concerts.id = ?
        ''', (self.concert_id,))
        band_name, band_hometown, venue_city = cur.fetchone()
        return f"Hello {venue_city}!!!!! We are {band_name} and we're from {band_hometown}"