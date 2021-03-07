import socket
import serial
import time
import re

ser = serial.Serial('COM7', 115200, timeout=1) # selsct the COM port accordingly (in which arduino is plugged in)
ser.flush()


s = socket.socket()
# host = "192.168.43.229"
host = "127.0.0.1"
port = 4596
s.bind((host, port))
time.sleep(1)

print(host)
s.listen(5)
c, addr = s.accept()
while True:

    
    d1 = c.recv(1024).decode('utf-8')  # receiving PWM signals from sender_arduino via socket
    d1 = re.findall(r'\d+', d1) # storing them in a list

    print(d1)
    ch = f"{d1[0]} {d1[1]} {d1[2]} {d1[3]} {d1[4]} {d1[5]}\n"
    ser.write(f"{ch}\n".encode('utf-8'))

