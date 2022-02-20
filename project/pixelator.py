import math
from PIL import Image

def main(file_location, palette_name):

    # Convert image to jpg? Test code with png?

    # Resize image to 1/4 of original
    with Image.open(file_location) as image:
        image_resized = image.resize((image.width // 4, image.height // 4))

        width, height = image_resized.size

        pixel_image = Image.new('RGB', (width, height))

        for x in range(width):
            for y in range(height):
                r, g, b = image_resized.getpixel((x, y))
                #new_pixel =
                color_picker(r, g, b, palette_name)
                #pixel_image.putpixel((x, y), new_pixel)


def color_picker(r, g, b, palette_name):
    """
    Take a pixel and a target palette of colors and find the color in the
    palette which is closet to the given pixel.  Return the palette color
    as an r, g, b value.
    """

    # Empty lists for palette values and distances
    palette_list = []
    distance_list = []

    # Obtain all RGB values for colors in chosen palette
    with Image.open(f'static/palettes/{palette_name}') as palette:
        for x in range(palette.width):
            for y in range(palette.height):
                r, g, b = palette.getpixel((x, y))
                rgb_list = [r, g, b]
                palette_list.append(rgb_list)

    print(palette_list)



if __name__ == "__main__":
    main("static/images/landscape.jpg", "ammo8.png")