#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

const int BUFFER_SIZE = 512; // set block size to 512 bytes for efficiency in reading
typedef uint8_t BYTE;

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

    BYTE buffer[BUFFER_SIZE]; // create an array of 512 bytes to read from raw file
    int file_index = 0; // set file index for naming JPEGs found
    char jpeg_file[8]; // array for JPEG files recovered

    // Read 512 bytes from input file
    while (fread(&buffer, 1, BUFFER_SIZE, input) == BUFFER_SIZE)
    {
        // Check first four bytes from raw file to see if they match JPEG "signature"
        if ((buffer[0] == 0xff) && (buffer[1] == 0xd8) && (buffer[2] == 0xff) && ((buffer[3] & 0xf0) == 0xe0)) // Last conditional uses bitwise operator to check if first four bytes are "1110"
        {
            sprintf(jpeg_file, "%03i.jpg", file_index); // use sprintf function to print formatted string to memory using the file_index number (to three places).
            FILE *output = fopen(jpeg_file, "w");
            file_index++;
            fwrite(&buffer, 1, BUFFER_SIZE, output);

            // Check if new header or continue reading
            fread(&buffer, 1, BUFFER_SIZE, input);
            while ((buffer[0] != 0xff) && (buffer[1] != 0xd8) && (buffer[2] != 0xff) && ((buffer[3] & 0xf0) != 0xe0))
            {
                fwrite(&buffer, BUFFER_SIZE, 1, output);
            }

            fclose(output);
        }
    }

    // Close files
    fclose(input);
}