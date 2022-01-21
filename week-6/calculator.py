from cs50 import get_int

x = get_int("x: ")
y = get_int("y: ")
print(x + y)

# without cs50 library (and using exceptions)
try:
    x = int(input("x: ")) # cast input string to integer
except ValueError: # if user does not enter integer
    print("That is not an int!")
    exit()
try:
    y = int(input("y: "))
except ValueError:
    print("That is not an int!")
    exit()
print(x + y)