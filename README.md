# Image to ASCII art Converter

A python script to convert an image to ascii art

## Getting started

### Dependencies

This is a python project, so to use it you need python version 3.

To get it, go to [python.org](https://www.python.org/downloads/) and download it.

With python installed, make sure to install the required python libraries

- Pillow
- Argparse

### Installation

Clone repo to your computer

```
git clone https://github.com/The339Agent/ConvertImageToAscii.git
```

Here, as long as you have the convertImgToAscii.py file, you have all you need (+ the project dependencies)

### Usage

To convert an image to ascii art, you have to first have an image you want to convert into ascii art. In this example, that file will be refered to `img.png` (the file does not have to be an .png file).

To get the argument options, do `python convertImgToAscii.py --help`. The same options will be in this README.

----------------------------------------------------------------------------------------------------
| Option   | Hint                        | Example                                                 |
----------------------------------------------------------------------------------------------------
| filepath         | The path to the input file  | `python convertImgToAscii.py img.png`           |
| -o               | The path to the output file | `python convertImgToAscii.py img.png -o output` |
| -shric-scale     | The factor to shrinc the image by               | `python convertImgToAscii.py img.png -shrinc-scale 10`             |
| --luminance-func | The method to get the luminance of a pixel with | `python convertImgToAscii.py img.png --luminance-func color_space` |
| --ascii-atlas    | The characters to represent different levels of luminance | `python convertImgToAscii.png img.png --ascii-atlas $H*~,. ` |

