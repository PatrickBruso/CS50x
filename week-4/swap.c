// Program to swap integers using pointers
#include <stdio.h>

void swap(int *a, int *b);

int main(void)
{
    int x = 1;
    int y = 2;

    printf("x is %i, y is %i\n", x, y);
    swap(&x, &y); // Pass in address to x and y
    printf("x is %i, y is %i\n", x, y);
}

// swap function obtains address of integers to make changes
void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}