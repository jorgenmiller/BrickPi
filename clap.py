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

for i in range(100):
    previouslevels.append(1000)

while True:
    try:

        BrickPiUpdateValues()
        currentlevel = BrickPi.Sensor[PORT_1]
        pastaverage = average(previouslevels)

        if currentlevel <= pastaverage + 100:
            previouslevels[currentpos] = currentlevel
            currentpos += 1
            if currentpos == 100:
                currentpos = 0
        else:
            print "clap!"

        print perviouslevels
        print str(pastaverage) + " - " + str(currentlevel)

    except KeyboardInterrupt:
        break
    time.sleep(.1)
