#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *x = malloc(3 * sizeof(int));  // obtain memory for three int and assign to int pointer x
    x[1] = 72;
    x[2] = 73;
    x[3] = 33;
}