import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('pic', type=str, default='pic.png', help='read pic name')
parser.add_argument('dir', type=str, default='tmp')

args = parser.parse_args()

pic = cv2.imread(args.pic)

num = set()
for r in pic:
    for pixel in r:
        print(pixel)
        num.add(pixel)

for n in num:
    pic_new = pic
    pic_new[pic_new != n] = 0
    cv2.imwrite(args.dir + '/' + str(n) + '.png')