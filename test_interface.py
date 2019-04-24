from abr_control.interfaces import PROSTHETIC_HAND
import time
import numpy as np

interface = PROSTHETIC_HAND()
interface.connect()

print(interface.serial_coms)



#Testing speed of interface class. Result: latency = 51-54 ms. 
# for i in range(100):
# 	# print("iteration " + str(i))
# 	prev = time.time()
# 	print(interface.get_feedback())
# 	interface.send_forces([0,50,0,50])
# 	cur_dt = time.time()-prev
# 	print(cur_dt)

# print('hi')
# print(feedback)
# print(cur_dt)

####Testing write. 
interface.get_feedback()

interface.send_forces([-150,-150,-150,-150])
time.sleep(1.5)

print(interface.get_feedback())

# interface.send_forces([-150,0,0,0])

# time.sleep(1)
# print(interface.get_feedback())
interface.send_forces([0,0,0,0])


#######Testing Feedback performance. Results: Occasionally fks up (lag a lot)
# for i in range(1000):
# 	print("iteration " + str(i))
# 	prev = time.time()
# 	feedback = interface.get_feedback()
# 	print(feedback)
# 	print(time.time()-prev)

########Testing write. 
# interface.send_forces(np.array([-150,-150,-150,-150]))
# time.delay(1.5)
# interface.send_forces(np.zeros(4))

#expected: 20.6, 0, -1.96, 0.59

# print(interface.get_feedback());
#expected: q:[] dq:[]

# # robot_config = jaco2.Config()
# ctrlr = OSC(robot_config)
# # interface = VREP(robot_config)

# interface.connect()

# target_xyz = [.2, .2, .5]  # in metres
# for ii in range(1000)
#     feedback = interface.get_feedback()  # returns a dictionary with q, dq
#     u = ctrlr.generate(feedback['q'], feedback['dq'], target_xyz)
#     interface.send_forces(u)  # send forces and step VREP sim forward

# interface.disconnect()