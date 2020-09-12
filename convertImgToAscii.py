from PIL import Image, ImageFilter
from argparse import ArgumentParser
import sys

def get_pixel_color_space_luminance(pixel):
    red, green, blue = pixel
    return (0.2126 * red + 0.7152 * green + 0.0722 * blue)

def get_pixel_perceived_luminance(pixel):
    red, green, blue = pixel
    return (0.299 * red + 0.587 * green + 0.114 * blue)

def get_pixel_perceived_sqrt_luminance(pixel):
    red, green, blue = pixel
    return sqrt(0.299 * red^2 + 0.587 * green^2 + 0.114 * blue^2)

def get_pixel_luminance(luminance_func, pixel):
    if luminance_func == "color_space":
        return get_pixel_color_space_luminance(pixel)
    elif luminance_func == "perceived":
        return get_pixel_perceived_luminance(pixel)
    elif luminance_func == "perceived_sqrt":
        return get_pixel_perceived_sqrt_luminance(pixel)
    else:
        print("ERROR: Cannot recognice given luminance function argument")
        sys.exit(-1)

def get_pixel_luminance_1_0(luminance_func, pixel, max_pixel):
    luminance = get_pixel_luminance(luminance_func, pixel)
    max_luminance = get_pixel_luminance(luminance_func, max_pixel)

    return luminance / max_luminance

# Create argument parser
parser = ArgumentParser(description="Convert a standart image into ascii art of said image.")

# Required arguments
parser.add_argument("filepath", type=str, help="The path to the input file")

# Optional arguments
parser.add_argument("-o", type=str, default="out", help="Path to output file")
parser.add_argument("--luminance-func", choices=["color_space", "perceived", "perceived_sqrt"], help="Which function to use to calculate luminance. Can be: 'color_space', 'percieved', 'perceived_sqrt'")

# Parse arguments
args = parser.parse_args()

# Load image
raw_image = Image.open(sys.argv[1])
raw_image_pixels = raw_image.load()
raw_image_width, raw_image_height = raw_image.size

print("Image Data:")
print(f"  Path: {sys.argv[1]}")
print(f"  Width: {raw_image_width}")
print(f"  Height: {raw_image_height}")
print(f"    (size: {raw_image.size})")

# Loop over image pixels
for y in range(raw_image_height):
    for x in range(raw_image_width):
        pixel_luminance = get_pixel_luminance_1_0(args.luminance_func, raw_image_pixels[x, y], [255, 255, 255])
        print(pixel_luminance, end=" ")

    print() # Newline
