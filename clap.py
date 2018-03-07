import time
from BrickPi import *

BrickPiSetup()
BrickPi.SensorType[PORT_1] = TYPE_SENSOR_RAW #analog sound sensor
BrickPiSetupSensors()

def average(previouslevels):
    sum = 0
    for level in previouslevels:
        sum += level
    average = sum / len(previouslevels)
    return average

claps = 0
previouslevels = []
currentpos = 0

for i in range(20):
    previouslevels.append(1000)

while True:
    try:

        BrickPiUpdateValues()

        previouslevels[currentpos] = BrickPi.Sensor[PORT_1]

        print average(previouslevels)

        currentpos += 1
        if currentpos == 20:
            currentpos = 0

        print previouslevels

    except KeyboardInterrupt:
        break
    time.sleep(.1)
