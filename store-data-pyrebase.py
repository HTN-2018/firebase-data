import pyrebase
import time
from configuration import *
from helpers import *

fb = pyrebase.initialize_app(FIREBASE_CONFIG)
auth = fb.auth()
db = fb.database()
storage = fb.storage()

user = authenticate_user(auth)
print(user)

#Get data video/images/metadata/etc

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

# data to save
#data = {
#    "name": "Mortimer 'Morty' Smith"
#}

# Pass the user's idToken to the push method
results = db.child("users").child(user['localId']).push(event_1, user['idToken'])