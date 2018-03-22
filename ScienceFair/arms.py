import time
from BrickPi import *

BrickPiSetup()
BrickPiSetupSensors()

BrickPi.MotorEnable[PORT_A] = 1
BrickPi.EncoderOffset[PORT_A] = BrickPi.Encoder[PORT_A]

BrickPi.MotorEnable[PORT_B] = 1
BrickPi.EncoderOffset[PORT_B] = BrickPi.Encoder[PORT_B]

BrickPi.MotorEnable[PORT_C] = 1
BrickPi.EncoderOffset[PORT_C] = BrickPi.Encoder[PORT_C]

BrickPi.MotorEnable[PORT_D] = 1
BrickPi.EncoderOffset[PORT_D] = BrickPi.Encoder[PORT_D]

while True:
    try:
        goto = input("pos? 0-360: ")
        position = BrickPi.Encoder[PORT_A]

        if goto > position:
            BrickPi.MotorSpeed[PORT_A] = 50
        elif goto < position:
            BrickPi.MotorSpeed[PORT_A] = -50
        else:
            BrickPi.MotorSpeed[PORT_A] = 0

            while position < goto - 30 or position > goto + 30:
                BrickPiUpdateValues()
        BrickPi.MotorSpeed[PORT_A] = 0
        BrickPiUpdateValues()

    except KeyboardInterrupt:
        break

    time.sleep(.1)
