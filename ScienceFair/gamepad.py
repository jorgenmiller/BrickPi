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

speed = 255

while True:
    try:
        BrickPi.MotorSpeed[PORT_A] = 0
        BrickPi.MotorSpeed[PORT_B] = 0
        BrickPi.MotorSpeed[PORT_C] = 0
        BrickPi.MotorSpeed[PORT_D] = 0
        BrickPiUpdateValues()
        txt = input("input: ")

        if txt == "1":
            BrickPi.MotorSpeed[PORT_A] = speed
        elif txt == "2":
            BrickPi.MotorSpeed[PORT_A] = -1 * speed
        elif txt == "3":
            BrickPi.MotorSpeed[PORT_B] = speed
        elif txt == "4":
            BrickPi.MotorSpeed[PORT_B] = -1 * speed
        elif txt == "5":
            BrickPi.MotorSpeed[PORT_C] = speed
        elif txt == "6":
            BrickPi.MotorSpeed[PORT_C] = -1 * speed
        elif txt == "7":
            BrickPi.MotorSpeed[PORT_D] = speed
        elif txt == "8":
            BrickPi.MotorSpeed[PORT_D] = -1 * speed

        BrickPiUpdateValues()

    except KeyboardInterrupt:
        break

    time.sleep(1)
