import csv

titles = {}

# Open CSV file
with open("favorites.csv", "r") as file:
    # Create reader
    reader = csv.DictReader(file)

    # Print out all show titles
    for row in reader:
        # Strip off whitespace and make uppercase
        title = row["title"].strip().upper()
        # Add to dictionary and increment for duplicates
        if not title in titles:
            titles[title] = 0
        titles[title] += 1

# Function that obtains the value for a title (to use with sorted)
def get_value(title):
    return titles[title]

# Call sorted and apply the key=get_value function call
for title in sorted(titles, key=get_value):
    print(title, titles[title])