import serial
import serial.tools.list_ports
import time

#List writing. 
from datetime import datetime
import csv

actual_path = [[1,1,1,1],[2,1,2,2],[3,1,3,4]]
target_path = [[2,2,2,3],[4,1,4,1],[4,1,6,4]]

cur_date = datetime.now()
cur_date = cur_date.timetuple()

folder_name = "test_results/"
test_name = "adapting" 
test_time = "-{}-{}:{}.csv".format(cur_date[2],cur_date[3],cur_date[4])

file_name = folder_name + test_name + test_time


with open(file_name, 'w') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in range(len(actual_path)):
	    spamwriter.writerow([str(actual_path[i]), str(target_path[i])])


#List reading. 
actual_list = []
target_list = []

with open(file_name, 'r') as csvfile:
    spamwriter = csv.reader(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

    for row in spamwriter:
    	actual = row[0]
    	target = row[1]
    	actual = actual.translate({ord(i):None for i in '[] '}).split(',') #[1,1,1,1]
    	target = target.translate({ord(i):None for i in '[] '}).split(',')
    	actual_list.append([int(x) for x in actual])
    	target_list.append([int(x) for x in target])

print(actual_list)
print(target_list)

# print([comport.device for comport in serial.tools.list_ports.comports()])
# ser1 = serial.Serial(str(serial.tools.list_ports.comports()[0]).split()[0], 9600, timeout = 0.01)
# print(str(serial.tools.list_ports.comports()[0]))


# #Convert int to the string format. (Round the val to a speed btwn -255-255. Add leading zeros)
# #str(1).zfill(2)

# time.sleep(3)
# #get_feedback (put into get_feedback function)
# for i in range(100):
# 	print("loop" + str(i))
# 	prevtime = time.time()
# 	ser1.write("1111\n".encode())
# 	#get_feedback; allow tiny amount of time for arduino to respond
# 	time.sleep(0.005)
# 	vals = ser1.readline().decode("utf-8")
# 	print("r: " + ser1.readline().decode("utf-8"))
# 	if vals != '': #or else you'll mess up the state machine
# 		ser1.write("00000000\n".encode())
# # print(str(serial.tools.list_ports.comports()[0]).split()[0])

# 	print(time.time()-prevtime)
# 	time.sleep(0.095)


# def read_serial(): Requires thread; not worth. 
# 	buffer_string = ''
#     while True:
#         # buffer_string = buffer_string + ser.read(ser.inWaiting())
#         buffer_string = buffer_string + ser.readline()

#         if '\n' in buffer_string:
#             lines = buffer_string.split('\n') # Guaranteed to have at least 2 entries
#             last_received = lines[-2]
#             #If the Arduino sends lots of empty lines, you'll lose the
#             #last filled line, so you could make the above statement conditional
#             #like so: if lines[-2]: last_received = lines[-2]
#             buffer_string = lines[-1]
#             break
#     print(buffer_string)


# while(True):
# 	prevtime = time.time()
# 	# ser1.read(20)
# 	print(ser1.readline())
# 	print("dt = " + str(time.time()-prevtime))

# # while True:
# # 	feedback = ser1.readline()
# # 	print(type(feedback))
# # 	print(feedback)
# # 	ser1.write('Python') #why is this repeating??

# 	#Current communication method takes 50 ms


# direction = 1;
# #Communication experiment: 

# while True:
# 	for i in range(255):
# 		# i = i*10

# 		start_time = time.time()

# 		ser1.write(str(i*direction).encode());
# 		feedback = ser1.readline()
# 		print(feedback)
# 		end_time = time.time()
# 		print("TIME ELAPSED: " + str(end_time-start_time))
# 		# delay(0.01)
# 	direction = direction*-1

# 	# for i in range(100, -1): 
# 	# 	ser1.write(str(i*direction).encode());
# 	# 	feedback = ser1.readline()
# 	# 	print(feedback)
# 	# 	direction = direction*-1

# ser1.write("00000000\n".encode())
		