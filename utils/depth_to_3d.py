import numpy as np
def ensemble_depth(depth):
    """
    input n * m
    output n * m * 3
    each 'pixel' is a (u, v, depth)
    """
    width, height = depth.shape
    ans = np.zeros((width, height, 3), dtype = np.float32)
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
    
    
    