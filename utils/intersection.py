import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('pic1', type=str, default='pic.png', help='read pic name')
parser.add_argument('pic2', type=str, default='pic.png', help='read pic name')
parser.add_argument('dir', type=str, default='tmp')

args = parser.parse_args()


pic1 = cv2.imread(args.pic1) # not active part set to zero
pic2 = cv2.imread(args.pic2)

import os.path as p
args.pic1 = p.basename(args.pic1)
args.pic2 = p.basename(args.pic2)

out = pic1 * pic2
cv2.imwrite(args.dir + '/' + args.pic1 + '_' + args.pic1 + '.png', out)