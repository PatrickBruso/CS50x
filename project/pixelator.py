import math
import numpy as np
from PIL import Image

def main(file_location, palette_name):

    """ Should I create a function for reading in an image location and returning a reshaped array of colors?
    Maybe not because I need to resize the image.  If so, I'll have to resize the image first before I obtain the array"""

    # Open palette choice
    with Image.open(f'static/palettes/{palette_name}') as palette:
        # Create array of palette colors
        array = np.array(palette.convert('RGB'))

    # Reshape array into usable list of colors
    palette_colors_list = array.reshape(-1, 3)

    r, g, b = palette_colors_list[0]
    #print(r)
    #print(g)
    #print(b)

    # Open image choice
    with Image.open(file_location) as image:
        array2 = np.array(image.convert('RGB')) # Array of larger sized image to see difference when not shrunken

        # Resize image to 1/4 of original
        image_resized = image.resize((image.width // 4, image.height // 4))

        # Create array of resized image
        resized_array = np.array(image_resized.convert('RGB'))

    # Reshape array into iterable list of colors
    test_big = array2.reshape(-1, 3)
    image_colors_list = resized_array.reshape(-1, 3)

    # print(len(test_big)) # 272640
    # print(len(test_small)) # 16960

    # Create empty list for array of pixelized image's colors
    pixel_image_list = []

    # Append to list each RGB value using color_picker function
    for color in image_colors_list:
        color_picker(palette_colors_list, color)


def color_picker(palette_list, pixel):
    """
    Take a pixel and a target palette of colors and find the color in the
    palette which is closet to the given pixel.  Return the palette color
    as an r, g, b value.
    """

    print(palette_list)
    print(pixel)



if __name__ == "__main__":
    main("static/images/landscape.jpg", "ammo8.png")