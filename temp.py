import serial
import serial.tools.list_ports
import time

print([comport.device for comport in serial.tools.list_ports.comports()])
print(str(serial.tools.list_ports.comports()[0]).split()[0])
ser1 = serial.Serial(str(serial.tools.list_ports.comports()[0]).split()[0], 9600)


# while True:
# 	feedback = ser1.readline()
# 	print(type(feedback))
# 	print(feedback)
# 	ser1.write('Python') #why is this repeating??

	#Current communication method takes 50 ms


direction = 1;
#Communication experiment: 

while True:
	for i in range(255):
		# i = i*10

		start_time = time.time()

		ser1.write(str(i*direction).encode());
		feedback = ser1.readline()
		print(feedback)
		end_time = time.time()
		print("TIME ELAPSED: " + str(end_time-start_time))
		# delay(0.01)
	direction = direction*-1

	# for i in range(100, -1): 
	# 	ser1.write(str(i*direction).encode());
	# 	feedback = ser1.readline()
	# 	print(feedback)
	# 	direction = direction*-1