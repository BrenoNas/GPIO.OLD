#!/usr/bin/env python
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

SPEAKER = 18

GPIO.setup(SPEAKER,GPIO.OUT)

pwmSPEAKER = GPIO.PWM(SPEAKER, 440)
pwmSPEAKER.start(50)

try:
    while True:
        for freq in range(500,1001, 1):
            pwmSPEAKER.ChangeFrequency(freq)
            sleep(0.001)
        for freq in range(1000, 499, -1):
            pwmSPEAKER.ChangeFrequency(freq)
            sleep(0.001)
except KeyboardInterrupt:
    pwmSPEAKER.stop()
    GPIO.cleanup()
exit()
