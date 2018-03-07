import time
from BrickPi import *

BrickPiSetup()
BrickPi.SensorType[PORT_1] = TYPE_SENSOR_RAW #analog sound sensor
BrickPiSetupSensors()

claps = 0
previouslevels = []

for i in range(15):
    previouslevels.append(1000)
print previouslevels

while True:
    try:
        BrickPiUpdateValues()
    except KeyboardInterrupt:
        break
    time.sleep(.1)
