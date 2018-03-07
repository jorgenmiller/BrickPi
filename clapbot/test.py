import time
from BrickPi import *

BrickPiSetup()
BrickPi.SensorType[PORT_1] = TYPE_SENSOR_RAW #analog sound sensor
BrickPiSetupSensors()

def good(soundlevel):
    return ( 1 - ( float(soundlevel) / 1000 ) )

while True:
    try:

        BrickPiUpdateValues()
        print good(BrickPi.Sensor[PORT_1])

    except KeyboardInterrupt:
        break

    time.sleep(.1)
