from cs50 import get_float

# Obtain change amount (non-negative number)
change = get_float("Change owed: ")
while change < 0:
    change = get_float("Change owed: ")

# Convert to cents
change = round(change * 100)

# Counter for number of coins given
coins = 0

# Iterate through change amount and decrease starting with quarters, then dimes, etc.
while change > 0:
    while change >= 25:
        coins += 1
        change -= 25
    while change >= 10:
        coins += 1
        change -= 10
    while change >= 5:
        coins += 1
        change -= 5
    while change >= 1:
        change -= 1
        coins += 1

# Print number of coins
print(coins)