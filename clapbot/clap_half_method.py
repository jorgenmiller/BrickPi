import time
from BrickPi import *


BrickPiSetup()
BrickPi.SensorType[PORT_1] = TYPE_SENSOR_RAW #analog sound sensor
BrickPiSetupSensors()


def checkSoundLevel():
    BrickPiUpdateValues()
    soundlevel = float(BrickPi.Sensor[PORT_1])
    return 1 - ( soundlevel / 1000 )    #1 is loud, 0 is quiet

def average(list):
    sum = float(0)
    for n in list:
        sum += n
    average = (sum / len(list))
    return average


previous_sound_levels = []
current_pos = 0
sound_in_row = 0
claps = 0

for i in range(50):
    previous_sound_levels.append(checkSoundLevel())
    time.sleep(.05)
print "go!"

while True:
    try:
        current_sound_level = checkSoundLevel()
        past_average = average(previous_sound_levels)

        if current_sound_level >= ( 1 + ( past_average / 2 ) ) / 2: #halfway between past_average and 1 (loud)
            if sound_in_row == 0:
                claps += 1
                print "clap ", claps
            sound_in_row += 1

        else:
            previous_sound_levels[current_pos] = current_sound_level
            current_pos += 1
            if current_pos == len(previous_sound_levels):
                current_pos = 0
            sound_in_row = 0

#        print previous_sound_levels
#        print str(past_average), " - ", (current_sound_level)

    except KeyboardInterrupt:
        break

    time.sleep(.1)
