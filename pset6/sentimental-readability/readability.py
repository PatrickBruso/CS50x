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

# determine varaibles for Coleman-Liau index
l_calc = (letters / words) * 100
s_calc = (sentences / words) * 100

# Calculate grade index
index = 0.0588 * l_calc - 0.296 * s_calc - 15.8
index = round(index)

# Print grade
if index < 1:
    print("Before Grade 1")
elif index > 15:
    print("Grade 16+")
else:
    print(f"Grade {index}")
