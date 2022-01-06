#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int index_calculation(int letters, int words, int sentences);

int main(void)
{
    // Obtain string input
    string s = get_string("Input: ");

    // Initialize variables
    int letters = 0;
    int sentences = 0;
    int words = 1;

    // Loop to detect letters, words, and sentences
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        if (s[i] >= 'a' && s[i] <= 'z')
        {
            letters += 1;
        }
        else if (s[i] >= 'A' && s[i] <= 'Z')
        {
            letters += 1;
        }
        else if (s[i] == '.' || s[i] == '?' || s[i] == '!')
        {
            sentences += 1;
        }
        else if (s[i] == ' ')
        {
            words += 1;  // No space after last word, need to start counter at 1 to count last word
        }
    }

    int grade = index_calculation(letters, words, sentences);

    // If statement to print correct grade if lower than 1 or above 16
    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", grade);
    }
}

int index_calculation(int letters, int words, int sentences)
{
    // Determine inputs L and S for calculation of grade index
    float L = ((float)letters / words) * 100;
    float S = ((float)sentences / words) * 100;

    // Calculate grade index
    float index = 0.0588 * L - 0.296 * S - 15.8;

    // call round function on index and assign to integer to remove decimal places
    int grade = round(index);

    return grade;
}