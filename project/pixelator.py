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

    for new_pixel in image_copy:
        x = new_pixel.x
        y = new_pixel.y
        old_pixel = image.get_pixel(x, y)
        palette_color = color_picker(old_pixel, palette)
        new_pixel.red = palette_color[0]
        new_pixel.green = palette_color[1]
        new_pixel.blue = palette_color[2]
        image_copy.set_pixel(x, y, new_pixel)

    return image_copy


if __name__ == "__main__":
    main("static/images/landscape.jpg", "ammo8.png")