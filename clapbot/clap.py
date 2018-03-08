import time
from BrickPi import *


BrickPiSetup()
BrickPi.SensorType[PORT_1] = TYPE_SENSOR_RAW #analog sound sensor
BrickPiSetupSensors()


def checkSoundLevel():
    BrickPiUpdateValues()
    soundlevel = float(BrickPi.Sensor[PORT_1])
    return 1 - ( soundlevel / 1000 )

def average(list):
    sum = float(0)
    for n in list:
        sum += n
    average = (sum / len(list))
    return average

def standardDeviation(list):
    sum_deviation = 0
    for n in list:
        sum_deviation += ( n - average(list)) ** 2
    standard_deviation = ( sum_deviation / len(list) ) ** .5
    return standard_deviation

def zScore(test_value, list):
    z_score = (test_value - average(list)) / standardDeviation(list)
    return z_score


previous_sound_levels = []
current_pos = 0


for i in range(40):
    previous_sound_levels.append(checkSoundLevel())


while True:
    try:
        current_sound_level = checkSoundLevel()
        past_average = average(previous_sound_levels)

        if zScore(current_sound_level, previous_sound_levels) >= 3:
            print "clap!"
        else:
            current_pos += 1
            if current_pos == len(previous_sound_levels):
                current_pos = 0

#        print previous_sound_levels
#        print str(past_average), " - ", (current_sound_level)

    except KeyboardInterrupt:
        break

    time.sleep(.2)
