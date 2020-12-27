# This is a list of callable functions for the servo going directly into the pi (signal pin being in GPIO 17 - Board number 11)

#Board pinouts servo  -> Pi
#V+(Orange) -> 5V (On Pi)
#GND(Brown) -> GND (On Pi)
#PWM(Yellow) -> GPIO 17/Pin 11

#imports
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT) # sets GPIO pin 11 as an output

pwm=GPIO.PWM(11, 50)
pwm.start(0)

def setAngle(angle): #goes to set angle (0-170)
    duty = angle / 18 + 3
    GPIO.output(11, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(11, False)
    pwm.ChangeDutyCycle(duty)

def left(): # go to the left
    setAngle(170)

def centre(): #go to neutral
    setAngle(90)

def right(): #got the right
    setAngle(0)

def exit(): #exit() will make usre there is a GPIO.cleanup() command
    pwm.stop()
    GPIO.cleanup()

def press(angle): # Press to set angle then go to neutral position
    setAngle(angle)
    time.sleep(0.01)
    setAngle(85)


def leftpress(): #where the servo is mounted on the left of the short push button (with the cables going upwards)
    press(70)

def rightpress(): #where the servo is mounted on the right of the short push button (with the cables going upwards)
    press(110)

def leftswitch(): #where the servo is mounted on the left of the switch (with the cables going upwards)
    press(70) # need to test what the perfect angle is NOT 70

def rightswitch(): #where the servo is mounted on the right of the switch (with the cables going upwards)
    press(110) # need to test what the perfect angle is NOT 110