from BrickPi import *

BrickPiSetup()

BrickPi.MotorEnable[PORT_A] = 1

while True:
    print ( BrickPi.Encoder[PORT_A] %720 ) /2
    BrickPiUpdateValues()
    time.sleep(.1)
