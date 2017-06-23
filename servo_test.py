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
<<<<<<< HEAD
            elif event.code == "BTN_WEST":
                BrickPi.EncoderOffset[PORT_A] = BrickPi.Encoder[PORT_A]
=======
>>>>>>> 15504954d6808ce63e2aee6c1cda07329268d1f6
            elif event.code == "BTN_MODE":
                global quitting
                quitting = True
                return

gamepad = threading.Thread(target = gamepad)
gamepad.start()

while True:
    if isinstance( BrickPi.Encoder[PORT_A], int ) == True:
        pos_A = BrickPi.Encoder[PORT_A]
    BrickPi.MotorSpeed[PORT_A] = ( pos_gamepad - pos_A )
    BrickPiUpdateValues()
    if quitting == True:
        sys.exit()
