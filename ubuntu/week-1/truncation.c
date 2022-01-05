#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get two integers from user
    int x = get_int("x: ");
    int y = get_int("y: ");

    // Set integers to floats to receive float answer
    float z = (float) x / (float) y;

    printf("%f\n", z);
}