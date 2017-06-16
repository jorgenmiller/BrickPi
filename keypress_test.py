from BrickPi import *
import readchar

BrickPiSetup()

BrickPi.MotorEnable[PORT_B] = 1
BrickPi.MotorEnable[PORT_C] = 1

while True:
	BrickPi.MotorSpeed[PORT_B] = 0
	BrickPi.MotorSpeed[PORT_C] = 0
	key = readchar.readkey()
	if (key == 'a'):
		print "a pressed"
		BrickPi.MotorSpeed[PORT_B] = 200

	if(key == 'd'):
		print "d pressed"
		BrickPi.MotorSpeed[PORT_C] = 200
	BrickPiUpdateValues()