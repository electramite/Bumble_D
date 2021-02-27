import socket
import time



s = socket.socket()
host = "192.168.43.70"
port = 4590
s.bind((host, port))
time.sleep(1)

print(host)
s.listen(5)
c, addr = s.accept()


while True:

	
	data = c.recv(1024).decode('utf-8')
	print(data)


