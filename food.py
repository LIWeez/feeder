
from firebase import firebase
import datetime
import json


firebase = firebase.FirebaseApplication('https://my-catfeeder.firebaseio.com', None)

weight = 20

#resultput = firebase.put('/settime',str(datetime.datetime.now().strftime('%H:%M:%S')),{ "time" : str(datetime.datetime.now().strftime('%H:%M:%S')), "weight" : "130" })
resultput = firebase.put('/resttime',str(datetime.datetime.now().strftime('%H:%M:%S')),{ "time" : str(datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')), "weight" : weight })    



#json_array = firebase.get('settime', None)
#print ("main")
#firebase.delete('m')

print (resultput)
#print (result)
       
#json_array = result
#json_array.sort(key = lambda x:x["time"])
#json_settime = json_array

mintime =86399
"""
while True:
    for item in json_array :
     print (item)
     timeget = firebase.get('settime/', item)
     print (timeget["time"])
     Fsettime= datetime.datetime.strptime(timeget["time"],"%H:%M:%S" )
     presenttime = datetime.datetime.strptime(datetime.datetime.now().strftime('%H:%M:%S'),"%H:%M:%S")

     presentsecond = (Fsettime - presenttime).seconds

     print (presentsecond)

     

     if presentsecond < mintime:
        mintime = presentsecond
        executetime = timeget["time"]

    print (mintime)
    print (executetime)

"""

    








