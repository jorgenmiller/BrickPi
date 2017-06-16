from inputs import get_gamepad
while True:
    for event in get_gamepad():
        print(event, event.ev_type, event.code, event.state)
