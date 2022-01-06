#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    // Obtain starting size greater than 9
    do
    {
        n = get_int("Start size: ");
    }
    while (n < 9);

    int k;
    // Obtain ending size greater than startin size
    do
    {
        k = get_int("End size: ");
    }
    while (k < n);

    int years = 0;
    int new_size = n;

    // Calculate years based on starting and ending size
    while (new_size < k)
    {
        new_size = (new_size + (new_size / 3) - (new_size / 4));
        years++;
    }

    printf("Years: %i\n", years);
}