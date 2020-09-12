from PIL import Image, ImageFilter
import sys

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
        print(x * y + x, end="")

    print() # Newline
