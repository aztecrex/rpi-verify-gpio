# Just see if we can get the PI to drive
# anything through the GPIO header


import RPi.GPIO as GPIO
import time

# LED channel
led_channel = 21
switch_channel = 26

# how many times to flash
flashes = 20

# how many seconds to stay on and off
on_duration = .1
off_duration = .1

GPIO.setmode(GPIO.BCM)

GPIO.setup(led_channel, GPIO.OUT)
GPIO.setup(switch_channel, GPIO.IN)

GPIO.wait_for_edge(switch_channel, GPIO.FALLING)

for i in range(flashes):
    GPIO.output(led_channel,GPIO.HIGH)
    time.sleep(on_duration)
    GPIO.output(led_channel,GPIO.LOW)
    time.sleep(off_duration)
GPIO.cleanup()

