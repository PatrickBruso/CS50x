from cs50 import get_string

def main():
    number = get_string("Number: ")

    # Apply Luhn's Algorithm to determine if valid number
    valid = luhn_algorithm(number)

    # Quit if not valid
    if valid is False:
        print("INVALID")


def luhn_algorithm(string):
    # Initialize variables
    products = []
    sum = 0

    # Iterate from 2nd to last number to beginning by 2
    for i in range(len(string) - 2, -1, -2):
        # Multiply each number by 2 and add to list
        products.append((int(string[i]) * 2))

    # iterate through list and obtain products' digits
    for number in products:
        converted_num = str(number)
        if len(converted_num) == 1:
            sum += int(number)
        elif len(converted_num) > 1:
            for num in converted_num:
                sum += int(num)

    # Add sum to digits that weren't multiplied by 2
    for i in range(len(string) - 1, -1, -2):
        sum += int(string[i])

    # convert sum to string to determine last digit
    string_sum = str(sum)
    if string_sum[-1] == '0':
        return True
    else:
        return False


if __name__ == '__main__':
    main()