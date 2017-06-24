from BrickPi import *

BrickPiSetup()
BrickPi.SensorType[PORT_4] = TYPE_SENSOR_LIGHT_OFF #light sensor
#TYPE_SENSOR_LIGHT_OFF      measure amount of ambient light
#TYPE_SENSOR_LIGHT_ON       measure amount of reflected light
BrickPiSetupSensors()

while True:
    BrickPiUpdateValues()
    print BrickPi.Sensor[PORT_4] #print the output (0-bright, 100-dim)
