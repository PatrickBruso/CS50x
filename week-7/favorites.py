import csv

# Use set to ignore duplicates
titles = set()

# Open CSV file
with open("favorites.csv", "r") as file:
    # Create reader
    reader = csv.DictReader(file)

    # Print out all show titles
    for row in reader:
        # Strip off whitespace and make uppercase
        title = row["title"].strip().upper()
        # Add to set
        titles.add(title)

# Use sorted method to sort list of titles
for title in sorted(titles):
    print(title)