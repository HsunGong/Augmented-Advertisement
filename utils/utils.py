import cv2
import numpy as np
import math
# def 
"""
Usage:
    getTrans(srcPoints, destPoints)
    srcPoints [4,2]
    destPoints [4,2]
    output [3,3]
        All np.float32
    
getTrans(a,b)
"""
getTrans = cv2.getPerspectiveTransform

"""
Usage:
    Trans_into(srcPic, transMat, shape)
    srcPic [W,H,3]
    transMat [3,3] from getTrans()
    shape: dest shape (W1,H1)
        All np.array
"""
Trans_into = cv2.warpPerspective

"""
Usage 
    Trans_forward(im, rect, ad)
    im : Image, np.uint8
    rect : Rectangle area to put the advertisement in the Image, np.float32
    ad : Advertisement, np.uint8
    k : transparency (of ad) 0 to 1. 
"""
def Trans_forward(im, rect, ad, k=.2):
    # im = im.astype(np.uint8)
    # ad = ad.astype(np.uint8)
    rect = np.array(rect,np.float32)
    w,h,_ = ad.shape
    iw, ih, _ = im.shape
    standart_rect = np.array([[0, 0], [0, w], [h, w], [h, 0]] , dtype = np.float32)
    blank = (np.ones(ad.shape, dtype = np.float16) * (1-k) * 255).astype(np.uint8)
    trans = getTrans(standart_rect, rect) 
    blank_tran = np.ones((1,), dtype = np.uint8) - Trans_into(blank, trans, (ih, iw)).astype(np.float16)/255
    im = im * blank_tran
    ad_tran = Trans_into((ad * (1-k)).astype(np.uint8), trans, (ih,iw))
    return np.array(im+ad_tran, dtype = np.uint8)

def get_k_mat(im_shape, k = 12, m = 10):
    w, h, _ = im_shape
    a = np.arange(w*h, dtype = np.int64).reshape((w,h))
    uv = np.zeros((w,h,2), dtype = np.float32)
    
    uv[:,:,0] = a // h
    uv[:,:,1] = a  % h
    
    cen = np.array(((w-1)/2,(h-1)/2),dtype = np.float32)
    dist = uv - cen.reshape((1,1,2))
    dist = dist*dist
    dist = dist[:,:,0]+dist[:,:,1]
    #dist = np.sqrt(dist)
    #dist = dist / math.sqrt(w*h) 
    dist = dist / np.max(dist) * k
    k = np.maximum(1/(np.exp(-dist)+1) .reshape((w,h,1))*m-(m-1),0)
    
    return k
    

if (__name__ == "__main__"):
    import sys,os
    img_dir = sys.argv[1]
    print(img_dir)
    im = cv2.imread(img_dir + '/img.png').astype(np.uint8)
    ad = cv2.imread(img_dir + '/ad.png').astype(np.uint8)
    w,h,c = im.shape

    bs = np.loadtxt(img_dir + '/process.txt').astype(np.float32) # 
    os.system('mkdir -p ' + img_dir + '/aug')
    for row in range(bs.shape[0]):
        xld,yld,xlu,ylu,xrd,yrd,xru,yru=bs[row,:]
        b = np.array([[yru,xru],[yrd,xrd],[yld,xld],[ylu,xlu]], dtype = np.float32)
        r = Trans_forward(im,b,ad)
        cv2.imwrite(img_dir + f'/aug/{row}.png', r)

    # bs = np.array([1016, 141, 979, 468, 343, 115, 338, 456]).astype(np.float32) # 
    # # m = getTrans(a,b)
    # xld,yld,xlu,ylu,xrd,yrd,xru,yru=bs
    # b = np.array([[yru,xru],[yrd,xrd],[yld,xld],[ylu,xlu]], dtype = np.float32)
    # r = Trans_forward(im,b,ad)
    # cv2.imwrite('tmp.png', r)