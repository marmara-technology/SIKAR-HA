import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD) #Numbers GPIOs by physical location
GPIO.setup(3,GPIO.OUT) # Pin 3 is set output for servo
GPIO.setup(10,GPIO.IN, pull_up_down=GPIO.PUD_UP) # Pin 10 is set HIGH input for "loop switch"
pwm=GPIO.PWM(3,50) # creating 50 Hz PWM from Pin 3 (Servo works with 20ms period or 50Hz freq)
pwm.start(0) # Lets start PWM
def SetAngle(angle):  # Angle paramater will be got from user
    duty = angle / 18 + 2  #Converting angle to duty
    GPIO.output(3, True)   # OUTPUT is high along the duty length
    pwm.ChangeDutyCycle(duty)
    sleep(1) # wait servo to get there
    GPIO.output(3, False)   # OUTPUT is low till starting function again
    pwm.ChangeDutyCycle(0)


while True:    #endless loop
 rec = GPIO.input(10)  # loop switch is set at pin 10
 x = int(input("Enter servo angle  ")) # getting angle from user
 SetAngle(x) #put variable to function
 while GPIO.input(10) == GPIO.HIGH:   # after servo getting to location checks for switch position
  SetAngle(0) #if it is on, servo going to starting position 
  print(" \nWait 3 secs until the servo goes to starting position.")
  sleep(3) 
  SetAngle(x) # after waiting 3 secs calling function again
  print("\nServo goes to recorded position. Wait 3 secs")
  sleep(3)
  if GPIO.input(10) == GPIO.LOW: # checking again switch position
   break # breaking loop of servo
        
    
 a=int(input("Enter number "1" to Continiue\n"))
 if a==1:
         continue # go to beginning of the endless loop
        
 else:
         break  # break endless loop and terminate the program

        
