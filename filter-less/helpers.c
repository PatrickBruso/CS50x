#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            RGBTRIPLE temp = image[i][j];
            int average = (temp.rgbtBlue + temp.rgbtGreen + temp.rgbtRed) / 3.0;
            image[i][j].rgbtBlue = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtRed = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            RGBTRIPLE temp = image[i][j];

            // Calculations for sepia colors assigned to temporary sepia pixels
            int sepiaRed = .393 * temp.rgbtRed + .769 * temp.rgbtGreen + .189 * temp.rgbtBlue;
            int sepiaGreen = .349 * temp.rgbtRed + .686 * temp.rgbtGreen + .168 * temp.rgbtBlue;
            int sepiaBlue = .272 * temp.rgbtRed + .534 * temp.rgbtGreen + .131 * temp.rgbtBlue;

            // Check for max int value of 255; if greater than, set to max 255
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }

            // Assign sepia values to current pixel
            image[i][j].rgbtBlue = sepiaBlue;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtRed = sepiaRed;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++) // half width because once you've swapped the first half you're finished
        {
            // temporary red, green, and blue pixels for swap
            int tempRed = image[i][j].rgbtRed;
            int tempGreen = image[i][j].rgbtGreen;
            int tempBlue = image[i][j].rgbtBlue;

            // Assign opposite width pixels to current pixel
            image[i][j].rgbtRed = image[i][width - (j + 1)].rgbtRed;
            image[i][j].rgbtGreen = image[i][width - (j + 1)].rgbtGreen;
            image[i][j].rgbtBlue = image[i][width - (j + 1)].rgbtBlue;

            // Assign temp pixels to opposite width pixels
            image[i][width - (j + 1)].rgbtRed = tempRed;
            image[i][width - (j + 1)].rgbtGreen = tempGreen;
            image[i][width - (j + 1)].rgbtBlue = tempBlue;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Create a copy of image
    RGBTRIPLE copy[height][width];

    // Iterate over image to put all pixels into copy
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            RGBTRIPLE copy[i][j] = image[i][j];
        }
    }

    // Initialize variables
    int blurRed = 0;
    int blurGreen = 0;
    int blurBlue = 0;
    int counter = 0;

    return;
}
