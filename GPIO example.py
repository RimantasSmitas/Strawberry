# External module imports
import RPi.GPIO as GPIO

# Pin Definitons:
butPin = 17 # Broadcom pin 17 (P1 pin 11)
ledPin = 23 # Broadcom pin 23 (P1 pin 16)

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
GPIO.setup(ledPin, GPIO.OUT) # LED pin set as output

# PROGRAM
A = GPIO.input(butPin)
if (A == 1):
 print ("Button not pressed")
 GPIO.output(ledPin, GPIO.LOW)
else:
    print ("Button is pressed")
    GPIO.output(ledPin, GPIO.HIGH)