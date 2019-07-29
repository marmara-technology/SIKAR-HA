import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) #Numbers GPIOs by physical location

#PINOUT SETTINGS
## MOTOR 1
GPIO.setup(3,GPIO.OUT) #Pin 3 is set output for servo
pwm=GPIO.PWM(3,50) # creating 50 Hz PWM from Pin 3 (Servo works with 20ms period or 50Hz freq)
pwm.start(0) # Lets start PWM
##MOTOR 2
GPIO.setup(5,GPIO.OUT)
pwm2=GPIO.PWM(5,50)
pwm2.start(0)
##GRIPPER
GPIO.setup(7,GPIO.OUT)
pwm3=GPIO.PWM(7,50)
pwm3.start(0)

GPIO.setup(9,GPIO.OUT)
pwm3=GPIO.PWM(9,50)
pwm3.start(0)


class Motor:
  def __init__(self,mnum,angle):
    self.mnum  = mnum
    self.angle = angle
  def setup(self,self.mnum):
    GPIO.setup(mnum,GPIO.OUT)
    self.pwm = GPIO.PWM(mnum,50)
    self.pwm.start(0)

  def SetAngle(self,self.angle):  # Angle paramater will be got from user
    self.duty = angle / 18 + 2  #Converting angle to duty
    GPIO.output(mnum, True)   # OUTPUT is high along the duty length
    self.pwm.ChangeDutyCycle(self.duty)
    time.sleep(1) # wait servo to get there
    GPIO.output(mnum, False)   # OUTPUT is low till starting function again
    self.pwm.ChangeDutyCycle(0)



  

