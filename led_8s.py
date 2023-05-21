import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pins = [18,24,21,14,4,11,16,12]
for p in pins:
GPIO.setup(p,GPIO.OUT)
cnt = 1000

pins = [18,24,21,14,4,11,16,12]

for i in range(0,cnt,1):
          for p in pins:
 	if p == 18:
	     GPIO.output(p,True)
	else
	     GPIO.output(p,False)		
          time.sleep(0.2)
     
          for p in pins:
 	if p == 24:
	     GPIO.output(p,True)
	else
	     GPIO.output(p,False)		
          
          time.sleep(0.2)
    
          for p in pins:
 	if p == 21:
	     GPIO.output(p,True)
	else
	     GPIO.output(p,False)		
          time.sleep(0.2)
          
          for p in pins:
 	if p == 14:
	     GPIO.output(p,True)
	else
	     GPIO.output(p,False)		
          time.sleep(0.2)
          
         for p in pins:
 	if p == 4:
	     GPIO.output(p,True)
	else
	     GPIO.output(p,False)		
          time.sleep(0.2)
          
          for p in pins:
 	if p == 11:
	     GPIO.output(p,True)
	else
	     GPIO.output(p,False)		
          time.sleep(0.2)
          
          for p in pins:
 	if p == 16:
	     GPIO.output(p,True)
	else
	     GPIO.output(p,False)		
          time.sleep(0.2)
          
          for p in pins:
 	if p == 12:
	     GPIO.output(p,True)
	else
	     GPIO.output(p,False)		
          time.sleep(0.2)
          
          print(i)
          
GPIO.cleanup()