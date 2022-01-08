// Standard C program to get input from user
#include <stdio.h>
int main(void)
{
    int x;
    printf("x: ");
    scanf("%i", &x); // Obtain integer and put it in address of x
    printf("x: %i\n", x);

    char *s;
    printf("s: ");
    scanf("%s", s);
    printf("s: %s\n", s);
}