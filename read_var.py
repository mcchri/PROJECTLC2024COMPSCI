import time
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import serial
from serial.tools.list_ports import comports

PID_MICROBIT = 516
VID_MICROBIT = 3368
TIMEOUT = 0.1

def find_comport(pid, vid, baud):
    #list_ports = serial.tools.list_ports.comports()
    ''' return a serial port '''
    ser_port = serial.Serial(timeout=TIMEOUT)
    ser_port.baudrate = baud
    ports = serial.tools.list_ports.comports()
    print('scanning ports')
    for p in ports:
        if (p.pid == pid) and (p.vid == vid):
            print('found target device pid: {} vid: {} port: {}'.format(p.pid, p.vid, p.device))
            ser_port.port = str(p.device)
            return ser_port
    return None

ser = find_comport(PID_MICROBIT, VID_MICROBIT, 115200)
if not ser:
    print('microbit not found')
else:    
    ser.open()

def firebase_read_reference(ref1,aux,ser1):
    source = 'microbit'
    var1 = ser1.readline()
    var1 = str(var1.decode('utf-8'))
    timestamp = int(time.time())
    date_time = datetime.fromtimestamp(timestamp)
    time_taken = date_time.strftime("%S/%M/%H/%d/%m/%Y")
    time_taken_key = date_time.strftime("%Y %m %d %H %d %m %Y")
    if aux == 0:
        time.sleep(1)
        ref1.update({timestamp:{'Light_level':var1, 'Location':source, 'time_taken_at':time_taken}})
        print("Light_level:",var1)
    elif aux == 1:
        time.sleep(1)
        ref1.update({timestamp:{'Age':var1, 'Location':source, 'time_taken_at':time_taken}})
        print("Age:",var1)
    elif aux == 2:
        time.sleep(1)
        ref1.update({timestamp:{'Score':var1, 'Location':source, 'time_taken_at':time_taken}})
        print("Score:",var1)
    else:
        time.sleep(1)
        ref1.update({timestamp:{'Level':var1, 'Location':source, 'time_taken_at':time_taken}})
        print("Level:",var1)
# path to the private key
cred = credentials.Certificate("C:/Users/19CTurean.ACC/Documents/config.json")
# URL to the database
firebase_admin.initialize_app(cred,{'databaseURL': 'https://comp-sci-c8d0a-default-rtdb.europe-west1.firebasedatabase.app/'})
# get a reference to our db
ref = db.reference()

#ser = serial.Serial()
#ser.baudrate = 115200
#ser.port = "COM6"
#ser.open()

while True:
    #print(ser.readline())
    #print(ser.readline())
    if ser.readline().strip().decode('utf-8') == 'lose':
       
        time.sleep(1)
        iterator = 0
        ref = db.reference().child('Light')
        firebase_read_reference(ref,iterator,ser)
        iterator += 1
        ref = db.reference().child('Age')
        firebase_read_reference(ref,iterator,ser)
        iterator += 1
        ref = db.reference().child('Score')
        firebase_read_reference(ref,iterator,ser)
        iterator += 1
        ref = db.reference().child('Level')
        firebase_read_reference(ref,iterator,ser)
    #ref.delete()
