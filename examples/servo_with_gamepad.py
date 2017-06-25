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




class ThreadClass(threading.Thread):
        def gamepad():
            print "loop"
            for event in get_gamepad():
                if event.code == "ABS_RX":
                    global pos_gamepad
                    pos_gamepad = event.state / 90
                elif event.code == "BTN_MODE":
                    global quitting
                    quitting = True
                    return

while True:
    gamepad.start()
    try:
        if isinstance( BrickPi.Encoder[PORT_A], int ) == True:
            pos_A = BrickPi.Encoder[PORT_A]
            BrickPi.MotorSpeed[PORT_A] = ( pos_gamepad - pos_A )
            BrickPiUpdateValues()
        elif quitting == True:
            sys.exit()
    except KeyboardInterrupt:
        print "interrupt"
        gamepad.join()
        print "interrupted"
        break
