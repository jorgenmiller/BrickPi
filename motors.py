
from inputs import get_gamepad

events = get_gamepad()

for event in events:
    events = get_gamepad()
    print "loop"
    if event.code == "BTN_WEST":
        print "pushed"
    else:
        print "stopped"
        
    
