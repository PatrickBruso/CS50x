#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    // Obtain starting size between 1 and 8, inclusive
    do
    {
        n = get_int("Height: ");
    }
    while (n > 8 || n < 1);

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            // Arithmetic to determine if printing space or hash
            if (i + j < n - 1)
            {
                printf(" ");
            }
            else
            {
                printf("#");
            }
        }
        printf("\n");
    }
}