import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) #Numbers GPIOs by physical location
class Motor:
  def __init__(self,mnum):
    self.mnum  = mnum
    
  def setup(self):
    GPIO.setup(self.mnum,GPIO.OUT)
    self.pwm = GPIO.PWM(self.mnum,50)
    self.pwm.start(0)

  def SetAngle(self,angle):  
    self.duty = sekf.angle / 18 + 2  #Converting angle to duty
    GPIO.output(self.mnum, True)   # OUTPUT is high along the duty length
    self.pwm.ChangeDutyCycle(self.duty)
    time.sleep(1) # wait servo to get there
    GPIO.output(self.mnum, False)   # OUTPUT is low till starting function again
    self.pwm.ChangeDutyCycle(0)
