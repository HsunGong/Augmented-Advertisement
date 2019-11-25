from PIL import Image
import sys

im = Image.open(sys.argv[1])
width, height = im.size

with open(sys.argv[2], 'w') as f:
    f.write(f"587 587 320 240 {width} {height}")