from BrickPi import *

BrickPiSetup()
BrickPiSetupSensors()
BrickPi.MotorEnable[PORT_A] = 1

motorRotateDegree([255],[0],[PORT_A])
print "0"
time.sleep(1)
motorRotateDegree([255],[720],[PORT_A])
print "255"

while True:
    print BrickPi.Encoder[PORT_A]
    BrickPiUpdateValues()
    time.sleep(.1)
