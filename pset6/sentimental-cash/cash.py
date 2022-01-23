from cs50 import get_float

coins = [.25, .10, .05, .01]

change_amount = get_float("Change owed: ")
while change_amount < 0:
    change_amount = get_float("Change owed: ")