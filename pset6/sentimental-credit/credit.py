from cs50 import get_string

def main():
    number = get_string("Number: ")

    # Apply Luhn's Algorithm to determine if valid number
    sum = []
    for i in range(len(number) - 2, -1, -2):
        sum.append((int(number[i]) * 2))

    for number in sum:
        

if __name__ == '__main__':
    main()