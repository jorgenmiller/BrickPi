from BrickPi import *

BrickPiSetup()
BrickPi.SensorType[PORT_1] = TYPE_SENSOR_RAW #analog sound sensor
BrickPiSetupSensors()

max = 1000

while True:
    try:
        BrickPiUpdateValues()
        soundlevel = BrickPi.Sensor[PORT_1]
        if soundlevel < max:
            max = soundlevel
            print max #print the output (1000-quiet, 0-loud)
    except KeyboardInterrupt:
        break
