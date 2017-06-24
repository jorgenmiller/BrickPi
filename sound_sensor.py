from BrickPi import *

BrickPiSetup()
BrickPi.SensorType[PORT_3] = TYPE_SENSOR_RAW #analog sound sensor
BrickPiSetupSensors()

while True:
    BrickPiUpdateValues()
    print BrickPi.Sensor[PORT_3] #print the output (1000-quiet, 0-loud)
