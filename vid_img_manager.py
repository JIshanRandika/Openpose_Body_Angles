# Written by Lex Whalen

import cv2 as cv
from pose_estimator import PoseEstimator
from frame_operations import FrameOperations
import os
import pandas as pd
import time

class VideoImgManager():

    def __init__(self):
        self.POSE_ESTIMATOR = PoseEstimator()
        self.FRAME_OPS = FrameOperations()

        self.FIRST = True

    def estimate_vid(self,webcam_id=0):
        """reads webcam, applies pose estimation on webcam"""
        start_time = time.time()
        cap = cv.VideoCapture(webcam_id)
        RArmData = []

        while(True):
            has_frame, frame = cap.read()

            if self.FIRST:
                self.WEB_CAM_H,self.WEB_CAM_W = frame.shape[0:2]
                self.FIRST = False

            frame,RArm = self.POSE_ESTIMATOR.get_pose_key_angles(frame)
            RArmData.append({'Time': time.time() - start_time, 'RArm': RArm})
            cv.imshow('frame',frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                df1 = pd.DataFrame(RArmData)
                try:
                    df1.to_excel(os.path.join(os.path.dirname(__file__),'camera_angles.xlsx'), index=False)
                    print("Excel files saved successfully.")
                except Exception as e:
                    print("Error saving Excel files:", e)
                break
    
    def estimate_img(self,img_path):
        """applies pose estimation on img"""

        img = cv.imread(img_path)

        img = self.POSE_ESTIMATOR.get_pose_key_angles(img)


        cv.imshow("Image Pose Estimation",img)

        cv.waitKey(0)
        cv.destroyAllWindows()

