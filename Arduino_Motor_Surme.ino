
#include <Servo.h>
int button=12;
int led = 8;
int buttonst= 0;



Servo base;
Servo yatay;
Servo dikey;
Servo gripper;


int bpot = 0;
int ypot = 1;
int dpot = 2;



int mbase;
int myatay;
int mdikey;
int mgripper;


void setup() {
  Serial.begin(9600);
  base.attach(2);  // attaches the servo on pin 9 to the servo object
  yatay.attach(3);
  dikey.attach(4);
  gripper.attach(5);
pinMode(button,INPUT);
pinMode(led,OUTPUT);
}

void loop() {
  
mbase = analogRead(bpot);
mbase = map(mbase,0,1023,0,179);

myatay = analogRead(ypot);
myatay = map(myatay,0,1023,0,179);

mdikey = analogRead(dpot);
mdikey = map(mdikey,0,1023,0,179);

// if (gopen == HIGH && mgripper <180) mgripper+=4;
// if (gclose == HIGH && mgripper >162) mgripper-=4;

base.write(mbase); // arka
yatay.write(myatay); // -seri haberleşmeden gelen bilgi test-
dikey.write(mdikey); // en üst
gripper.write(mgripper); // Gripper kapalı
delay(15);


buttonst= digitalRead(button);
  if (buttonst==HIGH) {
  
 digitalWrite(led,HIGH);
 Serial.println(mbase);
 delay(100);
 Serial.println(myatay);
  delay(100);
 Serial.println(mdikey);
  delay(100);
 Serial.println(mgripper);
  delay(100);
  }
  else digitalWrite(led,LOW);
  
 
}

