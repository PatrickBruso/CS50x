import csv

titles = []

# Open CSV file
with open("favorites.csv", "r") as file:
    # Create reader
    reader = csv.DictReader(file)

    # Print out all show titles
    for row in reader:
        # Strip off whitespace
        title = row["title"].strip().upper()
        # Check whether title is already in list before appending
        if not title in titles:
            titles.append(title)

for title in titles:
    print(title)