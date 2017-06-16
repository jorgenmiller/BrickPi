from inputs import get_gamepad
from BrickPi import *
import threading
import sys

BrickPiSetup()
BrickPi.MotorEnable[PORT_B] = 1
BrickPi.MotorEnable[PORT_C] = 1

def brickpi():
    while True:
        BrickPiUpdateValues()

brickpi = threading.Thread(target = brickpi)
brickpi.start()

while True:
    for event in get_gamepad():
        if event.code == "ABS_RX":
            BrickPi.MotorSpeed[PORT_B] = event.state / 128
        elif event.code == "ABS_RY":
            BrickPi.MotorSpeed[PORT_C] = event.state / 128
        elif event.code == "BTN_MODE":
            print "see ya"
            break
sys.exit()
