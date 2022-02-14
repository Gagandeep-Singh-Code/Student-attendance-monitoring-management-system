import cv2
import dlib
import os
import sys
import pyodbc

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#cam = cv2.VideoCapture(1)
face_detector = dlib.get_frontal_face_detector()

if len(sys.argv) is not 1:
	img = cv2.imread(str(sys.argv[1]))
	dets = face_detector(img, 1)
	if not os.path.exists('./cropped'):
		os.makedirs('./cropped')
	print ("detected = " + str(len(dets)))
	for i, d in enumerate(dets):
   		cv2.imwrite('./cropped/face' + str(i + 1) + '.jpg', img[d.top():d.bottom(), d.left():d.right()])