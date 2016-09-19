#!/usr/bin/python

import pifacedigitalio as pfd
from time import sleep

pf = pfd.PiFaceDigital()

power = pf.relays[0]
motor_on = power.turn_on
motor_off = power.turn_off

direction = pf.relays[1] # forward is turned off, retract is turned on
set_forward = direction.turn_off
set_reverse = direction.turn_on


def toggle_dir(event):
    direction.toggle()
    print 'changed direction'

def toggle_power(event):
    power.toggle()
    print 'changed power'


listener = pfd.InputEventListener(chip=pf)
listener.register(0, pfd.IODIR_FALLING_EDGE, toggle_power)
listener.register(1, pfd.IODIR_FALLING_EDGE, toggle_dir)
listener.activate()

set_forward()
sleep(0.05)
motor_on()
sleep(3)
motor_off()
sleep(1)

set_reverse()
sleep(0.05)
motor_on()
sleep(3)
motor_off()
sleep(0.05)
set_forward()
sleep(1)

listener.deactivate()
print 'done'
