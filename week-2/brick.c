#include <stdio.h>
#include <cs50.h>

int main(void)
{
    char c1 = 'H';
    char c2 = 'I';
    char c3 = '!';

    string s = "HI!";

    // Convert char '#' to ASCII by casting as int
    printf("%i %i %i\n", c1, (int) c2, (int) c3);  // Don't actually need to cast as int for it to work (see c1)
    printf("%s\n", s);
    // String is essentially an array of characters, which you can print out and convert to ASCII
    printf("%i %i %i %i\n", s[0], s[1], s[2], s[3]);
}