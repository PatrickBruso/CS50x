import math
from PIL import Image

def main(file_location, palette_name):
    # Recieve user inputs for palette choice
    palette = Image.open(f'static/palettes/{palette_name}')

    # Call shrink function on image and save result to copy
    image_copy = shrink(file_location)
    image_copy.save("shrunk.jpg")


def shrink(file_location):
    """
    Take an image and return a copy of that image that is reduced by 4 times.
    Each 4x4 grid of pixels in the original image will be 1 pixel in the new image
    that is the average color from the 4x4 grid.
    """

    # Open image provided
    image = Image.open(file_location)

    # Obtain width and height for target image
    width, height = image.size

    # Create blank image copy that is 4 times smaller than original
    image_copy = Image.new('RGB', (image.width // 4, image.height //4))

    # Set original coordinates and coordinates for image copy
    orig_x = 0
    orig_y = 0
    new_x = 0
    new_y = 0

    # Loop through x and y coords of original picture
    while orig_y < height - 2:
        while orig_x < width - 2:
            # Image copy is created using the average of the 4x4 pixel grid from original
            image_copy.putpixel((new_x, new_y), get_grid_average(orig_x, orig_y, file_location))
            new_x += 1
            orig_x += 4
        orig_x = 0
        new_x = 0
        new_y += 1
        orig_y += 4

    # Return copy of image
    return image_copy