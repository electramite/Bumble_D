import socket
import serial
import time
import re

ser = serial.Serial('/dev/USB0', 9600, timeout=1)
ser.flush()
s = socket.socket()
host = "127.0.0.1"
port = 4589
s.bind((host, port))
time.sleep(1)

print(host)
s.listen(5)
c, addr = s.accept()
while True:

	
	p = c.recv(1024).decode('utf-8')
	temp = re.findall(r'\d+', p)
	res = list(map(int, temp)) 
	pot = res[0]
	ser.write(f"{pot}\n".encode('utf-8'))
	print(pot)