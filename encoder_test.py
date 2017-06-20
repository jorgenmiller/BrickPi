from BrickPi import *

BrickPiSetup()
BrickPiSetupSensors()
BrickPi.MotorEnable[PORT_A] = 1

while True:
    print BrickPi.Encoder[PORT_A] / 2
    BrickPiUpdateValues()
    time.sleep(.1)
