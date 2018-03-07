import time
from BrickPi import *

BrickPiSetup()
BrickPi.SensorType[PORT_1] = TYPE_SENSOR_RAW #analog sound sensor
BrickPiSetupSensors()

claps = 0
previouslevels = []
currentpos = 0

for i in range(20):
    previouslevels.append(1000)
print previouslevels

while True:
    print currentpos
    currentpos += 1
    if currentpos == 15:
        currentpos = 0
    try:
        BrickPiUpdateValues()
    except KeyboardInterrupt:
        break
    time.sleep(.1)
