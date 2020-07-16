#!/usr/bin/env python
import time
import sys

import RPi.GPIO as GPIO

PIN_FORWARD = 16
PIN_AFT = 26
PIN_LEFT = 20
PIN_RIGHT = 21

PINS = [PIN_FORWARD, PIN_AFT, PIN_LEFT, PIN_RIGHT]

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

class DriveImpl(object):

    def __init__():
        # initialized all pins for output
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(PINS, GPIO.OUT)

    def set_dir(direction):
        # set the correct on/off on the left and write pins
        GPIO.output(DIRECTION_TO_PINS[direction][0], 0)
        GPIO.output(DIRECTION_TO_PINS[direction][1], 1)

    def set_speed(spd=1.0):
        # drive forward for a single cycle
        GPIO.output(PIN_FORWARD, 1)
        time.sleep(CYCLE_TIME * spd)
        GPIO.output(PIN_FORWARD, 0)
        time.sleep(CYCLE_TIME * (1-spd))

Drive = DriveImpl()


