import time
from BrickPi import *

BrickPiSetup()
BrickPi.SensorType[PORT_1] = TYPE_SENSOR_RAW #analog sound sensor
BrickPiSetupSensors()

claps = 0
previouslevels = []

for i in range(15):
    print i
while True:
    try:
        BrickPiUpdateValues()
        soundlevel = BrickPi.Sensor[PORT_1]
        if soundlevel <= previouslevel - 800:
            claps += 1
        print str(soundlevel) + "        " + str(claps)
        previouslevel = soundlevel
    except KeyboardInterrupt:
        break
    time.sleep(.1)
