import time
from BrickPi import *

BrickPiSetup()
BrickPi.SensorType[PORT_1] = TYPE_SENSOR_RAW #analog sound sensor
BrickPiSetupSensors()

def good(soundlevel):
    return ( 1 - ( soundlevel / 1000 ) )

while True:
    try:

        BrickPiUpdateValues()
        print BrickPi.Sensor[PORT_1]
        print good(BrickPi.Sensor[PORT_1])
        print ( 1 - ( float(BrickPi.Sensor[PORT_1]) / 1000 ) )

    except KeyboardInterrupt:
        break

    time.sleep(.1)
