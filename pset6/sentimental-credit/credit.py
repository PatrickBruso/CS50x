from cs50 import get_string

def main():
    number = get_string("Number: ")

    # Apply Luhn's Algorithm to determine if valid number
    products = []
    sum = 0
    for i in range(len(number) - 2, -1, -2):
        products.append((int(number[i]) * 2))

    for number in products:
        converted_num = str(number)
        if len(converted_num) == 1:
            sum += int(number)
        elif len(converted_num) > 1:
            for num in converted_num:
                sum += int(num)
    print(sum)

def luhn_algorithm:



if __name__ == '__main__':
    main()