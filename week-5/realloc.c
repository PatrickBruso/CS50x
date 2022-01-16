#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    // Example using realloc
    // Dynamically allocate an array of size 3
    int *list2 = malloc(3 * sizeof(int));
    if (list2 == NULL)
    {
        return 1;
    }

    // Assign three numbers to that array
    list2[0] = 1;
    list2[1] = 2;
    list2[2] = 3;

    // Resize old array to be of size 4
    int *tmp = realloc(list2, 4 * sizeof(int));
    if (tmp == NULL)
    {
        free(list2);
        return 1;
    }

    // Add fourth number to new array
    tmp[3] = 4;

    list2 = tmp; // set list2 pointer to tmp pointer

    // Print new array
    for (int i = 0; i < 4; i++)
    {
        printf("%i\n", list2[i]);
    }
    // Free new array
    free(list2);
    return 0;
}