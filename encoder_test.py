from BrickPi import *

BrickPiSetup()
BrickPiSetupSensors()
BrickPi.MotorEnable[PORT_A] = 1

while True:
    pos = BrickPi.Encoder[PORT_A]
    print pos / 2
    BrickPiUpdateValues()
    time.sleep(.1)
