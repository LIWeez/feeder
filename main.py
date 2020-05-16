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
firebase = firebase.FirebaseApplication('https://myapplication-84cfa.firebaseio.com', None)

mintime =86399
statu = "on"
executetime = "0"
executeweight = 0
executeitem = "0"
presentweight = 0
presentminsecond = 100
extime = False
ni = False

# initialize weight sensor
hx.set_reading_format("LSB", "MSB")
hx.set_reference_unit(465)
hx.reset()
hx.tare()
checkweight = hx.get_weight(5)
hx.power_down()
hx.power_up()
while checkweight < -5 or checkweight > 5 :
    hx.set_reading_format("LSB", "MSB")
    hx.set_reference_unit(465)
    hx.reset()
    hx.tare()
    checkweight = hx.get_weight(5)
    hx.power_down()
    hx.power_up()

while True:
    #check the scheduled time
    print ("check %d")%presentminsecond
    if presentminsecond < 2:
        statu = "off"
    if statu == "on":
        print ("catch")
        #get firebase SettingTime data array
        json_array = firebase.get('FdSet', None)

        for item in json_array :
            print ("loading...")
            #get time of each index in array  
            timeget = firebase.get('FdSet/', item)

            # calculate the interval seconds between settime and current time
            Fsettime= datetime.datetime.strptime(timeget["time"],"%H:%M" )
            presenttime = datetime.datetime.strptime(datetime.datetime.now().strftime('%H:%M:%S'),"%H:%M:%S")
            presentsecond = (Fsettime - presenttime).seconds

            if extime == True:
                # calculate the interval seconds between minime and current time
                Fmintime= datetime.datetime.strptime(executetime,"%H:%M" )
                presenttime = datetime.datetime.strptime(datetime.datetime.now().strftime('%H:%M:%S'),"%H:%M:%S")
                presentminsecond = (Fmintime - presenttime).seconds

            


            # decide the scheduled time
            if presentsecond < mintime:
                mintime = presentsecond
                print ("launch")
                executetime = timeget["time"]
                executeitem = item
                extime = True
                # calculate the interval seconds between minime and current time
                Fmintime= datetime.datetime.strptime(executetime,"%H:%M" )
                presenttime = datetime.datetime.strptime(datetime.datetime.now().strftime('%H:%M:%S'),"%H:%M:%S")
                presentminsecond = (Fmintime - presenttime).seconds


                executeweight =int(timeget["weight"])
            #check the scheduled time
            print ("check %d")%presentminsecond
            if presentminsecond < 2:
                break

    #execute the scheduled time
    #if str(datetime.datetime.now().strftime('%H:%M:%S')) == str(executetime):
    if presentminsecond < 2:
        


      
        while presentweight < executeweight:

            if ni == True :
                for i in range(4):
                    GPIO.setup(pin[i], GPIO.OUT)
                mot.set_motor('0000')
                mot.reverse(116, 0.01)
    
                for i in range(7):
                    presentweight = hx.get_weight(5)
                    hx.power_down()
                    hx.power_up()
                print presentweight

                ni = False


            for i in range(4):
                GPIO.setup(pin[i], GPIO.OUT)
            mot.set_motor('0000')
            mot.forward(123, 0.01)
    
            for i in range(7):
                presentweight = hx.get_weight(5)
                hx.power_down()
                hx.power_up()
            print presentweight

            ni = True
            

        mot.set_motor('0000')

        for i in range(30):
            time.sleep(1)
            print (30-i)

        for i in range(7):
            presentweight = hx.get_weight(5)
            hx.power_down()
            hx.power_up()
        print presentweight

        firebase.delete('FdSet/',executeitem)

        
        resultput = firebase.put('/resttime',str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')),{ "time" : str(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')), "weight" : presentweight })
        
        statu = "on"
        presentminsecond = 100
        mintime =86399
        
    


         
        

    
 

    


