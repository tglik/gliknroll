import time
import sys

import RPi.GPIO as GPIO

PIN_FORWARD = 29
PIN_AFT = 28
PIN_LEFT = 27
PIN_RIGHT = 25

PINS = [PIN_FORWARD, PIN_AFT, PIN_LEFT, PIN_RIGHT]
# initialized all pins for output
GPIO.setup(PINS, GPIO.OUT)

CYCLE_TIME = 0.1


class DIRECTION:
    STRAIGHT = 1
    LEFT = 2
    RIGHT = 3


# map from direction to which pins should be off and which should be on
DIRECTION_TO_PINS = {
    DIRECTION.STRAIGHT: ([PIN_LEFT, PIN_RIGHT], []),
    DIRECTION.RIGHT: ([PIN_LEFT], [PIN_RIGHT]),
    DIRECTION.LEFT: ([PIN_RIGHT], PIN_LEFT),
}


def go(direction):
    # set the correct on/off on the left and write pins
    GPIO.output(DIRECTION_TO_PINS[direction][0], 0)
    GPIO.output(DIRECTION_TO_PINS[direction][1], 1)

    # drive forward for a single cycle
    GPIO.output(PIN_FORWARD, 1)
    time.sleep(CYCLE_TIME)
    GPIO.output(PIN_FORWARD, 0)


if __name__ == "__main__":
    dir_map = {
        "F": DIRECTION.STRAIGHT,
        "L": DIRECTION.LEFT,
        "R": DIRECTION.RIGHT,
    }
    if len(sys.argv) != 2 or sys.argv[1] not in dir_map:
        print "Usage: drive [F/L/R]"

    go(dir_map[sys.argv[1]])