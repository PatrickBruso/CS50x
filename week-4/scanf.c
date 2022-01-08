// Standard C program to get input from user
// result is null becuse we didn't allocate memory
#include <stdio.h>
int main(void)
{
    char *s;
    printf("s: ");
    scanf("%s", s);
    printf("s: %s\n", s);
}