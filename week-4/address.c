#include <stdio.h>

int main(void)
{
    int n = 50;
    printf("%i\n", n);

    // Example of a pointer
    int *p = &n;
    printf("%p\n", p);

    // Don't even need the p variable
    printf("%p\n", &n);
}