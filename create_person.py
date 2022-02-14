import sys
from global_variables import PERSON_GROUP_ID
import pyodbc
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

KEY = 'ENTER API KEY HERE'


 
ENDPOINT = "ENTER BASE URL HERE"

face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

if len(sys.argv) is not 1:
    res = face_client.person_group_person.create(PERSON_GROUP_ID, str(sys.argv[1]))       #creating person in person group
    #print(res)
    extractId = str(sys.argv[1])[14:-1]
    server = 'ENTER SERVER NAME HERE'
    database = 'ENTER DATABASE NAME HERE'
    username = 'ENTER USERNAME HERE'
    password = 'ENTER PASSWORD HERE'
    connect = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cmd = "SELECT * FROM Students WHERE ID = " + extractId
    cursor = connect.execute(cmd)
    isRecordExist = 0
    for row in cursor:                                                          # checking wheather the id exist or not
        isRecordExist = 1
    if isRecordExist == 1:                                                      # updating name and roll no
        connect.execute("UPDATE Students SET personID = ? WHERE ID = ?",(res.person_id, extractId))
    connect.commit()                                                            # commiting into the database
    connect.close()
    print ("Person ID successfully added to the database")

