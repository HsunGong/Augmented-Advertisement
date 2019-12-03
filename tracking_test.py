# Copyright (c) Group Three-Forest SJTU. All Rights Reserved. 
import cv2
from tracking.tracking import tracking_video_rectangle_tovideo
from utils.video import ReadVideo, WriteVideo
# a = tracking_video_rectangle("video/","1.mp4",[[273,352],[266,616],[412,620],[416,369]])

video_in = ReadVideo("1.mp4")
video_out = WriteVideo("result.mp4", video_in.width, video_in.height, video_in.fps)

a = tracking_video_rectangle_tovideo("video/","1.mp4", "1.png", [[273,352],[266,616],[412,620],[416,369]], result = 'result__.avi', method_num = 5, edge = 4, middle_halt = 250)
