import cv2
class ReadVideo:
    def __init__(self, name):
        self.name = name
        self.video = cv2.VideoCapture(name)
        self.width = round(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = round(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.fps = round(self.video.get(cv2.CAP_PROP_FPS))

    def get_frame(self, i):
        self.video.set(cv2.CAP_PROP_POS_FRAMES, round(i * self.fps))
        return self.video.read()

    def get_part_video(self, i):
        self.video.set(cv2.CAP_PROP_POS_FRAMES, round(i * self.fps))
        return self.video

class WriteVideo:
    def __init__(self, name, width, height, fps):
        self.name = name
        self.width = round(width)
        self.height = round(height)
        self.fps = round(fps)
        self.video = cv2.VideoWriter(name,cv2.VideoWriter_fourcc(*"DIVX"),fps,(self.width,self.height))

    def write_frame(self, frame):
        print(frame.shape)
        print(self.width,self.height)
        # assert(frame.shape[0]==self.width and frame.shape[1]==self.height)
        self.video.write(frame)
    
    def release(self):
        self.video.release()

    def get_part_video(self):
        return self.video

if (__name__ == "__main__"):
    pass


