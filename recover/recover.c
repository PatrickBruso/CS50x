#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    // Open file and and inform user if cannot be opened
    FILE *input = fopen(argv[1], "r");  // open file for reading
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    const int BUFFER_SIZE = 512; // set block size to 512 bytes for efficiency in reading
    uint8_t buffer[BUFFER_SIZE]; // create an array of 512 bytes to read from raw file

    // Read 512 bytes from input file
    while (fread(&buffer, sizeof(uint8_t), BUFFER_SIZE, input) == BUFFER_SIZE)
    {
        // Check first four bytes from raw file to see if they match JPEG "signature"
        if 
    }

    // Close files
    fclose(input);
}