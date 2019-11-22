import cv2
import numpy as np
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
    clockwise
    
    
"""
def Trans_forward(im, rect, ad):
    w,h,_ = ad.shape
    iw, ih, _ = im.shape
    standart_rect = np.array([[0, 0], [0, w], [h, w], [h, 0]] , dtype = np.float32)
    blank = np.ones(ad.shape, dtype = np.uint8)
    trans = getTrans(standart_rect, rect)
    blank_tran = np.ones((1,), dtype = np.uint8) - Trans_into(blank, trans, (ih, iw))
    im = im * blank_tran
    ad_tran = Trans_into(ad, trans, (ih,iw))
    return im+ad_tran


if (__name__ == "__main__"):
    im = cv2.imread(r'img.jpg')
    ad = cv2.imread(r'1.png')
    w,h,c = im.shape
    a = np.array([[0,0],[0,w-1],[h-1,0],[h-1,w-1]], dtype = np.float32)
    b = np.array([[h/10,w/10],[0,w/3],[h/2,w/2],[h/3,0]], dtype = np.float32)
    # m = getTrans(a,b)
    r = Trans_forward(im,b,ad)

    cv2.imwrite(r'saved.jpg',r)



    '''
    im = cv2.imread(r'img.jpg')
    w,h,c = im.shape
    a = np.array([[0,0],[0,w-1],[h-1,0],[h-1,w-1]], dtype = np.float32)
    b = np.array([[0,0],[0,500],[1000,0],[1000,1000]], dtype = np.float32)
    m = getTrans(a,b)
    r = Trans_into(im,m,(1000,1000))

    cv2.imwrite(r'saved.jpg',r)
    '''


    """
    im = np.ones((5,5),np.float32)

    """