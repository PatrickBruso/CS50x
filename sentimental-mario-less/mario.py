from cs50 import get_int

height = get_int("Height: ")
    try:
        

for i in range(height):
    print(" " * (height - i) + "#" * i)