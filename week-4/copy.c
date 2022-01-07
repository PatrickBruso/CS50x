#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main(void)
{
    char *s = get_string("s: ");

    // Create pointer to new string and allocate memory
    char *t = malloc(strlen(s) + 1);
    // Error check if malloc fails
    if (t == NULL)
    {
        return 1;
    }

    /**for (int i = 0, n = strlen(s) + 1; i < n; i++)
    {
        t[i] = s[i];
    }**/

    strcpy(t, s); // same as the for loop

    // Check for characters in string
    if (strlen(t) > 0)
    {
        t[0] = toupper(t[0]);
    }

    printf("s: %s\n", s);
    printf("t: %s\n", t);

    // Free allocated space for t (get_string does this automatically for s)
    free(t);

    return 0; // successful termination
}