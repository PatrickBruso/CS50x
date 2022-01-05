// Better implementation of the scrabble problem

#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};


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
        // Subtract 65 from char ASCII value to match with POINTS array
        score += POINTS[word[i] - 65];
    }

    return score;
}
