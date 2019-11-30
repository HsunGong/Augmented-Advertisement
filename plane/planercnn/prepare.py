from PIL import Image
import sys

im = Image.open(sys.argv[1])
width, height = im.size

with open(sys.argv[2], 'w') as f:
    f.write(f"587 587 {height/2} {width/2} {height} {width}") # f_x f_y(don't care), centre_x, centre_y, w, h