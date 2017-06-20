from BrickPi import *

BrickPiSetup()

BrickPi.MotorEnable[PORT_A] = 1

while True:
    print ( BrickPi.Encoder[PORT_A] %720 ) /2
    time.sleep(.1)
