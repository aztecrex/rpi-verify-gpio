# Just see if we can get the PI to drive
# anything through the GPIO header


import RPi.GPIO as GPIO
import time

# LED channel
channel = 21

# how many times to flash
flashes = 20

# how many seconds to stay on and off
on_duration = .1
off_duration = .1

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

for i in range(flashes):
    GPIO.output(channel,GPIO.HIGH)
    time.sleep(on_duration)
    GPIO.output(channel,GPIO.LOW)
    time.sleep(off_duration)
GPIO.cleanup()

