from inputs import get_gamepad
from BrickPi import *
import threading

BrickPiSetup()
BrickPi.MotorEnable[PORT_A] = 1
BrickPi.MotorEnable[PORT_B] = 1
BrickPi.MotorEnable[PORT_C] = 1
BrickPi.MotorEnable[PORT_D] = 1

quitting = False

def gamepad():
    while True:
        for event in get_gamepad():
            if event.code == "ABS_Y":
                BrickPi.MotorSpeed[PORT_B] = event.state / 128
                BrickPi.MotorSpeed[PORT_C] = event.state / 128
            elif event.code == "ABS_RX":
                BrickPi.MotorSpeed[PORT_A] = event.state / -260
                BrickPi.MotorSpeed[PORT_D] = event.state / 260
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
