#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

pin = [5, 6, 13, 19]
forward_sq = ['0011', '1001', '1100', '0110']
reverse_sq = ['0110', '1100', '1001', '0011']

class motorcontrol:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
 
        pin = [5, 6, 13, 19]
        for i in range(4):
            GPIO.setup(pin[i], GPIO.OUT)
 
        forward_sq = ['0011', '1001', '1100', '0110']
        reverse_sq = ['0110', '1100', '1001', '0011']
 
    def forward(self,steps, delay):
        for i in range(steps):
            for step in forward_sq:
                self.set_motor(step)
                time.sleep(delay)
 
    def reverse(self,steps, delay):
        for i in range(steps):
            for step in reverse_sq:
                self.set_motor(step)
                time.sleep(delay)
 
    def set_motor(self,step):
        for i in range(4):
            GPIO.output(pin[i], step[i] == '1')

          




"""

mot = motorcontrol()
 
mot.set_motor('0000')
mot.forward(20, 0.01)
mot.set_motor('0000')
mot.reverse(20,0.01)

GPIO.cleanup()

"""






