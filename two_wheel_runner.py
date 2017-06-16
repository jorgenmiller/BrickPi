from BrickPi import *
from inputs import get_gamepad
import threading

BrickPiSetup()
BrickPi.MotorEnable[PORT_B] = 1
BrickPi.MotorEnable[PORT_C] = 1

quitting = False

def gamepad():
    while True:
        for event in get_gamepad():
            if event.code == "ABS_RY":
                BrickPi.MotorSpeed[PORT_B] = event.state / 128
            elif event.code == "ABS_Y":
                BrickPi.MotorSpeed[PORT_C] = event.state / 128
            elif event.code == "BTN_MODE":
                global quitting
                quitting = True
                return

gamepad = threading.Thread(target = gamepad)
gamepad.start()

while True:
    BrickPiUpdateValues()
    if quitting == True:
        sys.exit()
