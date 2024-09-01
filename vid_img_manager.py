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
        fps = cap.get(cv.CAP_PROP_FPS)
        print(f"Frame rate set to: {fps} FPS")
        RArmData = []
        RKneeData = []
        LKneeData = []
        RElbowData = []
        LElbowData = []

        frame_number = 0  # Initialize the frame counter

        while(True):
            has_frame, frame = cap.read()
            if not has_frame:
                print("Error: Could not read frame.")
                break

            if self.FIRST:
                self.WEB_CAM_H,self.WEB_CAM_W = frame.shape[0:2]
                self.FIRST = False

            frame, RArm, LKnee, RKnee, LElbow, RElbow = self.POSE_ESTIMATOR.get_pose_key_angles(frame, frame_number)
            LKneeData.append({'Time': time.time() - start_time, 'LKnee': LKnee})
            RKneeData.append({'Time': time.time() - start_time, 'RKnee': RKnee})
            RElbowData.append({'Time': time.time() - start_time, 'RElbow': RElbow})
            LElbowData.append({'Time': time.time() - start_time, 'LElbow': LElbow})
            frame_number += 1  # Increment the frame counter

            cv.imshow('frame',frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
            # print("Video capture finished.")
        # return LElbowData
        # print("Video capture finished.")
        df1 = pd.DataFrame(LKneeData)
        try:
            df1.to_excel(os.path.join(os.path.dirname(__file__),'LeftKnee_7608-3_70626--V3.xlsx'), index=False)
            print("Excel files saved successfully.")
        except Exception as e:
            print("Error saving Excel files:", e)

    def estimate_img(self,img_path):
        """applies pose estimation on img"""

        img = cv.imread(img_path)

        img = self.POSE_ESTIMATOR.get_pose_key_angles(img)


        cv.imshow("Image Pose Estimation",img)

        cv.waitKey(0)
        cv.destroyAllWindows()

