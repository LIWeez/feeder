"""

import RPi.GPIO as GPIO
import time
import sys
from hx711 import HX711
import motorcontrol
import datetime
from firebase import firebase
from motorcontrol import motorcontrol

pin = [5, 6, 13, 19]
forward_sq = ['0011', '1001', '1100', '0110']
reverse_sq = ['0110', '1100', '1001', '0011']


mot = motorcontrol()
hx = HX711(21,20)


\
hx.set_reading_format("LSB", "MSB")
hx.set_reference_unit(465)
hx.reset()
hx.tare()
presentweight = hx.get_weight(5)
print presentweight
hx.power_down()
hx.power_up()
GPIO.cleanup()
\
executeweight = 30
presentweight = 0
hx.set_reading_format("LSB", "MSB")
hx.set_reference_unit(465)
hx.reset()
hx.tare()
while presentweight < executeweight:


    for i in range(4):
        GPIO.setup(pin[i], GPIO.OUT)
    mot.set_motor('0000')
    mot.forward(45, 0.01)
    
    for i in range(7):
        presentweight = hx.get_weight(5)
    print presentweight
    hx.power_down()
    hx.power_up()

mot.set_motor('0000')

for i in range(30):
    time.sleep(1)
    print (30-i)

for i in range(7):
        presentweight = hx.get_weight(5)
hx.power_down()
hx.power_up()
print presentweight

resultput = firebase.put('/resttime',str(datetime.datetime.now().strftime('%H:%M:%S')),{ "time" : str(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')), "weight" : presentweight })

"""


# test motorcontrll

import RPi.GPIO as GPIO
import time
import sys

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

          
def cleanAndExit():
    print "Cleaning..."
    GPIO.cleanup()
    print "Bye!"
    sys.exit()
    











while True:
    try:

        mot = motorcontrol()
 
        mot.set_motor('0000')
        mot.forward(30, 0.01)
        #mot.set_motor('0000')
        #mot.reverse(132,0.01)

        #GPIO.cleanup()  


        
    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()



        
    




