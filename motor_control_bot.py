#Indoor navigation system use the Arruco marker to detect the rotation and the position of the robot control with IoT processing data 
import time 
import math 
import requests
from itertools import count
from pyfirmata import ArduinoMega, util
board = ArduinoMega('/dev/ttyUSB0')
mr1 = board.get_pin('d:2:p')
mr2 = board .get_pin('d:3:p')
ml1 = board.get_pin('d:4:p')
ml2 = board.get_pin('d:6:p')
def stop():
    mr1.write(0)
    mr2.write(0)
    ml1.write(0)
    ml2.write(0)
def motion_logic(mr_val1,mr_val2,ml_val1,ml_val2):
    mr1.write(mr_val1)
    mr2.write(mr_val2)
    ml1.write(ml_val1)
    ml2.write(ml_val2)
#Get the email data 
email = "kornbot380@hotmail.com" 
project_name = "Smart_Robots"
#Stop the all the motion logic function 
stop() 
store_detect  = {}
for i in count(0):
     #Get the current position 
     reqpos = requests.get("http://192.168.50.247:8912/total_nav_pos").json()[email][project_name]
     print("Current position data: ",reqpos)
     #Get the local pos 
     x= int(float(reqpos.get('X')))
     y = int(float(reqpos.get('Y')))
     angle = int(float(reqpos.get('Angle')))
     print("Locl_pos: ",x,y,angle,type(x),type(y),type(angle))
     #Get request local command 
     req_server = requests.get("http://192.168.50.193:5776/localcommand").json()[email][project_name] 
     print("Local server command: ",req_server) #Get the local server command data 
     stop()
     time.sleep(0.07)
     command = list(req_server)[0]
     speed = req_server[command]
     pos_x = int(float(req_server['X'])) 
     pos_y = int(float(req_server['Y']))
     Angle = int(float(req_server['Angle']))
     store_detect['X'] = pos_x
     store_detect['Y'] = pos_y
     store_detect['Angle'] = Angle 
     try:
        #angle_current = math.degrees(math.atan(y/x)) 
        #angle_target = math.degrees(math.atan(pos_y/pos_x)) #Get the angle of the desire angle 
        def pos_y_adjust():
           if  y > pos_y:
              motion_logic(speed,0,speed,0)
           if  y < pos_y:
              motion_logic(0,speed,0,speed)
           if  y == pos_y:
               stop()

        def pos_x_adjust():
          if  x > pos_x:
            motion_logic(speed,0,speed,0)
          if  x < pos_x:
            motion_logic(0,speed,0,speed)
          if  x == pos_x:
              pos_y_adjust()
              stop()
  
        if command != "stop": 
          if angle < Angle:              
            #store_detect['min_angle'] = angle 
            #if "found_angle" not in list(store_detect):
               motion_logic(0,speed,speed,0)
            
          if angle >Angle:
            #store_detect['max_angle'] = angle
            #if "found_angle" not in list(store_detect):
              motion_logic(speed,0,0,speed)  
       
          if angle == Angle:
              #stop()     
              print("Target position checked") 
              store_detect['found_angle'] = angle
              pos_x_adjust()         
              reqdat = requests.post("http://192.168.50.193:5776/post_position_command",json={'email':'kornbot380@hotmail.com','project_name':'Smart_Robots','command':{'stop':0.45,'X':150,'Y':140,'Angle':130}})
          if 'found_angle' in list(store_detect):
                 if Angle != store_detect['Angle']:
                       del store_detect['found_angle']

     except:
         print("Error division")      
   
   
