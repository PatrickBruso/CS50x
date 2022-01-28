import csv

from cs50 import SQL

# Open db file
db = SQL("sqlite:///favorites.db")

# Obtain title from user and strip whitespace
title = input("Title: ").strip()

# Execute db query on database to obtain list of rows from favorites where title matches user input
rows = db.execute("SELECT COUNT(*) AS counter FROM favorites WHERE title LIKE ?", title)

# Take first row
row = rows[0]

# Print out counter from first row (which is a dictionary)
print(row["counter"])