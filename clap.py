from BrickPi import *

BrickPiSetup()
BrickPi.SensorType[PORT_1] = TYPE_SENSOR_RAW #analog sound sensor
BrickPiSetupSensors()

claps = 0
previouslevel = 1000

while True:
    try:
        BrickPiUpdateValues()
        soundlevel = BrickPi.Sensor[PORT_1]
        if soundlevel <= previouslevel - 800:
            claps += 1
        print soundlevel + "        " + claps
        previouslevel = soundlevel
    except KeyboardInterrupt:
        break
