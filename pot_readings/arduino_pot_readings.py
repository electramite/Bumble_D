import serial
import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
ser = serial.Serial('COM7', baudrate = 115200, timeout = 1)


host = "192.168.43.70"
port = 4589

s.connect((host, port))

def getVal():
	data = ser.readline()
	return data
while True:
	p = getVal()
	b = p.decode()
	s.send(bytes(b, "utf-8"))
	print(b)

