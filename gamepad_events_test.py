#for F310 as event2 in /dev/input


from evdev import InputDevice, categorize, ecodes, KeyEvent

def find_controller():

    event2 = InputDevice("/dev/input/event2")

    gamepad = event2

    return gamepad

gamepad = find_controller()



for event in gamepad.read_loop():
	print(event.code)
for event in gamepad.read_loop():
	print(event.value)
for event in gamepad.read_loop():

        if event.type == ecodes.EV_KEY:

            keyevent = categorize(event)

            if keyevent.keystate == KeyEvent.key_down:

                print(keyevent.keycode)