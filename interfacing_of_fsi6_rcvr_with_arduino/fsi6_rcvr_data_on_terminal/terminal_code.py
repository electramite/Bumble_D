import serial
import time


ser = serial.Serial('COM6', baudrate = 115200, timeout = 1)

time.sleep(1)
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
	
	print(li)
