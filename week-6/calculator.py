from cs50 import get_int

x = get_int("x: ")
y = get_int("y: ")
print(x + y)

# without cs50 library
x = int(input("x: ")) # cast input string to integer
y = int(input("y: "))
print(x + y)