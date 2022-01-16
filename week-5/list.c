#include <stdio.h>

int main(void)
{
    /* old version
    int list[3];

    list[0] = 1;
    list[1] = 2;
    list[2] = 3;

    for (int i = 0; i < 3; i++)
    {
        printf("%i\n", list[i]);
    }
    */

    int *list = malloc(3 * sizeof(int));
}