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


def get_grid_average(x, y, file_location):
    """
    Function that takes in an x and y coordinate for a pixel on an image and
    returns the average of the colors of a range that is a 4x4 grid starting at that coordinate.
    """

    # Initialize empty lists for RGB values
    red = []
    green = []
    blue = []

    # Open and load image
    image = Image.open(file_location)
    pixels = image.load()

    # Create counter for use in determining average pixel colors
    counter = 0

    # For each 4x4 grid obtain the pixel and then add the RGB values to lists
    for i in range(x, x + 4):
        for j in range(y, y + 4):
            pixel_r, pixel_g, pixel_b = pixels[i, j]
            red.append(pixel_r)
            green.append(pixel_g)
            blue.append(pixel_b)
            counter += 1

    # Get average of each RGB value and return that average as a pixel
    return int(sum(red) / counter), int(sum(green) / counter), int(sum(blue) / counter)


if __name__ == "__main__":
    main("static/images/landscape.jpg", "ammo8.png")