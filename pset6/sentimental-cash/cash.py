from cs50 import get_float

change_amount = get_float("Change owed: ")
while change_amount < 0:
    change_amount = get_float("Change owed: ")

coins = 0

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

print(coins)