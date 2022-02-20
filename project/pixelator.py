import math
from PIL import Image

def main(file_location, palette_name):
    # Recieve user inputs for palette choice
    palette = Image.open(f'static/palettes/{palette_name}')

    # Resize image to 1/4 of original
    with Image.open(file_location) as image:
        image_resized = image.resize((image.width // 4, image.height // 4))

        pixel_image = Image.new('RGB', (image.width, image.height))

        for x in range(image.width):
            for y in range(image.height):
                old_pixel = image.getpixel((x, y))
                new_pixel = color_picker(old_pixel, palette)
                pixel_image.putpixel((x, y), new_pixel)


if __name__ == "__main__":
    main("static/images/landscape.jpg", "ammo8.png")