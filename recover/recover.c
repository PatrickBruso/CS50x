#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 1)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }
}