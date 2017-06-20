from inputs import get_gamepad
from BrickPi import *
import threading

BrickPiSetup()
BrickPiSetupSensors()
BrickPi.MotorEnable[PORT_A] = 1
quitting = False
pos_A = 0
motorRotateDegree([255],[0],[PORT_A])

def gamepad():
    while True:
        for event in get_gamepad():
            if event.code == "ABS_RX":
                pos_A = event.state / 90
                print pos_A
                motorRotateDegree([255],[pos_A],[PORT_A])
            elif event.code == "BTN_MODE":
                global quitting
                quitting = True
                return

gamepad = threading.Thread(target = gamepad)
gamepad.start()

while True:
    BrickPiUpdateValues()
    print BrickPi.Encoder[PORT_A]
    if quitting == True:
        sys.exit()
