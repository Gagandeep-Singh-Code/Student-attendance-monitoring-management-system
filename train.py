from global_variables import PERSON_GROUP_ID
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

KEY = '6e10e7984461435eae5bf7237b4b0490'
#CF.Key.set(Key)

ENDPOINT = 'https://attendancesystem.cognitiveservices.azure.com/'  
#CF.BaseUrl.set(BASE_URL)

face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

print('Training the person group...')
# Train the person group
face_client.person_group.train(PERSON_GROUP_ID)

#getting status
'''
while (True):
    training_status = face_client.person_group.get_training_status(PERSON_GROUP_ID)
    print("Training status: {}.".format(training_status.status))
    print()
    if (training_status.status is TrainingStatusType.succeeded):
        break
    elif (training_status.status is TrainingStatusType.failed):
        face_client.person_group.delete(person_group_id=PERSON_GROUP_ID)
        sys.exit('Training the person group has failed.')
    time.sleep(5)
'''