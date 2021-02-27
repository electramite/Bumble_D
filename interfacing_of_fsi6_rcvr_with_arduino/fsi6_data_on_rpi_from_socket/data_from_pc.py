import serial
import time
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
ser = serial.Serial('COM6', baudrate = 9600, timeout = 1)

host = "192.168.43.70"
port = 4590

s.connect((host, port))

time.sleep(1)
print("connected....")
def getVal():
	data1 = ser.readline()
	data2 = ser.readline()
	data3 = ser.readline()
	data4 = ser.readline()
	data5 = ser.readline()
	data6 = ser.readline()
	return data1, data2, data3, data4, data5, data6
while True:
	li = []

	d1, d2, d3, d4, d5, d6 = getVal()
	d1 = d1[0:4]
	d2 = d2[0:4]
	d3 = d3[0:4]
	d4 = d4[0:4]
	d5 = d5[0:4]
	d6 = d6[0:4]

	d1 = d1.decode("ascii")
	d2 = d2.decode("ascii")
	d3 = d3.decode("ascii")
	d4 = d4.decode("ascii")
	d5 = d5.decode("ascii")
	d6 = d6.decode("ascii")

	d1 = d1.split()
	d2 = d2.split()
	d3 = d3.split()
	d4 = d4.split()
	d5 = d5.split()
	d6 = d6.split()

	li.append(d1)
	li.append(d2)
	li.append(d3)
	li.append(d4)
	li.append(d5)
	li.append(d6)

	data = f"{li[0][0]},{li[1][0]},{li[2][0]},{li[3][0]},{li[4][0]},{li[5][0]}"
  s.send(data.encode("utf-8"))
	print(data)
