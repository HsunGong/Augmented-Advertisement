# Copyright (c) Group Three-Forest SJTU. All Rights Reserved. 
import cv2
from tracking import tracking_video_rectangle_tovideo
from tracking import sup_tracking_video_standard
import sys
sys.path.append('/mnt/lustre/sjtu/home/xg000/cv/')
from utils.video import ReadVideo, WriteVideo
from utils.utils import Trans_forward,get_k_mat
import numpy as np
# a = tracking_video_rectangle("video/","1.mp4",[[273,352],[266,616],[412,620],[416,369]])

# video_in = ReadVideo("1.mp4")
# video_out = WriteVideo("result.mp4", video_in.width, video_in.height, video_in.fps)

# a = tracking_video_rectangle_tovideo("video/","1.mp4", "1.png", [[273,352],[266,616],[412,620],[416,369]], result = 'result__.avi', method_num = 5, edge = 4, middle_halt = 250)
points = np.array([1016, 141, 979, 468, 343, 115, 338, 456]).reshape((4,2))
points = np.array([1016, 141, 979, 468, 343, 115, 338, 456]).reshape((4,2))
pointx = points[:,0]
pointy = points[:,1]
points[:,0] = pointy
points[:,1] = pointx
# points = np.array([[273,352],[266,616],[412,620],[416,369]])

# li = []
# for i in range(points.shape[0]):
    # li.append(tracking_video_standard(ReadVideo("video/part_video.mp4"),points[i]))
ans = sup_tracking_video_standard(ReadVideo("demo/video/main.mp4"),points,save_img=True)
np.save(f"tmp{points[0,0]}.npy",ans)
ans = np.load(f"tmp{points[0,0]}.npy", allow_pickle=True)

video_in = ReadVideo("demo/video/main.mp4")
adver_video = ReadVideo("demo/video/ad3.mp4")
video_out = WriteVideo("demo/video/aug.mp4",video_in.width,video_in.height,video_in.fps)
for i in range(ans.shape[1]):
    xld,yld,xlu,ylu,xrd,yrd,xru,yru=ans[:,i,:].reshape(-1)
    b = np.array([[yru,xru],[yrd,xrd],[yld,xld],[ylu,xlu]], dtype = np.float32)
    # b = ans[:,i,:]
    im = Trans_forward(video_in.video.read()[1],b, adver_video.video.read()[1],.2)
    print("step ",i)
    video_out.video.write(im)

video_out.release()