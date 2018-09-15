import pyrebase
import time
from configuration import *
from helpers import *

fb = pyrebase.initialize_app(FIREBASE_CONFIG)
auth = fb.auth()
db = fb.database()
storage = fb.storage()

user = authenticate_user(auth)
#print(user)


#Get data video/images/metadata/etc from an event

###TEST EVENTS
event_1 = {
    'time': time.time(),
    'metadata': {'type': 'usps delivery', 'gender': 'female'},
}

event_1_photo = './photos/twitter_banner.png'

event_2 = {
    'time': time.time(),
    'metadata': {'type': 'metronet salesperson', 'gender': 'male'},
}

event_2_photo = './photos/amazon.png'


# Pass the user's idToken to the push method
metadata_store = db.child("users").child(user['localId']).push(event_1, user['idToken'])
#Store the image
media_store = storage.child('images/' + user['localId'] + '/' + str(time.time()) + '.png').put(event_1_photo, user['idToken'])
