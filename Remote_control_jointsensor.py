import requests 
import time 
import numpy as np 
from itertools import count
import random

for r in count(0):
    #reqdata = requests.post("https://roboreactor.com/package_iot_control",json={'kornbot380@hotmail.com':{}})
    #current_feedback = reqdata.json()['Smart_Robots']['revolute'] 
    #res_feedback = requests.post('https://roboreactor.com/feedback_sensor',json={'kornbot380@hotmail.com':{'wrist':{'Analog-read':45.0},'base':{'Analog-read':140.4}}})
    #print(res_feedback.json())
    c= 0.1
    rc = 0 
    for i in range(0,240):
          #for r in range(0,8):
          '''
          try:
            reqdata = requests.post("https://roboreactor.com/package_iot_control",json={'kornbot380@hotmail.com':{}})
            current_feedback = reqdata.json()['Smart_Robots']['revolute'] 
            base  = current_feedback['base'] 
            print("Destination angle,current feedback",rc,base)
            d = rc -base
            i = rc+d    
            res_feedback = requests.post('https://roboreactor.com/feedback_sensor',json={'kornbot380@hotmail.com':{'wrist':{'Analog-read':i},'shoulder':{'Analog-read':i},'base':{'Analog-read':i}}})
            #for r in range(0,8):
            #      print("Forward: ",i)

          except:
                  print("No old data read")
          '''
          rc = i #+random.random()
       
          res_feedback = requests.post('https://roboreactor.com/feedback_sensor',json={'kornbot380@hotmail.com':{'wrist':{'Analog-read':rc},'shoulder':{'Analog-read':rc},'base':{'Analog-read':rc}}})
              #for r in range(0,8):
          print("Forward: ",rc)
          try:
             reqdata = requests.post("https://roboreactor.com/package_iot_control",json={'kornbot380@hotmail.com':{}})
             current_feedback = reqdata.json()['Smart_Robots']['revolute']
             print(current_feedback)
          except:
               print("No data input yet") 
    for i in range(240,0,-1):
          #for r in range(0,8): 
          rc = i #+random.random()
          res_feedback = requests.post('https://roboreactor.com/feedback_sensor',json={'kornbot380@hotmail.com':{'wrist':{'Analog-read':rc},'shoulder':{'Analog-read':rc},'base':{'Analog-read':rc}}})
          #for r in range(0,8):  
          print("Back ward: ",rc)
          try:
             reqdata = requests.post("https://roboreactor.com/package_iot_control",json={'kornbot380@hotmail.com':{}})
             current_feedback = reqdata.json()['Smart_Robots']['revolute']
             print(current_feedback)
          except:
             print("No data input yet") 
    #time.sleep(0.04)
#for i in np.arange(0.0, 270.0, 0.01):
#    print(i)   
#    res_feedback = requests.post('https://roboreactor.com/feedback_sensor',json={'kornbot380@hotmail.com':{'wrist':{'Analog-read':i},'shoulder':{'Analog-read':i},'base':{'Analog-read':i}}}) 	
#res_feedback = requests.post('https://roboreactor.com/feedback_sensor',json={'kornbot380@hotmail.com':{'wrist':{'Angle-read':
#270}}})
