from BrickPi import *

BrickPiSetup()
BrickPiSetupSensors()
BrickPi.MotorEnable[PORT_A] = 1

BrickPi.offset_motor_encoder = BrickPi.Encoder[PORT_A]
motorRotateDegree([25],[0],[PORT_A],0)
print "0"
motorRotateDegree([25],[360],[PORT_A],0)
print "255"

while True:
    print BrickPi.Encoder[PORT_A]
    BrickPiUpdateValues()
    time.sleep(.1)
