# Written by Lex Whalen

from vid_img_manager import VideoImgManager
import os
import pandas as pd

class Main():

    def __init__(self):
        self.VI_M = VideoImgManager()

    # def img_estimation(self,img_path):
    #     self.VI_M.estimate_img(img_path)
            
    # def live_estimation(self,webcam_id=0):
    #     self.VI_M.estimate_vid(webcam_id)
            
    def video_estimation(self,video_path):
        self.VI_M.estimate_vid(video_path)
        # df1 = pd.DataFrame(self.VI_M.estimate_vid(video_path))
        # df1.to_excel(os.path.join(os.path.dirname(__file__),'EEElbowData_angle.xlsx'), index=False)
        # try:
        #     df1.to_excel(os.path.join(os.path.dirname(__file__),'EEElbowData_angle.xlsx'), index=False)
        #     print("Excel files saved successfully.")
        # except Exception as e:
        #     print("Error saving Excel files:", e)

if __name__ == "__main__":
    app = Main()
    app.video_estimation("7608-3_70626.avi")

