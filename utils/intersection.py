import cv2
import argparse

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument('pic1', type=str, default='pic.png', help='read pic name')
#     parser.add_argument('pic2', type=str, default='pic.png', help='read pic name')
#     parser.add_argument('dir', type=str, default='tmp')

#     args = parser.parse_args()


#     pic1 = cv2.imread(args.pic1) # not active part set to zero
#     pic2 = cv2.imread(args.pic2)

#     import os.path as p
#     args.pic1 = p.basename(args.pic1)
#     args.pic2 = p.basename(args.pic2)

#     out = pic1 * pic2
#     cv2.imwrite(args.dir + '/' + args.pic1 + '_' + args.pic2 + '.png', out)
import os
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--pic1', type=str, default='seg', help='read pic name')
    parser.add_argument('--pic2', type=str, default='plane', help='read pic name')
    parser.add_argument('--dir', type=str, default='tmp')

    args = parser.parse_args()
    import os.path as p
    import time
    t = time.clock()
    for root1, _, files1 in os.walk(args.pic1):
        for p1 in files1:
            if p.splitext(p1)[1] != '.png':
                continue
            for root2, _, files2 in os.walk(args.pic2):
                for p2 in files2:
                    if p.splitext(p2)[1] != '.png' :
                        continue
                    pic1 = cv2.imread(root1 + '/' + p1) # not active part set to zero
                    pic2 = cv2.imread(root2 + '/' + p2)
                    h = max(pic1.shape[0], pic2.shape[0])
                    w = max(pic1.shape[1], pic2.shape[1])
                    out = cv2.resize(pic1, (w, h)) * cv2.resize(pic2, (w,h))
                    import numpy as np
                    out = out.astype(np.uint8)
                    if np.all(out == 0):
                        continue
                    print(p.splitext(p1)[0] + '_' + p.splitext(p2)[0], out[out != 0].shape)
                    # print(args.dir + '/' + p.splitext(p1)[0] + '_' + p.splitext(p2)[0] + '.png')
                    # from skimage import io
                    # tran = np.ones((h,w,1)) * 0.8
                    # out = np.concatenate((out, tran), axis=2).astype(np.uint8)
                    # # out = np.transpose(out, (2,0,1)).astype(np.uint8)
                    out = np.concatenate((out, 255+np.zeros((h,w,1), dtype=np.uint8)), axis=2)
                    # out[out == np.equal([[[0,0,0,255]]])] = np.array([[[0,0,0,0]]])
                    for x in range(h):
                        for y in range(w):
                            if out[x, y,3] == 255:
                                out[x, y,3] = 0

                    from PIL import Image
                    out = Image.fromarray(out.astype(np.uint8))
                    out = Image.blend(Image.new('RGBA', out.size, (0,0,0,100)), out, 1)

                    out.save(args.dir + '/' + p.splitext(p1)[0] + '_' + p.splitext(p2)[0] + '.png')
    print(time.clock() - t)