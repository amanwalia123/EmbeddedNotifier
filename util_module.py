
from lcd import *
import RPi.GPIO as GPIO


########################################################
hasNOTIFICATION = False
pin_1 = 2
pin_2 = 3
pin_3 = 4

# GPIO pin 18 controlling LED
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin_1,GPIO.OUT)
GPIO.setup(pin_2,GPIO.OUT)
GPIO.setup(pin_3,GPIO.OUT)

def RED():
    GPIO.output(pin_1,1)
    GPIO.output(pin_2,0)
    GPIO.output(pin_3,0)

def BLUE():
    GPIO.output(pin_1,0)
    GPIO.output(pin_2,1)
    GPIO.output(pin_3,0)

def GREEN():
    GPIO.output(pin_1,0)
    GPIO.output(pin_2,0)
    GPIO.output(pin_3,1)

def CYAN():
    GPIO.output(pin_1,0)
    GPIO.output(pin_2,1)
    GPIO.output(pin_3,1)

def PURPLE():
    GPIO.output(pin_1,1)
    GPIO.output(pin_2,0)
    GPIO.output(pin_3,1)

def YELLOW():
    GPIO.output(pin_1,1)
    GPIO.output(pin_2,1)
    GPIO.output(pin_3,0)

def WHITE():
    GPIO.output(pin_1,1)
    GPIO.output(pin_2,1)
    GPIO.output(pin_3,1)

def OFF():
    GPIO.output(pin_1,0)
    GPIO.output(pin_2,0)
    GPIO.output(pin_3,0)

def turn_LEDS():
    while True:
        if hasNOTIFICATION:
            RED();
            time.sleep(0.05)
            BLUE();
            time.sleep(0.05)
            GREEN();
            time.sleep(0.05)
            CYAN();
            time.sleep(0.05)
            PURPLE();
            time.sleep(0.05)
            YELLOW();
            time.sleep(0.05)
            WHITE();
            time.sleep(0.05)
########################################################