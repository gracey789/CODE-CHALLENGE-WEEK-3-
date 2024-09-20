from band import Band
from venue import Venue
from concert import Concert
import sqlite3

# Establish a connection to the database
conn = sqlite3.connect('concerts.db')
cur = conn.cursor()

# Insert sample data using different syntax and handling multiple inserts separately
bands = [('Band A', 'City A'), ('Band B', 'City B')]
venues = [('Venue X', 'City A'), ('Venue Y', 'City B')]
concerts = [(1, 1, '2024-10-01'), (2, 2, '2024-10-02')]

# Insert data into bands table
for band in bands:
    cur.execute("INSERT INTO bands (name, hometown) VALUES (?, ?)", band)

# Insert data into venues table
for venue in venues:
    cur.execute("INSERT INTO venues (title, city) VALUES (?, ?)", venue)

# Insert data into concerts table
for concert in concerts:
    cur.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (?, ?, ?)", concert)

conn.commit()  # Save changes to the database

# Test Band class methods
band = Band(1)  # Create Band object for band with ID 1
print("Concerts played by this band:", band.concerts())
print("Venues where this band has performed:", band.venues())
print("Band's introductions at concerts:", band.all_introductions())

# Test Venue class methods
venue = Venue(1)  # Create Venue object for venue with ID 1
print("Concerts held at this venue:", venue.concerts())
print("Bands that have played at this venue:", venue.bands())

# Test Concert class methods
concert = Concert(1)  # Create Concert object for concert with ID 1
print("Band performing at this concert:", concert.band())
print("Venue for this concert:", concert.venue())
print("Is this a hometown show?", concert.hometown_show())
print("Concert introduction:", concert.introduction())

conn.close()  # Close the connection to the database
