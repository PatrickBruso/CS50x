#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // Obtain user name
    string answer = get_string("What's your name? ");
    // Greet user
    printf("Hello, %s\n", answer);
}