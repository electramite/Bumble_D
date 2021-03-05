import serial
import time
import socket
import re

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
ser = serial.Serial('COM6', baudrate = 115200, timeout = 1) # select the COM port accordingly

# host = "192.168.43.229"
host = "127.0.0.1" # localHost
port = 4596

s.connect((host, port))

time.sleep(1)
print("connected....")
def getVal():
	data1 = ser.readline() # getting PWM signals from sender_arduino 

	return data1
while True:


	d1 = getVal()
	s.sendall(d1) # sending all pwm readings to RPi

	d1 = d1.decode("ascii")
	D1 = re.findall(r"[-+]?\d*\.\d+|\d+", d1) # storing all PWM readings in a list
	print(D1)
