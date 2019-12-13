import cv2
import numpy as np
import numpy as np
def ensemble_depth(depth):
    """
    input n * m
    output n * m * 3
    each 'pixel' is a (u, v, depth)
    """
    width, height = depth.shape
    ans = np.zeros((width, height, 3), dtype = np.float64)
    ans[:,:,2] = depth
    tmp = np.arange(width * height).reshape((width,height))
    ans[:,:,0] = tmp // height
    ans[:,:,1] = tmp % height
    return ans
    
    
def depth_to_3d(ens_depth, K):
    """
    ens_depth: ensembled depth n * m * 3
    K: camera param 3 * 3
    output: n * m * 3 (x, y, z)
    """
    K_inv = np.linalg.inv(K)
    ens_depth = np.array(ens_depth)
    ens_depth[:,:,:2] *= ens_depth[:,:,2:]
    output = np.matmul(ens_depth , K_inv.T)
    return output
    
def _3d_to_depth(xyz, K):
    """
    inverse of depth_to_3d
    """
    output = np.matmul(xyz, K.T)
    output[:,:,:2] /= output[:,:,2:]
    return output
    
    
    
if (__name__ == "__main__"):
    import sys
    img_dir = sys.argv[1]
    depth=np.load(img_dir + '/mega_depth.npy')
    #depthh=cv2.imread(r'mega_depth.png')
    w,h = depth.shape
    c=3
    #for i in range(0,w):
    #    for j in range(0,h):
    #        depthh[i,j,0]=1.0/depthh[i,j,0]
    #depth=1.0/depthh
    mask1=np.load(img_dir + '/masks.npy').astype(int)
    mask2=np.load(img_dir + '/rcnn/plane_masks.npy').astype(int)
    mask1 = cv2.resize(mask1,(mask2.shape[1], mask2.shape[0]))
    print(mask1.shape, mask2.shape)
    #mask=cv2.imread(r'0.png')
    depth=ensemble_depth(depth)
    print(depth.shape)
    print(mask1.shape)
    print(mask2.shape)
    xyz=depth_to_3d(depth,[[1,0,w//2],[0,1,h//2],[0,0,1]])
    f = open(img_dir + "/out.txt", "w") 
    print(w,h,file=f)
    for i in range(0,w):
        for j in range(0,h):
            print(mask1[i,j],file=f)
    for i in range(0,w):
        for j in range(0,h):
            print(int(mask2[i,j]),file=f)
    for i in range(0,w):
        for j in range(0,h):
            print(xyz[i,j,0],file=f)
    for i in range(0,w):
        for j in range(0,h):
            print(xyz[i,j,1],file=f)
    for i in range(0,w):
        for j in range(0,h):
            print(xyz[i,j,2]*100,file=f)
    f.close()