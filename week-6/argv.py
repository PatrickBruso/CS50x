# How to use command line arguments
from sys import argv

print(f"Program: {argv[0]}")

if len(argv) == 2:
    print(f"hello, {argv[1]}")
else:
    print("hello, world")