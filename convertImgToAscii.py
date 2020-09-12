from PIL import Image, ImageFilter
from argparse import ArgumentParser
import sys


def get_pixel_color_space_luminance(pixel):
    '''Get the pixels luminance

    Get the luminance of the given pixel using the color
    space luminance function.
    '''
    red, green, blue = pixel
    return (0.2126 * red + 0.7152 * green + 0.0722 * blue)


def get_pixel_perceived_luminance(pixel):
    '''Get the pixels luminance

    Get the luminance of the given pixel using the percieved
    luminance function.
    '''
    red, green, blue = pixel
    return (0.299 * red + 0.587 * green + 0.114 * blue)


def get_pixel_perceived_sqrt_luminance(pixel):
    '''Get the pixels luminance

    Get the luminance of the given pixel using the perceived_sqrt
    luminance function.
    '''
    red, green, blue = pixel
    return sqrt(0.299 * red^2 + 0.587 * green^2 + 0.114 * blue^2)


def get_pixel_luminance(luminance_func, pixel):
    '''Get the luminance of a pixel

    Get the luminance of the given pixel using the given luminance function
    from the input arguments to convert the pixel.
    '''

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
    '''Get the luminance of a pixel as a value between 1 and 0
    
    Use the given luminance function from the input arguments to get
    the luminance of the given pixel, and then give it a value between
    1 and 0 where 0 is no luminance and 1 is the luminance of the
    brightest possible pixel.
    '''
    luminance = get_pixel_luminance(luminance_func, pixel)
    max_luminance = get_pixel_luminance(luminance_func, max_pixel)

    return luminance / max_luminance


def get_luminance_char(ascii_atlas, luminance):
    '''Get the ascii character matching the given luminance best

    Get the ascii character from the given ascii atlas matching
    the given luminance best. The luminance should be between 1
    and 0.
    '''

    # Clamp luminance value within 1 to 0
    luminance = max(0, min(1, luminance))

    # Get luminance position in atlas
    atlas_pos = round(luminance * (len(ascii_atlas) - 1))

    # Return ascii character at position
    return ascii_atlas[atlas_pos]


if __name__ == "__main__":

    # Create argument parser
    parser = ArgumentParser(description="Convert a standart image into ascii art of said image.")

    # Required arguments
    parser.add_argument("filepath", type=str, help="The path to the input file")

    # Optional arguments
    parser.add_argument("-o", type=str, default="out", help="Path to output file")
    parser.add_argument("--luminance-func", choices=["color_space", "perceived", "perceived_sqrt"], help="Which function to use to calculate luminance. Can be: 'color_space', 'percieved', 'perceived_sqrt'")
    parser.add_argument("--ascii-atlas", type=str, default="$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ", help="Characters to represent different levels of luminance. Should go from darkest to brightest.")

    # Parse arguments
    args = parser.parse_args()

    # Load image
    raw_image = Image.open(sys.argv[1])
    raw_image_pixels = raw_image.load()
    raw_image_width, raw_image_height = raw_image.size

    # Log image data
    print("Image Data:")
    print(f"  Path: {sys.argv[1]}")
    print(f"  Width: {raw_image_width}")
    print(f"  Height: {raw_image_height}")
    print(f"    (size: {raw_image.size})")
    
    # Create output file
    with open(args.o, "w") as output_file:

        # Loop over image pixels
        for y in range(raw_image_height):
            for x in range(raw_image_width):
                # Get luminance of pixel
                pixel_luminance = get_pixel_luminance_1_0(args.luminance_func, raw_image_pixels[x, y], [255, 255, 255])
                
                # Get ascii character for luminance
                luminance_char = get_luminance_char(args.ascii_atlas, pixel_luminance)

                # Write luminance to output file
                output_file.write(luminance_char)

                print(luminance_char, end="")
    
            # Write newline
            output_file.write("\n")
            print()

