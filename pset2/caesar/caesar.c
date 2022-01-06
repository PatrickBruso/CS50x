#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    // Make sure proper command-line arguments inputted
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else
    {
        // Check that argv[1] contains only decimal digits
        for (int i = 0, n = strlen(argv[1]); i < n; i++)
        {
            if (argv[1][i] < '0' || argv[1][i] > '9')
            {
                printf("Usage: ./caesar key\n");
                return 1;
            }
        }
    }

    // Convert key string to integer
    int key = atoi(argv[1]);

    // Apply mod 26 to key to determine shift amount
    int shift_amount = key % 26;

    // Obtain plaintext string to apply cipher to
    string plaintext = get_string("plaintext: ");

    // Use for loop to shift plaintext string to ciphertext
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        // Check if lowercase
        if (islower(plaintext[i]) != 0)
        {
            // Check to see if char needs to wrap around from 'z' to 'a'
            if (plaintext[i] + shift_amount > 122)
            {
                // Equation to wraparound text that goes past 'z'
                plaintext[i] = 96 + ((plaintext[i] + shift_amount) - 122);
            }
            else
            {
                plaintext[i] += shift_amount;
            }
        }
        // Check if uppercase
        else if (isupper(plaintext[i]) != 0)
        {
            // Check to see if char needs to wrap around from 'Z' to 'A'
            if (plaintext[i] + shift_amount > 90)
            {
                // Equation to wraparound text that goes past 'Z'
                plaintext[i] = 64 + ((plaintext[i] + shift_amount) - 90);
            }
            else
            {
                plaintext[i] += shift_amount;
            }
        }
    }

    // Successful exit
    printf("ciphertext: %s", plaintext);
    printf("\n");
    return 0;
}