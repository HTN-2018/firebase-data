from firebase import firebase

fb = firebase.FirebaseApplication('https://hack-the-north-2018.firebaseio.com', None)

name = input('Enter a name: ')

result = fb.post('/users', name)
print(result)