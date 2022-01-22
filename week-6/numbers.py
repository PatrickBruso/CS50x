from sys import exit

numbers = [4, 6, 8, 2, 7, 5, 0]

if 0 in numbers:
    print("Found")
    exit(0)

print("Not found")
exit(1)