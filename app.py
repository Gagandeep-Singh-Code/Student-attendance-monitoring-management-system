from flask import Flask, send_file,render_template, flash, request,redirect,url_for
import os, glob, shutil, sys
from flask import send_from_directory
from files.add_student import AddStudent
from files.create_person_group import create_person_group_func
from openpyxl import Workbook, load_workbook
from datetime import date
app = Flask(__name__)
app.secret_key = "Trial"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addrecord/', methods = ['POST','GET'])
def addrecord():
    if request.method == 'POST':
        user_name = request.form.get('name_stu')
        user_roll = request.form.get('roll')
        a = request.form.get('exe')
        AddStudent(user_name, user_roll)
        if a == "Yes":
            create_person_group_func()
            flash("Person group created")
        elif a == "No":
            pass
        else:
            print("Invalid choice.")
            pass
        folderPath = './dataset'
        os.system("python create_person.py " + max(glob.glob(os.path.join(folderPath, '*/')), key=os.path.getmtime))
        flash("Person ID successfully added to the database")
        os.system("python add_person_faces.py " + max(glob.glob(os.path.join(folderPath, '*/')), key=os.path.getmtime))
        os.system("python train.py")
        os.system("python get_status.py")
        flash("Student record added.")
        return render_template('index.html')
    else:
        flash("When you click on Submit wait for a few moments, while the images will be uploaded.")
        return render_template('addrecord.html')
    

@app.route('/attendance/', methods = ['POST','GET'])
def attend():
    if request.method == 'GET':
        flash("The attendance will be taken automatically in 3 seconds.")
        flash("Wait for a few moments to download the excel sheet with attendance details.")
        #os.system("python take_attendance.py")
        folder = './attendance'
        latest_folder = max(glob.glob(os.path.join(folder, '*/')), key=os.path.getmtime)
        croppedFol = './cropped'
        for image in os.listdir(latest_folder):
            if os.path.exists(croppedFol):
                shutil.rmtree(croppedFol)
            os.makedirs(croppedFol)
            os.system("python detect.py " + os.path.join(latest_folder, image))
            os.system("python spreadsheet.py ")
            os.system("python identify.py ")
        flash("Excel sheet ready to download")
        return render_template('attendance.html')
    else:
        return render_template('index.html')

@app.route('/download/')
def download_file():
    file_path = "./reports.xlsx"
    return send_file(file_path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)




'''
#********************************************AddStudentCode*********************************************************
import cv2                                                                      # openCV
import numpy as np                                                              # for numpy arrays
import pyodbc
import dlib
import os                                                                       # for creating folders
from subprocess import run
import sys

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()

def insertOrUpdate(Id, Name, roll) :                                            # this function is for database
    #connect = sqlite3.connect("Face")                                          # connecting to the database
    server = 'tcp:dbdata1.database.windows.net'
    database = 'FaceData'
    username = 'root_g'
    password = 'Tiger@1807'
    connect = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cmd = "SELECT * FROM Students WHERE ID = " + Id                             # selecting the row of an id into consideration
    cursor = connect.execute(cmd)
    isRecordExist = 0
    for row in cursor:                                                          # checking wheather the id exist or not
        isRecordExist = 1
    if isRecordExist == 1:                                                      # updating name and roll no
        connect.execute("UPDATE Students SET Name = ? WHERE ID = ?",(Name, Id))
        connect.execute("UPDATE Students SET Roll = ? WHERE ID = ?",(roll, Id))
    else:
    	params = (Id, Name, roll)                                               # insering a new student data
    	connect.execute("INSERT INTO Students(ID, Name, Roll) VALUES(?, ?, ?)", params)
    connect.commit()                                                            # commiting into the database
    connect.close()                                                             # closing the connection

def AddStudent(namei,rolli):
    name = namei
    roll = rolli
    #Id = roll[-5:]
    Id = roll[1:]
    insertOrUpdate(Id, name, roll)                                                  # calling the sqlite3 database


    folderName = "user" + Id                                                        # creating the person or user folder
    folderPath = os.path.join("D:/Gagandeep/Future Ready Talent/Face-Recognition-attendance-system/Attendance-System-with-original-code/", "dataset/"+folderName)
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)

'''
'''
    sampleNum = 0
    while(True):
        ret, img = cap.read()                                                       # reading the camera input
        #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                                # Converting to GrayScale
        dets = detector(img, 1)
        for i, d in enumerate(dets):                                                # loop will run for each face detected
            sampleNum += 1
            cv2.imwrite(folderPath + "/User." + Id + "." + str(sampleNum) + ".jpg",
                        img[d.top():d.bottom(), d.left():d.right()])                                                # Saving the faces
            cv2.rectangle(img, (d.left(), d.top())  ,(d.right(), d.bottom()),(0,255,0) ,2) # Forming the rectangle
            cv2.waitKey(200)                                                        # waiting time of 200 milisecond
        cv2.imshow('frame', img)                                                    # showing the video input from camera on window
        cv2.waitKey(1)
        if(sampleNum >= 20):                                                        # will take 20 faces
            break

    cap.release()                                                                   # turning the webcam off
    cv2.destroyAllWindows()                                                         # Closing all the opened windows
    '''


'''
#********************************************CreatePersonGroupCode*********************************************************
from global_variables import PERSON_GROUP_ID
import sys
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

KEY = '6e10e7984461435eae5bf7237b4b0490'
#CF.Key.set(Key)

ENDPOINT = 'https://attendancesystem.cognitiveservices.azure.com/'  
#CF.BaseUrl.set(BASE_URL)

def create_person_group_func():
    face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

    try:    
        print('Person group name:', PERSON_GROUP_ID)
        #Person Group Created
        face_client.person_group.create(person_group_id=PERSON_GROUP_ID, name=PERSON_GROUP_ID)
        print('Created person group:', PERSON_GROUP_ID)
    except:
        print("Group already present, Try another name.")
'''