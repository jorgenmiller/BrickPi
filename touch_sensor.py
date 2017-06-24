from BrickPi import *

BrickPiSetup()
BrickPi.SensorType[PORT_2] = TYPE_SENSOR_TOUCH_DEBOUNCE #touch sensor
BrickPiSetupSensors()

while True:
    BrickPiUpdateValues()
    print BrickPi.Sensor[PORT_2] #print the output (0-not pressed, 1-pressed)
