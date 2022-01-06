#include <stdio.h>
#include <cs50.h>
#include <string.h>

// Data structure
typedef struct
{
    string name;
    string number;
}
person;  // Name of new data structure

int main(void)
{
    // Create an array called people with two items of the person data structure.
    person people[2];

    // Assign names and numbers to the first index of people array
    people[0].name = "Brian";
    people[0].number = "+1-617-495-1000";

    // Assign names and numbers to the second index of people array
    people[1].name = "David";
    people[1].number = "+1-949-468-2750";

    for (int i = 0; i < 2; i++)
    {
        if (strcmp(people[i].name, "David") == 0)
        {
            printf("Found %s\n", people[i].number);
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}