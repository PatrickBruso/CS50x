// Example of linear search (O(n) time)

#include <stdio.h>
#include <cs50.h>

int DOORS = 7;
int numbers[] = {4, 6, 8, 2, 7, 5, 0};

int main(void)
{
    for (int i = 0; i < DOORS; i++)
    {
        if (numbers[i] == 0)
        {
            return true;
        }
    }
    return false;
}