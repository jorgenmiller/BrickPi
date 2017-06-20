from inputs import get_gamepad
from BrickPi import *
import threading

BrickPiSetup()
BrickPiSetupSensors()
BrickPi.MotorEnable[PORT_A] = 1
quitting = False
pos_A = 0
pos_gamepad = 0
motorRotateDegree([255],[0],[PORT_A])

def gamepad():
    while True:
        for event in get_gamepad():
            if event.code == "ABS_RX":
                pos_A = event.state / 90
            elif event.code == "BTN_MODE":
                global quitting
                quitting = True
                return

gamepad = threading.Thread(target = gamepad)
gamepad.start()

while True:
    BrickPi.Encoder[PORT_A] = pos_gamepad
    if pos_A > pos_gamepad + 10:
        BrickPi.MotorSpeed[PORT_A] = -50
        print "greater"
    elif pos_A < pos_gamepad - 10:
        BrickPi.MotorSpeed[PORT_A] = 50
        print "less"
    for pos_A in range(pos_gamepad - 10, pos_gamepad + 10):
        BrickPi.MotorSpeed[PORT_A] = 0
        print "equal"
    BrickPiUpdateValues()
    if quitting == True:
        sys.exit()
