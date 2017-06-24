import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)    #LED near BrickPi power port
GPIO.setup(13, GPIO.OUT)    #LED above RPi LEDs
GPIO.output(12, True)

while True:
    try:
        GPIO.output(13, False)
        time.sleep(.5)
        GPIO.output(13, True)
        time.sleep(.5)

    except KeyboardInterrupt:
        GPIO.output(12, False)
        GPIO.output(13, False)
        GPIO.cleanup()
        break
