from BrickPi import *

BrickPiSetup()
BrickPi.SensorType[PORT_1] = TYPE_SENSOR_ULTRASONIC_CONT #ultrasonic sensor
BrickPiSetupSensors()

while True:
    BrickPiUpdateValues()
    print BrickPi.Sensor[PORT_1] #print the output (0-close, 255-far) in cm
