from abr_control.interfaces import PROSTHETIC_HAND
import time
import numpy as np

interface = PROSTHETIC_HAND()
interface.connect()


interface.get_feedback()

interface.send_forces([-150,-150,-150,-150])
time.sleep(2)

print(interface.get_feedback())

interface.send_forces([0,0,0,0])
