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


if __name__ == "__main__":
    main("static/images/landscape.jpg", "ammo8.png")