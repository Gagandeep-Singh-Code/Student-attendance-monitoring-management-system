import sys
import os, time
from global_variables import PERSON_GROUP_ID
import urllib
import pyodbc
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


KEY = 'ENTER API KEY HERE'


 
ENDPOINT = "ENTER BASE URL HERE"


face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))



def get_person_id():
	person_id = ''
	extractId = str(sys.argv[1])[14:-1]
	server = 'ENTER SERVER NAME HERE'
	database = 'ENTER DATABASE NAME HERE'
	username = 'ENTER USERNAME HERE'
	password = 'ENTER PASSWORD HERE'
	connect = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
	c = connect.cursor()
	cmd = "SELECT * FROM Students WHERE ID = " + extractId
	c.execute(cmd)
	row = c.fetchone()
	person_id = row[3]
	connect.close()
	return person_id

if len(sys.argv) is not 1:
    currentDir = os.path.dirname(os.path.abspath(__file__))
    imageFolder = os.path.join(currentDir, "dataset/" + str(sys.argv[1])[9:-1])
    person_id = get_person_id()
    for filename in os.listdir(imageFolder):
        if filename.endswith(".jpg"):
            #print (filename)
            image = (os.path.join(imageFolder, filename))
            img = open(image, 'r+b')
            res = face_client.face.detect_with_stream(img, detectionModel='detection_03')
            time.sleep(6)
            if len(res) != 1:
                print ("No face detected in image")
            else:
                res = face_client.person_group_person.add_face_from_stream(PERSON_GROUP_ID, person_id, open(image, 'r+b'))
                print("Uploaded for:", filename)
                