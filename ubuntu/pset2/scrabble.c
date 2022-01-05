#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Call computer_score function to use in main
int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // If statements to print statement based upon higher score (or tie)
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score2 > score1)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int compute_score(string word)
{
    // Convert string to all uppercase to avoid case sensitive errors
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        word[i] = toupper(word[i]);
    }

    // Placeholder counter for score
    int score = 0;

    // Iterate over string and add score based on characters in string
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        if (word[i] == 'A' || word[i] == 'E' || word[i] == 'I' || word[i] == 'L' || word[i] == 'N' || word[i] == 'O' || word[i] == 'R'
            || word[i] == 'S' || word[i] == 'T' || word[i] == 'U')
        {
            score += 1;
        }
        else if (word[i] == 'D' || word[i] == 'G')
        {
            score += 2;
        }
        else if (word[i] == 'B' || word[i] == 'C' || word[i] == 'M' || word[i] == 'P')
        {
            score += 3;
        }
        else if (word[i] == 'F' || word[i] == 'H' || word[i] == 'V' || word[i] == 'W' || word[i] == 'Y')
        {
            score += 4;
        }
        else if (word[i] == 'K')
        {
            score += 5;
        }
        else if (word[i] == 'J' || word[i] == 'X')
        {
            score += 8;
        }
        else if (word[i] == 'Q' || word[i] == 'Z')
        {
            score += 10;
        }
    }
    return score;
}
