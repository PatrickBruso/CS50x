from cs50 import get_int

def main():
    number = get_int("Number: ")

    # Apply Luhn's Algorithm to determine if valid number
    sum = 0
    for i in range(-2, 0, 2):
        sum += (i * 2)
    print(sum)

if __name__ == '__main__':
    main()