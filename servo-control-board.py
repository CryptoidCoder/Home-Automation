# This is a list of callable functions for the servo control board

#Board pinouts servo control board -> Pi
#VCC -> 3.3v (On Pi)
#SDA -> SDA/GPIO 2/Pin 2
#SCL -> SCL/GPIO 3/Pin 5
#GND -> GND (On Pi) 

#imports
from __future__ import division
import time
import Adafruit_PCA9685

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Configure min and max servo pulse lengths
servo_min = 90  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096
servo_middle = 400 # Middle pulse length out of 4096

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

def move(channel, angle):
    print('Moving servo ', channel, 'to angle of ', angle)
    pwm.set_pwm(channel, 0, angle)


def left(channel):
    pwm.set_pwm(channel, 0, servo_max)

def centre(channel):
    pwm.set_pwm(channel, 0, servo_middle)

def right(channel):
    pwm.set_pwm(channel, 0, servo_min)


def press(channel):
    pwm.set_pwm(channel, 0, 310)
    time.sleep(0.1)
    pwm.set_pwm(channel,0, servo_middle)

def test(channel):
    print("pressing ", channel)
    press(channel)
    time.sleep(1)
    print("left, ", channel)
    left(channel)
    time.sleep(1)
    print("right, ", channel)
    right(channel)
    time.sleep(1)
    print("centre, ", channel)
    centre(channel)
    time.sleep(1)

test(0)
test(1)