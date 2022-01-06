#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    float owed;
    // Obtain change amount (non-negative)
    do
    {
        owed = get_float("Change owed: ");
    }
    while (owed < 0);

    // Convert dollars to cents to avoid floating-point imprecision errors
    int cents = round(owed * 100);

    // Set up counter to deterine how many coins given
    int counter = 0;

    // While loops to subtract largest coints first based on amount of change left
    while (cents >= 25)
    {
        cents -= 25;
        counter += 1;
    }

    while (cents >= 10 && cents < 25)
    {
        cents -= 10;
        counter += 1;
    }

    while (cents >= 5 && cents < 10)
    {
        cents -= 5;
        counter += 1;
    }

    while (cents > 0 && cents < 5)
    {
        cents -= 1;
        counter += 1;
    }

    printf("%i\n", counter);
}