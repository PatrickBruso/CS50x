#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *x = malloc(3 * sizeof(int));  // obtain memory for three int and assign to int pointer x
    x[0] = 72;
    x[1] = 73;
    x[2] = 33;

    free(x);  // always free memory if you use malloc
}