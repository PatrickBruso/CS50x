#include <cs50.h>
#include <stdio.h>

// Constant for total scores that will be submitted
const int TOTAL = 3;

// Call the average function
float average(int length, int array[]);

int main(void)
{
    // Create scores array to hold scores
    int scores[TOTAL];

    // Obtain all scores and assign to array by index
    for (int i = 0; i < TOTAL; i++)
    {
        scores[i] = get_int("Score: ");
    }

    printf("Average: %f\n", average(TOTAL, scores));
}

// Function that takes array and length of array and returns average of array items
float average(int length, int array[])
{
    int sum = 0;
    for (int i = 0; i < length; i++)
    {
        sum += array[i];
    }
    return sum / (float) length;
}