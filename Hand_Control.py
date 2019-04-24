from abr_control.arms import jaco2
from abr_control.controllers import OSC
from abr_control.interfaces import PROSTHETIC_HAND


# robot_config = jaco2.Config()
# ctrlr = OSC(robot_config)
interface = PROSTHETIC_HAND()

interface.connect()
while True: 
	feedback = interface.get_feedback()
	print feedback
	
# target_xyz = [.2, .2, .5]  # in metres
# for ii in range(1000):
#     feedback = interface.get_feedback()  # returns a dictionary with q, dq
#     u = ctrlr.generate(feedback['q'], feedback['dq'], target_xyz)
#     interface.send_forces(u)  # send forces and step VREP sim forward

# interface.disconnect()