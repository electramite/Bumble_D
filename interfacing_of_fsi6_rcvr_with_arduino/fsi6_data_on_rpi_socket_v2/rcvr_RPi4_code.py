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
    ch1 = str(d1[0]) # extracting PWM reading for Ch1
    ser.write(f"{ch1}\n".encode('utf-8')) # sending PWM signal for Ch1 to rcvr_arduino which is connected to RPi via serial communication
    ch2 = str(d1[1]) # extracting PWM reading for Ch2
    ser.write(f"{ch2}\n".encode('utf-8')) # sending PWM signal for Ch2 to rcvr_arduino 
    ch3 = str(d1[2]) # extracting PWM reading for Ch3
    ser.write(f"{ch3}\n".encode('utf-8'));
    ch4 = str(d1[3]) # extracting PWM reading for Ch4
    ser.write(f"{ch4}\n".encode('utf-8'))
    ch5 = str(d1[4]) # extracting PWM reading for Ch5
    ser.write(f"{ch5}\n".encode('utf-8'))
    ch6 = str(d1[5]) # extracting PWM reading for Ch6
    ser.write(f"{ch6}\n".encode('utf-8')) 
