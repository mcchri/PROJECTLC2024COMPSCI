import serial
import time

ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM6"
ser.open()

while True:
    light = ser.readline()
    print(str(light.decode('utf-8'))) 
