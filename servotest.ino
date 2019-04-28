/*
Sıkar-Ha motor Test 
*/

#include <Servo.h>

Servo base;
Servo yatay;
Servo dikey;
Servo gripper; 

angle =1;
void setup() {
  Serial.begin(9600);
  base.attach(2);  // attaches the servo on pin 9 to the servo object
  yatay.attach(3);
  dikey.attach(4);
  gripper.attach(5);
}

void loop() {
  if(Serial.available()){
    angle = angle*(Serial.read()-'0'); // raspi-arduino haberleşmesinden alınacak bilgi -yapım aşamasında-
    }
  base.write(180); // arka
  yatay.write(angle); // -seri haberleşmeden gelen bilgi test-
  dikey.write(180); // en üst
  gripper.write(180); // Gripper kapalı

  delay(15);                           // waits for the servo to get there
}
