import serial
import serial.tools.list_ports
import time


# print([comport.device for comport in serial.tools.list_ports.comports()])
ser1 = serial.Serial(str(serial.tools.list_ports.comports()[0]).split()[0], 9600, timeout = 0.01)

ser2 = serial.Serial(str(serial.tools.list_ports.comports()[1]).split()[0], 9600, timeout = 0.01)



#Convert int to the string format. (Round the val to a speed btwn -255-255. Add leading zeros)
#str(1).zfill(2)
ser1.write("1111\n".encode())
ser1.write("0\n".encode())

ser2.write("1111\n".encode())
ser2.write("0\n".encode())