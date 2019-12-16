from video import *
import cv2

# f = ReadVideo("demo/video/main.mov")
# print('demo/img')
# cv2.imwrite('demo/img/img.png', f.get_frame(0)[1])
# fout = WriteVideo("demo/video/main.mp4",width = f.height, height = f.width, fps = f.fps)
# ok,frame = f.video.read()
# while (ok):
#     fout.write_frame(frame.swapaxes(1,0))
#     ok,frame = f.video.read()
#     # print(frame.shape)
# fout.release()

f = ReadVideo("demo/video/main.mp4")
print('demo/img')
cv2.imwrite('demo/img/img.png', f.get_frame(0)[1])
