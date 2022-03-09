import math
import time
import numpy as np
from PIL import Image

# Constant resize amount that will be used to shrink and expand image
RESIZE = 4

def main(file_location, palette_name, save_location):

    # Open palette choice
    with Image.open(f'static/palettes/{palette_name}') as palette:

        # Empty list for palette RGB values
        palette_list = []

        # Grab palette RGB values and append to list
        for x in range(palette.height):
            for y in range(palette.width):
                pixel = palette.get_pixel(x, y)
                palette_list.append(pixel)

    print(palette_list)

    # Open image choice
    with Image.open(file_location) as image:

        # Resize image to specified fraction of original
        image_resized = image.resize((image.width // RESIZE, image.height // RESIZE))

        # Set width and height variables for resized image for later use
        width, height = image_resized.size

        # Create new blank image
        pixel_image = Image.new('RGB', (width, height))

        # Call color_picker function for each pixel in resized target image
        for x in range(width):
            for y in range(height):
                pixel = color_picker(palette, image_resized.get_pixel(x, y))


        # Resize new pixel image
        pixel_image_resized = pixel_image.resize((width * RESIZE, height * RESIZE))

        # Save new image
        pixel_image_resized.save(save_location)


def color_picker(palette_list, pixel):
    """
    Take a pixel and a target palette of colors and find the color in the
    palette which is closet to the given pixel.  Return the palette color
    as an r, g, b value.
    """

    # Grab RGB values for target pixel
    r, g, b = pixel.red, pixel.green, pixel.blue

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
    main("static/images/landscape.jpg", "ammo8.png")
    print("------- %s seconds -------" % (time.time() - start_time))