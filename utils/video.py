import cv2
class ReadVideo:
    def __init__(self, name):
        self.name = name
        self.video = cv2.VideoCapture(name)
        self.width = self.video.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.fps = self.video.get(cv2.CAP_PROP_FPS)

    def get_frame(self, i):
        self.video.set(cv2.CAP_PROP_POS_FRAMES, round(i * self.fps))
        return self.video.read()

    def get_part_video(self, i):
        self.video.set(cv2.CAP_PROP_POS_FRAMES, round(i * self.fps))
        return self.video

class WriteVideo:
    def __init__(self, name, width, height, fps):
        self.name = name
        self.width = width
        self.height = height
        self.fps = fps
        self.video = cv2.VideoWriter(name,cv2.VideoWriter_fourcc(*"DIVX"),fps,(self.width,self.height))

    def write_frame(self, frame):
        self.video.write(frame)
    
    def release(self):
        self.video.release()

    def get_part_video(self):
        return self.video

if (__name__ == "__main__"):
    pass


