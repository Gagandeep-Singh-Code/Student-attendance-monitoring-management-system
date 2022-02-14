from global_variables import PERSON_GROUP_ID
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

KEY = 'ENTER API KEY HERE'


 
ENDPOINT = "ENTER BASE URL HERE"

face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

while (True):
    training_status = face_client.person_group.get_training_status(PERSON_GROUP_ID)
    print("Training status: {}.".format(training_status.status))
    print()
    if (training_status.status=='succeeded'):
        break
    elif (training_status.status=='failed'):
        face_client.person_group.delete(person_group_id=PERSON_GROUP_ID)
        sys.exit('Training the person group has failed.')
    time.sleep(5)
