import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

def blinkS ():
    GPIO.output(4, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(4, GPIO.LOW)
    time.sleep(1)
    GPIO.output(4, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(4, GPIO.LOW)
    time.sleep(1)
    GPIO.output(4, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(4, GPIO.LOW)


def blinkO ():
    GPIO.output(4, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(4, GPIO.LOW)
    time.sleep(1)
    GPIO.output(4, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(4, GPIO.LOW)
    time.sleep(1)
    GPIO.output(4, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(4, GPIO.LOW)


while True:
    blinkS()
    blinkO()
    blinkS()