from BrickPi import *
import curses, time

BrickPiSetup()

BrickPi.MotorEnable[PORT_B] = 1
BrickPi.MotorEnable[PORT_C] = 1

BrickPiSetupSensors()

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

key = ''
while True:
	key = stdscr.getch()
	BrickPi.MotorSpeed[PORT_B] = 0
	if key == curses.KEY_LEFT :
		BrickPi.MotorSpeed[PORT_B] = 200
	BrickPiUpdateValues()