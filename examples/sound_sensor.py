from BrickPi import *

BrickPiSetup()
BrickPi.SensorType[PORT_1] = TYPE_SENSOR_RAW #analog sound sensor
BrickPiSetupSensors()

while True:
    try:
        BrickPiUpdateValues()
        print BrickPi.Sensor[PORT_1] #print the output (1000-quiet, 0-loud)
    except KeyboardInterrupt:
        break
