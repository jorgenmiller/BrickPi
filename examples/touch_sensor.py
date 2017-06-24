from BrickPi import *

BrickPiSetup()
BrickPi.SensorType[PORT_1] = TYPE_SENSOR_TOUCH_DEBOUNCE #touch sensor
BrickPiSetupSensors()

while True:
    try:
        BrickPiUpdateValues()
        print BrickPi.Sensor[PORT_1] #print the output (0-not pressed, 1-pressed)
    except KeyboardInterrupt:
        break
