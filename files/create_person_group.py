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
