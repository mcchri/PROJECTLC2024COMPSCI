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
# this functoin automatically connects to the comport of the serial
def find_comport(pid, vid, baud):
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
# A function to write data into the firebase
def firebase_read_reference(ref1,aux,ser1,timestamp,mem1):
    source = 'microbit'
    var1 = ser1.readline()
    var1 = str(var1.decode('utf-8'))
    
    date_time = datetime.fromtimestamp(timestamp)
    time_taken = str(date_time.strftime("%S %M %H %d %m %Y"))
    time_taken_key = date_time.strftime("%Y %m %d %H %d %m %Y")
    print(str(date_time.strftime("%S %M %H %d %m %Y")))
    #add the values into the dictionary of the nodes
    if aux == 0:
        time.sleep(0.1)
        ref1.update({timestamp:{'Memory_level':var1, 'Location':source}})
        print("Memory:",var1)
        return var1
    if aux == 1:
        time.sleep(0.1)
        ref1.update({timestamp:{'Light_level':var1, 'Location':source, 'Memory_level':mem1}})
        print("Light_level:",var1)
    elif aux == 2:
        time.sleep(0.1)
        ref1.update({timestamp:{'Age':var1, 'Location':source, 'Memory_level':mem1}})
        print("Age:",var1)
    elif aux == 3:
        time.sleep(0.1)
        ref1.update({timestamp:{'Score':var1, 'Location':source}})
        print("Score:",var1)
    else:
        time.sleep(0.1)
        ref1.update({timestamp:{'Level':var1, 'Location':source}})
        print("Level:",var1)
    
# path to the private key
cred = credentials.Certificate("C:/Users/k_tur/OneDrive/Documents/cs/config.json")
# URL to the database
firebase_admin.initialize_app(cred,{'databaseURL': 'https://comp-sci-c8d0a-default-rtdb.europe-west1.firebasedatabase.app/'})
# get a reference to our db
ref = db.reference()

#while true go through all the nodes in the firebase

while True:
    timestamp1 = int(time.time())
    if ser.readline().strip().decode('utf-8') == 'lose':
       
        time.sleep(0.1)
        iterator = 0
        y=0
        ref = db.reference().child('Memory')
        memory = firebase_read_reference(ref,iterator,ser,timestamp1,y)
        iterator += 1
        ref = db.reference().child('Light')
        firebase_read_reference(ref,iterator,ser,timestamp1,memory)
        iterator += 1
        ref = db.reference().child('Age')
        firebase_read_reference(ref,iterator,ser,timestamp1,memory)
        iterator += 1
        ref = db.reference().child('Score')
        firebase_read_reference(ref,iterator,ser,timestamp1,y)
        iterator += 1
        ref = db.reference().child('Level')
        firebase_read_reference(ref,iterator,ser,timestamp1,y)

