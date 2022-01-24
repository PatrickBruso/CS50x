from cs50 import get_string

# Obtain input text
text = get_string("Text: ")

# Initialize variables
letters = 0
words = 1
sentences = 0

for characters in text:
    if ((characters >= 'a' and characters <= 'z') or
        (characters >= 'A' and characters <= 'Z')):
        letters += 1
    if characters == '.' or characters == '?' or characters == '!':
        sentences += 1
    if characters == ' ':
        words += 1

l_calc = (letters / words) * 100
s_calc = (sentences / words) * 100

# Calculate grade index
index = 0.0588 * l_calc - 0.296 * s_calc - 15.8

print(index)

# call round function on index and assign to integer to remove decimal places
int grade = round(index)