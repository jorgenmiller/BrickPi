from evdev import InputDevice, categorize, ecodes, KeyEvent

def find_controller():

    event2 = InputDevice("/dev/input/event2")

    gamepad = event2

    return gamepad

gamepad = find_controller()


for event in gamepad.read_loop():

    x = event.code

    #print(event)

    if x == 2:

        print('left wheels fw')

    elif x == 5:

        print('right wheels fw')

    elif x == 310:

        print('left wheels back')

    elif x == 311:

        print('right wheels back')

    elif x == 3:

        y = event.value

        if y > 0:

            print('pan right')

        else:

                  print('pan left')

    elif x == 0:

        y = event.value

        if y > 0:

            print 'left ' , y

            #move(y / 40, 'right', False)

        elif y < 0:
                  print 'right ' , (y*-1)
                  #move((y * -1) / 40, 'left', False)
    elif x == 1:
        y = event.value
        if y > 0:

            print 'back', y

        else:

                  print 'fwd', (y * -1)

    elif x == 4:

        y = event.value

        if y > 0:

            print('tilt fwd')

        else:

                  print('tilt back')

    elif x == 314:

        print('quit')

        break

    elif x == 315:

        print('servo reset')