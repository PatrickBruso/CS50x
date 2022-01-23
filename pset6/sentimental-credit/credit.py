from cs50 import get_string

def main():
    number = get_string("Number: ")

    # Apply Luhn's Algorithm to determine if valid number
    sum = 0
    for i in range(len(number) - 2, -1, -2):
        sum += (int(number[i]) * 2)
        print(sum)
    print(sum)

if __name__ == '__main__':
    main()