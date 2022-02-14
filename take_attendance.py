import cv2                                                                      # openCV
#import numpy as np                                                              # for numpy arrays
#import sqlite3
import dlib
import os                                                                       # for creating folders
import sys

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



#
#database
#

def capture():
    cap = cv2.VideoCapture(0)
    sampleNum = 0
    while(True):
        ret, img = cap.read()                                                       # reading the camera input
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                # Converting to GrayScale
        if ret:                                                # loop will run 
            sampleNum += 1
            cv2.imwrite(folderPath + "/attend." + Id + "." + str(sampleNum) + ".jpg", img)                                                # Saving the images
            #cv2.rectangle(img, (d.left(), d.top())  ,(d.right(), d.bottom()),(0,255,0) ,2) # Forming the rectangle
            cv2.waitKey(100)                                                        # waiting time of 50 milisecond
        cv2.imshow('frame', img)                                                    # showing the video input from camera on window
        cv2.waitKey(1)
        if(sampleNum == 1):                                                        # will take 20 faces
            break

    cap.release()                                                                   # turning the webcam off
    cv2.destroyAllWindows() 

Id = '1'
x = int(input("Enter 1 to capture:"))
if x == 1:
    folderName = "Attend" + Id                                                        # creating the car or user folder
    folderPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "attendance/"+folderName)
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)
    #capture()
    Id = str(int(Id) + 1)
else:
    print("Invalid Input.")
