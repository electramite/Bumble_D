import socket
import serial
import time
import re

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
ser.flush()


s = socket.socket()
host = "192.168.43.70"
port = 4592
s.bind((host, port))
time.sleep(1)

print(host)
s.listen(5)
c, addr = s.accept()
while True:

	
	d1 = c.recv(1024).decode('utf-8')	
	d1 = re.findall(r'\d+', d1)
	
	D1 = list(map(int, d1))
	name = str(D1[0])
	ser.write(f"{name}\n".encode('utf-8'))
