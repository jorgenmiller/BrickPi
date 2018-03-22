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
        print("got it")

        if goto > position:
            BrickPi.MotorSpeed[PORT_A] = 50
            print("up")
        elif goto < position:
            BrickPi.MotorSpeed[PORT_A] = -50
            print("down")
        else:
            BrickPi.MotorSpeed[PORT_A] = 0
            print("stay")

        while position < goto - 30 or position > goto + 30:
            print("again")
            BrickPiUpdateValues()
        BrickPi.MotorSpeed[PORT_A] = 0
        BrickPiUpdateValues()
        print("finished")

    except KeyboardInterrupt:
        break

    time.sleep(.1)
