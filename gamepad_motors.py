from inputs import get_gamepad
from BrickPi import *

BrickPiSetup()
BrickPi.MotorEnable[PORT_B] = 1

while True:
    print 1
    events = get_gamepad()
    for event in events:
        print 2
        if event.ev_type != "Sync":
            print 3
            if event.code == "BTN_WEST":
                print 4
                if event.state == 1:
                    print 5
        else: 
            break
