#!/usr/bin/env python
import time
import sys
from gpiozero import Motor, OutputDevice, PhaseEnableMotor

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

    def __init__(self):
        # initialized all pins for output
        #GPIO.setmode(GPIO.BCM)
        #GPIO.setup(PINS, GPIO.OUT)
        #pwm = GPIO.PWM(PIN_FORWARD, 100)
        #pwm.start(0)
        self.drive_motor = Motor(PIN_FORWARD, PIN_AFT)
        self.turn_motor = Motor(PIN_RIGHT, PIN_LEFT)
        #self.pin_right = OutputDevice(PIN_RIGHT)
        #self.pin_left = OutputDevice(PIN_LEFT)

    def set_dir(self, dir):
        direction = DIRECTION.STRAIGHT
        #if dir > 0.3:
            #GPIO.output(PIN_RIGHT, 1)
            #GPIO.output(PIN_LEFT, 0)
            #self.pin_right.on()
            #self.pin_left.off()
        #elif dir < -0.3:
            #GPIO.output(PIN_RIGHT, 0)
            #GPIO.output(PIN_LEFT, 1)
            #self.pin_right.off()
            #self.pin_left.on()

        if dir > 0.1:
            self.turn_motor.forward(abs(dir))
        elif dir < -0.1:
            self.turn_motor.backward(abs(dir))
        else:
            self.turn_motor.stop()

        # set the correct on/off on the left and write pins
        #GPIO.output(DIRECTION_TO_PINS[direction][0], 0)
        #GPIO.output(DIRECTION_TO_PINS[direction][1], 1)

    def set_speed(self, speed=1.0):
        #spd = abs(speed)
        # drive forward for a single cycle
        #GPIO.output(PIN_FORWARD, 1)
        #time.sleep(CYCLE_TIME * spd)
        #GPIO.output(PIN_FORWARD, 0)
        #time.sleep(CYCLE_TIME * (1-spd))
        if speed > 0.1:
            self.drive_motor.forward(abs(speed))
        elif speed < -0.1:
            self.drive_motor.backward(abs(speed))
        else:
            self.drive_motor.stop()

Drive = DriveImpl()


