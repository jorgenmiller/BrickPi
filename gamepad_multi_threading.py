from inputs import get_gamepad
from BrickPi import *
import threading

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
        if event.code == "BTN_WEST":
            BrickPi.MotorSpeed[PORT_B] = event.state * 255
