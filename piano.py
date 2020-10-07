import RPi.GPIO as GPIO 
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

buzzer = 23
do = 21
re = 20
mi = 16
fa = 26
sol = 19
ra = 13
si = 6
do2 = 5
scale = [261,294,329,349,392,440,493,523,1]  
GPIO.setup(do,GPIO.IN)
GPIO.setup(re,GPIO.IN)
GPIO.setup(mi,GPIO.IN)
GPIO.setup(fa,GPIO.IN)
GPIO.setup(sol,GPIO.IN)
GPIO.setup(ra,GPIO.IN)
GPIO.setup(si,GPIO.IN)
GPIO.setup(do2,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)

p = GPIO.PWM(buzzer,600)

p.start(10)
  
try:
   while True:
       if GPIO.input(do) == GPIO.HIGH :
         p.ChangeFrequency(scale[0])
    
       elif GPIO.input(re) == GPIO.HIGH  :
         p.ChangeFrequency(scale[1])
        
       elif GPIO.input(mi) == GPIO.HIGH  :
         p.ChangeFrequency(scale[2])
       
       elif GPIO.input(fa) == GPIO.HIGH  :
         p.ChangeFrequency(scale[3])
        
       elif GPIO.input(sol) ==GPIO.HIGH :
         p.ChangeFrequency(scale[4])
        
       elif GPIO.input(ra) == GPIO.HIGH :
         p.ChangeFrequency(scale[5])
         
       elif GPIO.input(si) == GPIO.HIGH :
         p.ChangeFrequency(scale[6])
        
       elif GPIO.input(do2) == GPIO.HIGH :
         p.ChangeFrequency(scale[7])
         
       else :
         p.ChangeFrequency(scale[8])
         

finally:
  p.stop()  
  GPIO.cleanup()