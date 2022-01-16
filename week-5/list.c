#include <stdio.h>

int main(void)
{
    // Put memory on stack
    int list[3];

    list[0] = 1;
    list[1] = 2;
    list[2] = 3;

    for (int i = 0; i < 3; i++)
    {
        printf("%i\n", list[i]);
    }

    // Put memory on heap
    int *list2 = malloc(3 * sizeof(int));
    if (list2 == NULL)
    {
        return 1;
    }

    list2[0] = 1;
    list2[1] = 2;
    list2[2] = 3;

    // Can change size of array, unlike stack
    list2 = malloc(4 * sizeof(int));
    list2[3] = 4;
}