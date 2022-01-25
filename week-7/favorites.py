import csv

titles = []

# Open CSV file
with open("favorites.csv", "r") as file:
    # Create reader
    reader = csv.DictReader(file)

    # Print out all show titles
    for row in reader:
        if not row["title"] in titles:
            titles.append(row["title"])

for title in titles:
    print(title)