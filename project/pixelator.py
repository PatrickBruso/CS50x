import math
import time
import numpy as np
from PIL import Image

# Constant resize amount that will be used to shrink and expand image
RESIZE = 3

def main(file_location, palette_name):

    """ Should I create a function for reading in an image location and returning a reshaped array of colors?
    Maybe not because I need to resize the image.  If so, I'll have to resize the image first before I obtain the array"""

    """
    To do:
    Compare output file to output of code in place final project for same picture and palette
    Create version without using numpy arrays... (might be only option to match SimpleImage program results)
    """

    # Open palette choice
    with Image.open(f'static/palettes/{palette_name}') as palette:

        # Create array of palette colors
        array = np.array(palette.convert('RGB'))

    # Reshape array into usable list of colors
    palette_colors_list = array.reshape(-1, 3)

    # Open image choice
    with Image.open(file_location) as image:

        # Resize image to 1/4 of original
        image_resized = image.resize((image.width // RESIZE, image.height // RESIZE))

        width, height = image_resized.size

        # Create array of resized image
        resized_array = np.array(image_resized.convert('RGB'))

    # Reshape array into iterable list of colors
    image_colors_list = resized_array.reshape(-1, 3)

    # Create empty list for array of pixelized image's colors
    pixel_image_array = np.empty_like(image_colors_list)

    # Create counter for updating pixel_image_list array with new pixel
    counter = 0

    # Append to list each RGB value using color_picker function
    for pixel in image_colors_list:

        # obtain the new pixel value for that pixel and assign to new_pixel
        new_pixel = color_picker(palette_colors_list, pixel)

        # Use counter to update pixel_image_list with new pixel value
        pixel_image_array[counter] = new_pixel

        # increment counter for next value
        counter += 1

    # Reshape pixel_image_array to match the original array shape of the resized image
    pixel_image_array = np.reshape(pixel_image_array, resized_array.shape)

    # Create PIL image of pixelated array of colors
    pixel_image = Image.fromarray(pixel_image_array)

    # Resize new pixel image
    pixel_image_resized = pixel_image.resize((width * RESIZE, height * RESIZE))

    # Save new image
    pixel_image_resized.save("test.jpg")


def color_picker(palette_list, pixel):
    """
    Take a pixel and a target palette of colors and find the color in the
    palette which is closet to the given pixel.  Return the palette color
    as an r, g, b value.
    """

    # Grab RGB values for target pixel
    r, g, b = int(pixel[0]), int(pixel[1]), int(pixel[2])

    # Create empty list for distance values
    distance_list = []

    # Iterate over each color in the palette
    for color in palette_list:

        # Determine the distance value for each color in pallete
        distance = int(math.sqrt((r - color[0]) ** 2 + (g - color[1]) ** 2 + (b - color[2]) ** 2))

        # Append distance value for that color to distance_list
        distance_list.append(distance)

    # Find the smallest value in the distance list
    closest_color = min(distance_list)

    # Obtain the index location of the smallest distance value
    location = distance_list.index(closest_color)

    # Return the color in pallete_list that has smallest distance from target pixel
    return palette_list[location]


if __name__ == "__main__":
    start_time = time.time()
    main("static/images/landscape.jpg", "cybear9.png")
    print("------- %s seconds -------" % (time.time() - start_time))