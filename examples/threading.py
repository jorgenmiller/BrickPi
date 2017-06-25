from inputs import get_gamepad
import threading

position = 0

def gamepad():
    while True:
        for event in get_gamepad():
            if event.code == "ABS_Y":
                position = event.state

gamepad = threading.Thread(target = gamepad)
gamepad.daemon = True
gamepad.start()

while True:
    print position
