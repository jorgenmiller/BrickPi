from BrickPi import *

BrickPiSetup()
BrickPiSetupSensors()
BrickPi.MotorEnable[PORT_A] = 1
quitting = False
motorRotateDegree([255],[0],[PORT_A])

def gamepad():
    while True:
        for event in get_gamepad():
            elif event.code == "ABS_RX":
                BmotorRotateDegree([255],[event.state / 90],[PORT_A])
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
