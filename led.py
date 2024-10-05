import RPi.GPIO as GPIO
import time

def marioStart():
    pwm_green.ChangeDutyCycle(100)
    time.sleep(1)
    pwm_yellow.ChangeDutyCycle(100)
    time.sleep(1)
    pwm_red.ChangeDutyCycle(100)
    time.sleep(0.5)
    pwm_green.ChangeDutyCycle(0)
    pwm_yellow.ChangeDutyCycle(0)
    pwm_red.ChangeDutyCycle(0)
    time.sleep(0.5)
    pwm_green.ChangeDutyCycle(100)
    pwm_yellow.ChangeDutyCycle(100)
    pwm_red.ChangeDutyCycle(100)
    time.sleep(0.5)
    pwm_green.ChangeDutyCycle(0)
    pwm_yellow.ChangeDutyCycle(0)
    pwm_red.ChangeDutyCycle(0)

def traffic_light():
    pwm_green.ChangeDutyCycle(100)
    time.sleep(3)
    pwm_green.ChangeDutyCycle(0)
    pwm_yellow.ChangeDutyCycle(100)
    time.sleep(1)
    pwm_yellow.ChangeDutyCycle(0)
    pwm_red.ChangeDutyCycle(100)
    time.sleep(2)
    pwm_green.ChangeDutyCycle(0)
    pwm_yellow.ChangeDutyCycle(0)
    pwm_red.ChangeDutyCycle(0)
    

#Setting board mode
GPIO.setmode(GPIO.BOARD)

#For the circuits we are going to use pin 7,13 and 19
pins = [7, 13, 19]

#Initializing pins to board
for pin in pins:
#Since its a led (and we only send values to it)we are going to set OUT parameter
    GPIO.setup(pin,GPIO.OUT)

#Setting all pins to 1000hz
pwm_green = GPIO.PWM(7,1000)
pwm_yellow = GPIO.PWM(13,1000)
pwm_red = GPIO.PWM(19,1000)

#To use its 50% capacity
pwm_green.start(0)
pwm_yellow.start(0)
pwm_red.start(0)

marioStart()
traffic_light()

#We stop the light
pwm_green.stop()
pwm_yellow.stop()
pwm_red.stop()

#To close the pins again 
#if not, it will show a warning saying that the pin is already in use
GPIO.cleanup