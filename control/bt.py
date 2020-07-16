#import evdev
from evdev import InputDevice, categorize, ecodes


class ControlsImpl(object):
    def __init__():
        pass

    def setup():
        #creates object 'gamepad' to store the data
        #you can call it whatever you like
        self.gamepad = InputDevice('/dev/input/event0')

        #prints out device info at start
        print(gamepad)

    def run_loop(onkey, onspped, ondir):
        #evdev takes care of polling the controller in a loop
        for event in gamepad.read_loop():
            #print(categorize(event))
            if event.type == ecodes.EV_KEY:
                if event.value == 1: # down
                    if event.code == ecodes.BTN_B:
                        if not onkey("B"):
                            break
                    elif event.code == ecodes.BTN_A:
                        if not onkey("A"):
                            break
                    elif event.code == ecodes.BTN_Y:
                        if not onkey("Y"):
                            break
                    elif event.code == ecodes.BTN_X:
                        if not onkey("X"):
                            break
            elif event.type == ecodes.EV_ABS:
                value = event.value
                if event.code == ecodes.ABS_X:
                    if not ondir(value)
                        break
                elif event.code == ecodes.ABS_Y:
                    if not onspeed(value)
                        break

Controls = ControlsImpl()
