from cs50 import get_int

# Obtain height from user
height = get_int("Height: ")
if height < 1 or height > 8:
    height = get_int("Height: ")

for i in range(1, height + 1):
    print(" " * (height - i) + "#" * i)