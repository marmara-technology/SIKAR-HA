import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) 
class Motor:
  def __init__(self,mnum):
    self.mnum  = mnum
    self.cout = 0
  def setup(self):
    GPIO.setup(self.mnum,GPIO.OUT)
    self.pwm = GPIO.PWM(self.mnum,50)
    self.pwm.start(0)
    

  def SetAngle(self,angle):  
    self.duty = angle / 18 + 2  
    GPIO.output(self.mnum, True)   
    self.pwm.ChangeDutyCycle(self.duty)
    GPIO.output(self.mnum, False) 
    self.pwm.ChangeDutyCycle(0)
    
  def run(self,ang):
    for self.cout in range (0,ang):
      self.SetAngle(ang)
      time.sleep(0.005)
      self.cout +=1

    if self.cout == ang:
      self.cout =0
     
