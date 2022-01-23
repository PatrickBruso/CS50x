from cs50 import get_float

# Obtain change amount (non-negative number)
change_amount = get_float("Change owed: ")
while change_amount < 0:
    change_amount = get_float("Change owed: ")

# Counter for number of coins given
coins = 0

# Iterate through change amount and decrease starting with quarters, then dimes, etc.
while change_amount >= .25:
    change_amount -= .25
    coins += 1
while change_amount >= .10 and change_amount < .25:
    change_amount -= .10
    coins += 1
while change_amount >= .05 and change_amount < .10:
    change_amount -= .05
    coins += 1
while change_amount < .05 and change_amount > 0:
    change_amount -= .01
    coins += 1

# Print number of coins
print(coins)