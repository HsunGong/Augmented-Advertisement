# Copyright (c) Group Three-Forest SJTU. All Rights Reserved. 

from tracking.tracking import *

# a = tracking_video_rectangle("video/","1.mp4",[[273,352],[266,616],[412,620],[416,369]])
a = tracking_video_rectangle_tovideo("video/","1.mp4", "1.png", [[273,352],[266,616],[412,620],[416,369]], result = 'result__.avi', method_num = 5, edge = 4, middle_halt = 250)
