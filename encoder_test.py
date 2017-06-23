from BrickPi import *

BrickPiSetup()
BrickPiSetupSensors()
BrickPi.MotorEnable[PORT_A] = 1
BrickPi.EncoderOffset[PORT_A] = BrickPi.Encoder[PORT_A]

while True:
    print BrickPi.Encoder[PORT_A]
    BrickPiUpdateValues()
    time.sleep(.1)
