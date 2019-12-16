# Copyright (c) Group Three-Forest SJTU. All Rights Reserved. 

import cv2
import sys
from os.path import join
import numpy as np
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
from utils.utils import *
from utils.video import *

def tracking_video(root, name, point, edge = 20, save_img = True):
    # Set up tracker.
    # Instead of MIL, you can also use
    tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'CSRT', 'MOSSE']
    tracker_type = tracker_types[5]

    if int(minor_ver) >= 3:
        tracker = cv2.Tracker_create(tracker_type)
    else:
        if tracker_type == 'BOOSTING':
            tracker = cv2.TrackerBoosting_create()
        if tracker_type == 'MIL':
            tracker = cv2.TrackerMIL_create()
        if tracker_type == 'KCF':
            tracker = cv2.TrackerKCF_create()
        if tracker_type == 'TLD':
            tracker = cv2.TrackerTLD_create()
        if tracker_type == 'MEDIANFLOW':
            tracker = cv2.TrackerMedianFlow_create()
        if tracker_type == 'CSRT':
            tracker = cv2.TrackerCSRT_create()
        if tracker_type == 'MOSSE':
            tracker = cv2.TrackerMOSSE_create()

    # Read video
    video = cv2.VideoCapture(join(root, name))

    # Exit if video not opened.
    if not video.isOpened():
        print("Could not open video")
        sys.exit()

    # Read first frame.
    ok, frame = video.read()
    if not ok:
        print('Cannot read video file')
        sys.exit()
    cv2.imwrite("result/%05d.jpg"%(0),frame)
    # Define an initial bounding box
    bbox = (point[0] - edge, point[1] - edge, edge*2 , edge*2)

    # Uncomment the line below to select a different bounding box
    # bbox = cv2.selectROI(frame, False)

    # Initialize tracker with first frame and bounding box
    ok = tracker.init(frame, bbox)
    
    ans = []
    index_ = 0
    while True:
        # Read a new frame
        index_ += 1
        ok, frame = video.read()
        if not ok:
            break
         
        # Start timer
        timer = cv2.getTickCount()

        # Update tracker
        ok, bbox = tracker.update(frame)

        # Calculate Frames per second (FPS)
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);

        # Draw bounding box
        if ok:
            # Tracking success
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            p3 = (int(bbox[0] + bbox[2]/2), int(bbox[1] + bbox[3]/2))
            ans.append(p3)
            if (save_img):
                cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
        else :
            # Tracking failure
            if (save_img):
                cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)

        if (save_img):
            # Display tracker type on frame
            cv2.putText(frame, tracker_type + " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);

            # Display FPS on frame
            cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);

            # Display result
            cv2.imwrite("result/%05d.jpg"%(index_) , frame)
        # Exit if ESC pressed
        k = cv2.waitKey(1) & 0xff
        if k == 27 : break
    return np.array(ans)

def tracking_video_standard(video, point, edge = 20, save_img = False):
    # Set up tracker.
    # video = ReadVideo("1.mp4")
    assert(isinstance(video, ReadVideo))
    
    # Instead of MIL, you can also use
    tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'CSRT', 'MOSSE']
    tracker_type = tracker_types[5]

    if int(minor_ver) >= 3:
        tracker = cv2.Tracker_create(tracker_type)
    else:
        if tracker_type == 'BOOSTING':
            tracker = cv2.TrackerBoosting_create()
        if tracker_type == 'MIL':
            tracker = cv2.TrackerMIL_create()
        if tracker_type == 'KCF':
            tracker = cv2.TrackerKCF_create()
        if tracker_type == 'TLD':
            tracker = cv2.TrackerTLD_create()
        if tracker_type == 'MEDIANFLOW':
            tracker = cv2.TrackerMedianFlow_create()
        if tracker_type == 'CSRT':
            tracker = cv2.TrackerCSRT_create()
        if tracker_type == 'MOSSE':
            tracker = cv2.TrackerMOSSE_create()

    # Read video
    # video = cv2.VideoCapture(join(root, name))

    # Exit if video not opened.
    if not video.video.isOpened():
        print("Could not open video")
        sys.exit()

    # Read first frame.
    ok, frame = video.video.read()
    if not ok:
        print('Cannot read video file')
        sys.exit()
    cv2.imwrite("result/%05d.jpg"%(0),frame)
    # Define an initial bounding box
    bbox = (point[0] - edge, point[1] - edge, edge*2 , edge*2)

    # Uncomment the line below to select a different bounding box
    # bbox = cv2.selectROI(frame, False)

    # Initialize tracker with first frame and bounding box
    ok = tracker.init(frame, bbox)
    
    ans = [point]
    index_ = 0
    while True:
        # Read a new frame
        index_ += 1
        print(index_)
        ok, frame = video.video.read()
        if not ok:
            break
         
        # Start timer
        timer = cv2.getTickCount()

        # Update tracker
        ok, bbox = tracker.update(frame)

        # Calculate Frames per second (FPS)
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

        # Draw bounding box
        if ok:
            # Tracking success
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            p3 = (int(bbox[0] + bbox[2]/2), int(bbox[1] + bbox[3]/2))
            ans.append(p3)
            if (save_img):
                cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
        else :
            # Tracking failure
            if (save_img):
                cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)

        if (save_img):
            # Display tracker type on frame
            cv2.putText(frame, tracker_type + " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);

            # Display FPS on frame
            cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);

            # Display result
            cv2.imwrite("result/%05d.jpg"%(index_) , frame)
        # Exit if ESC pressed
        k = cv2.waitKey(1) & 0xff
        if k == 27 : break
    return np.array(ans)

def sup_tracking_video_standard(video, points, edge = 20, save_img = False, position = 0):
    ans = []
    # video = ReadVideo("")
    length = 100000000
    for i in range(points.shape[0]):
        video.get_part_video(position)
        ans.append(tracking_video_standard(video, points[i],edge , save_img))
        length = min(length, ans[i].shape[0])
        # print(ans)
    for i in range(points.shape[0]):
        ans[i] = ans[i][0:length].reshape((1,length,2))
    ans = np.concatenate(ans)
    return ans

        

def tracking_video_rectangle(root, name, ad_name, point, edge = 20, save_img = False, save_result = True):
    # Set up tracker.
    # Instead of MIL, you can also use
    tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'CSRT', 'MOSSE']
    tracker_type = tracker_types[5]
    
    ad = cv2.imread(join(root,ad_name))
    
    if int(minor_ver) >= 3:
        tracker = [cv2.Tracker_create(tracker_type) for _ in range(4)]
    else:
        if tracker_type == 'BOOSTING':
            tracker = [cv2.TrackerBoosting_create() for _ in range(4)]
        if tracker_type == 'MIL':
            tracker = [cv2.TrackerMIL_create() for _ in range(4)]
        if tracker_type == 'KCF':
            tracker = [cv2.TrackerKCF_create() for _ in range(4)]
        if tracker_type == 'TLD':
            tracker = [cv2.TrackerTLD_create() for _ in range(4)]
        if tracker_type == 'MEDIANFLOW':
            tracker = [cv2.TrackerMedianFlow_create() for _ in range(4)]
        if tracker_type == 'CSRT':
            tracker = [cv2.TrackerCSRT_create() for _ in range(4)]
        if tracker_type == 'MOSSE':
            tracker = [cv2.TrackerMOSSE_create() for _ in range(4)]

    # Read video
    video = cv2.VideoCapture(join(root, name))

    # Exit if video not opened.
    if not video.isOpened():
        print("Could not open video")
        sys.exit()

    # Read first frame.
    ok, frame = video.read()
    if not ok:
        print('Cannot read video file')
        sys.exit()
    cv2.imwrite("result/%05d.jpg"%(0),frame)
    # Define an initial bounding box
    bbox = [(point[_][0] - edge, point[_][1] - edge, edge*2 , edge*2) for _ in range(4)]
    
    # Uncomment the line below to select a different bounding box
    # bbox = cv2.selectROI(frame, False)

    # Initialize tracker with first frame and bounding box
    for _ in range(4):
        ok = tracker[_].init(frame, bbox[_])
    
    
    index_ = 0
    while True:
        # Read a new frame
        index_ += 1
        ok, frame = video.read()
        if not ok:
            break
         
        # Start timer
        timer = cv2.getTickCount()

        
        ans = []
        for _ in range(4):
            # Update tracker
            ok, bbox = tracker[_].update(frame)
            # Calculate Frames per second (FPS)
            # fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
            # Draw bounding box
            if ok:
                # Tracking success
                p1 = (int(bbox[0]), int(bbox[1]))
                p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
                p3 = (int(bbox[0] + bbox[2]/2), int(bbox[1] + bbox[3]/2))
                ans.append(p3)
                if (save_img):
                    cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
            else :
                # Tracking failure
                if (save_img):
                    cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)

            if (save_img):
                # Display tracker type on frame
                cv2.putText(frame, tracker_type + " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);

                # Display FPS on frame
                # cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);

                # Display result
                cv2.imwrite("result/%05d_%d.jpg"%(index_, _) , frame)
        if (save_result):
            frame = Trans_forward(frame, np.array(ans , dtype = np.float32), ad)
            cv2.imwrite("result/%05d_%d.jpg"%(index_, 9) , frame)
        # Exit if ESC pressed
        k = cv2.waitKey(1) & 0xff
        if k == 27 : break
    return np.array(ans)

def tracking_video_rectangle_tovideo(root, name, ad_name, point, result = 'cool_project.avi', edge = 20, save_img = False, save_result = True, method_num = 5, save_img2 = True, middle_halt = -1):
    # Set up tracker.
    # Instead of MIL, you can also use
    tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'CSRT', 'MOSSE']
    tracker_type = tracker_types[method_num]
    
    ad = cv2.imread(join(root,ad_name))
    
    if int(minor_ver) >= 3:
        tracker = [cv2.Tracker_create(tracker_type) for _ in range(4)]
    else:
        if tracker_type == 'BOOSTING':
            tracker = [cv2.TrackerBoosting_create() for _ in range(4)]
        if tracker_type == 'MIL':
            tracker = [cv2.TrackerMIL_create() for _ in range(4)]
        if tracker_type == 'KCF':
            tracker = [cv2.TrackerKCF_create() for _ in range(4)]
        if tracker_type == 'TLD':
            tracker = [cv2.TrackerTLD_create() for _ in range(4)]
        if tracker_type == 'MEDIANFLOW':
            tracker = [cv2.TrackerMedianFlow_create() for _ in range(4)]
        if tracker_type == 'CSRT':
            tracker = [cv2.TrackerCSRT_create() for _ in range(4)]
        if tracker_type == 'MOSSE':
            tracker = [cv2.TrackerMOSSE_create() for _ in range(4)]

    # Read video
    video = cv2.VideoCapture(join(root, name))

    # Exit if video not opened.
    if not video.isOpened():
        print("Could not open video")
        sys.exit()

    # Read first frame.
    ok, frame = video.read()
    if not ok:
        print('Cannot read video file')
        sys.exit()
    cv2.imwrite("result/%05d.jpg"%(0),frame)
    out = cv2.VideoWriter(result , cv2.VideoWriter_fourcc(*'DIVX'), 10, (frame.shape[1],frame.shape[0]))
    
    # Define an initial bounding box
    bbox = [(point[_][0] - edge, point[_][1] - edge, edge*2 , edge*2) for _ in range(4)]
    
    # Uncomment the line below to select a different bounding box
    # bbox = cv2.selectROI(frame, False)

    # Initialize tracker with first frame and bounding box
    for _ in range(4):
        ok = tracker[_].init(frame, bbox[_])
    
    
    index_ = 0
    while True:
        # Read a new frame
        index_ += 1
        ok, frame = video.read()
        if not ok:
            break
         
        # Start timer
        timer = cv2.getTickCount()

        
        ans = []
        for _ in range(4):
            # Update tracker
            ok, bbox = tracker[_].update(frame)
            # Calculate Frames per second (FPS)
            # fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
            # Draw bounding box
            if ok:
                # Tracking success
                p1 = (int(bbox[0]), int(bbox[1]))
                p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
                p3 = (int(bbox[0] + bbox[2]/2), int(bbox[1] + bbox[3]/2))
                ans.append(p3)
                if (save_img or save_img2):
                    cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
            else :
                # Tracking failure
                if (save_img or save_img2):
                    cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)

            if (save_img):
                # Display tracker type on frame
                cv2.putText(frame, tracker_type + " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);

                # Display FPS on frame
                # cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);

                # Display result
                cv2.imwrite("result/%05d_%d.jpg"%(index_, _) , frame)
        if (save_img2):
            cv2.imwrite("result/%05d_.jpg"%(index_), frame)
        if (save_result):
            frame = Trans_forward(frame, np.array(ans , dtype = np.float32), ad)
            cv2.imwrite("result2/%05d_.jpg"%(index_), frame)
            out.write(frame)
        # Exit if ESC pressed
        k = cv2.waitKey(1) & 0xff
        if k == 27 : break
        if index_ == middle_halt : break
    out.release()
    return np.array(ans)
if (__name__=="__main__"):
    pass