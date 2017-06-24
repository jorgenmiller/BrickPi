from BrickPi import *

BrickPiSetup()
BrickPiSetupSensors()
BrickPi.MotorEnable[PORT_A] = 1
BrickPi.EncoderOffset[PORT_A] = BrickPi.Encoder[PORT_A]

while True:
    try:
        print BrickPi.Encoder[PORT_A]
        BrickPiUpdateValues()
        time.sleep(.1)
    except KeyboardInterrupt:
        break
