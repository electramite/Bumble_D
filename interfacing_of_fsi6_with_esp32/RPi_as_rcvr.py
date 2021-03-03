import socket
 
s = socket.socket()         
 
s.bind(('0.0.0.0', 8091))
s.listen(5)                 
 
while True:
  
    c, addr = s.accept() # waiting for connection
    d1 = c.recv(1024).decode('utf-8') # recieving data from esp
    print(d1) # printing data to terminal
 
 

