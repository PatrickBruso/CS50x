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