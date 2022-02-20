import math
from PIL import Image

def main(file_location, palette_name):
    # Recieve user inputs for palette choice
    palette = Image.open(f'static/palettes/{palette_name}')

    # Resize image to 1/4 of original
    with Image.open(file_location) as image:
        (width, height) = (image.width // 4, image.height // 4)
        image_resized = image.resize((width, height))

        pixel_image = pixelate(image_resized, palette)


def pixelate(image, palette):
    """
    Function that replaces pixel from target image with pixel from a set color palette
    that closest resembles target  pixel and returns a copy of the image
    """

    # Get width and height
    width, height = image.size
    image_copy = Image.new('RGB', (width, height))

    for x in range(width):
        for y in range(height):
            old_pixel = image.getpixel((x, y))
            new_pixel = color_picker(old_pixel, palette)
            image_copy.putpixel((x, y), new_pixel)

    return image_copy


if __name__ == "__main__":
    main("static/images/landscape.jpg", "ammo8.png")