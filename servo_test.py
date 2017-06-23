from inputs import get_gamepad
from BrickPi import *
import threading

BrickPiSetup()
BrickPiSetupSensors()
BrickPi.MotorEnable[PORT_A] = 1
BrickPi.EncoderOffset[PORT_A] = BrickPi.Encoder[PORT_A]
quitting = False
pos_A = 0
pos_gamepad = 0

def gamepad():
    while True:
        for event in get_gamepad():
            if event.code == "ABS_RX":
                global pos_gamepad
                pos_gamepad = event.state / 90
                print pos_gamepad
            elif event.code == "BTN_MODE":
                global quitting
                quitting = True
                return

gamepad = threading.Thread(target = gamepad)
gamepad.start()

while True:
    BrickPi.Encoder[PORT_A] = pos_A
    BrickPiUpdateValues()
    if quitting == True:
        sys.exit()
