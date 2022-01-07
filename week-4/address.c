#include <stdio.h>

int main(void)
{
    int n = 50;
    printf("%i\n", n);

    // Example of a pointer
    int *p = &n;
    printf("%p\n", p);  // Don't need to use * as that just describes what p is (same as int, char, etc.)

    // Don't even need the p variable
    printf("%p\n", &n);

    // Can use * as a dereference operator to print an int using that int's location
    printf("%i\n", *p);

    char *s = "HI!";  // Operates the same as "string s" from cs50.h
    printf("%s\n", s);
}