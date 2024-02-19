import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import serial
# path to the private key
cred = credentials.Certificate("C:/Users/19CTurean.ACC/Documents/comp-sci-c8d0a-firebase-adminsdk-yk4h3-55cfc3c52d.json")
# URL to the database
firebase_admin.initialize_app(cred,{'databaseURL': 'https://comp-sci-c8d0a-default-rtdb.europe-west1.firebasedatabase.app/'})
# get a reference to our db
ref = db.reference()

ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM6"
ser.open()

ref = db.reference().child('Light')
ref = db.reference().child('Age')
ref = db.reference().child('Score')

ref.update({'Description':'Biology123 class', 'id':'Biology123', 'title':'Biology 123'})
#ref = db.reference().child('classes').child('Math123')
#ref.update({'Description':'Math123 class', 'id':'Math123', 'title':'Math123'})

#ref = db.reference().child('classes').child('Biology123')
#ref.delete()



while True:
    light = ser.readline()
    light = str(light.decode('utf-8'))
    #ref = db.reference().child('Light')
   # ref.update({'Description':light, 'id':light, 'title':light})
    print(light)