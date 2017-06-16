from evdev import InputDevice, categorize, ecodes, KeyEvent
from BrickPi import *

motorScale = 128
vertValue = 0
sideValue = 0

BrickPiSetup()

BrickPi.MotorEnable[PORT_B] = 1
BrickPi.MotorEnable[PORT_C] = 1

gamepad = InputDevice("/dev/input/event2")

for event in gamepad.read_loop():

    if event.code == 3: # right joystick sideways

        print('side ',event.value)

        sideValue = event.value / motorScale

    elif event.code  == 4: # right joystick vertical

        print('vert ',event.value)

        vertValue = event.value / motorScale


    BrickPi.MotorSpeed[PORT_B] = vertValue
    BrickPi.MotorSpeed[PORT_C] = sideValue
    
    BrickPiUpdateValues()
