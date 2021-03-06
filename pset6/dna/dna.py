import csv
import sys


def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # Read database file into a variable
    persons = []

    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for person in reader:
            persons.append(person)

    # Read DNA sequence file into a variable
    with open(sys.argv[2]) as file:
        dna_sequence = file.read()

    # Find longest match of each STR in DNA sequence
    # Pull STRs
    str_list = list(persons[0])
    str_list.pop(0)

    # Create dictionary for longest subsequences match
    longest = []

    # Call longest_match function for each STR
    for item in str_list:
        longest.append(str(longest_match(dna_sequence, item)))

    # Check database for matching profiles
    match_list = []
    found = False

    # Iterate through each person to compare values to longest values
    for person in persons:
        for item in str_list:
            match_list.append((person[item]))
        # If values match, print name and set found to true
        if match_list == longest:
            print(person["name"])
            found = True
        # Reset match_list to empty list for next person's values
        match_list = []

    # Check if no match
    if found == False:
        print("No Match")

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
