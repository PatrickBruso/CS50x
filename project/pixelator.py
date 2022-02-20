import math
import numpy as np
from PIL import Image

def main(file_location, palette_name):

    # Convert image to jpg? Test code with png?

    # Obtain list of RGB values for palette using numpy array
    with Image.open(f'static/palettes/{palette_name}') as palette:
        array = np.array(palette.convert('RGB'))
        colors = np.unique(array.reshape(-1, 3), axis=0) # Not sure i want to use unique (that may remove duplicate colors)
        test = array.reshape(-1, 3) # Same output as above but not unique

    for list in test:
        print(list)

    r, g, b = colors[0]
    print(r)
    print(g)
    print(b)

    # use for color in colors to compare pixel RGB values to each color in palette

    """ What if we turned the palette and image into numpy arrays and then
    did the calculation on each (for color in image_colors) to get image pixel RGB
    and then compare that to each palette RGB to find closest.  Then you can just convert
    the new array of pixels into a PIL image"""

    # Resize image to 1/4 of original
    with Image.open(file_location) as image:
        image_resized = image.resize((image.width // 4, image.height // 4))

        width, height = image_resized.size

        pixel_image = Image.new('RGB', (width, height))

        for x in range(width):
            for y in range(height):
                r, g, b = image_resized.getpixel((x, y))
                #new_pixel = color_picker(r, g, b, palette_name)
                #pixel_image.putpixel((x, y), new_pixel)


def color_picker(r, g, b, palette_name):
    """
    Take a pixel and a target palette of colors and find the color in the
    palette which is closet to the given pixel.  Return the palette color
    as an r, g, b value.
    """

    # Empty lists for palette values and distances
    #palette_list = []
    #distance_list = []

    # Obtain all RGB values for colors in chosen palette
    with Image.open(f'static/palettes/{palette_name}') as palette:
        palette_list = palette.getpalette()
        print(palette_list)

        # Obtain list of RGB values for palette
        array = np.array(palette.convert('RGB'))
        colors = np.unique(array.reshape(-1, 3), axis=0)
        print(colors)


        """
        for x in range(palette.width):
            for y in range(palette.height):
                r, g, b = palette.getpixel((x, y))
                rgb_list = [r, g, b]
                palette_list.append(rgb_list)

    print(palette_list)"""



if __name__ == "__main__":
    main("static/images/landscape.jpg", "ammo8.png")