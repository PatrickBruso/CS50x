from cs50 import get_int

x = get_int("x: ")
y = get_int("y: ")
print(x + y)

# Without cs50 library (and using exceptions)
try:
    # Cast input string to integer
    x = int(input("x: "))
    # If user does not enter integer
except ValueError:
    print("That is not an int!")
    exit()
try:
    y = int(input("y: "))
except ValueError:
    print("That is not an int!")
    exit()
print(x + y)