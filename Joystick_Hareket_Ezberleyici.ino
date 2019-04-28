
#include <Servo.h>
//KAYIT İÇİN GİRİŞ VE ÇIKIŞLAR
int button=12;
int led = 13;
int buttonst= 0;
int tkr =1;
int counter=0;
int i;
int Play=10;
int playstate = 0;
int led2 = 7;
int Play2= 0;

// SERVOLAR
Servo base;
Servo yatay;
Servo dikey;
Servo gripper;

// MOTOR AÇI KAYITLARI
int mbase;
int myatay;
int mdikey ;
int mgripper;
//KAYIT AÇILARI
int mbase2;
int myatay2;
int mdikey2;
int mgripper2;

// JOYSTICK BAĞLANTILARI
int x1pin = A0;
int y1pin = A1;

int x2pin = A2;
int y2pin = A3;

int x1pos; //sag sol okunacak
int y1pos; // ileri geri okunacak

int x2pos;
int y2pos;




void setup() {
  Serial.begin(9600);
  base.attach(2); 
  yatay.attach(3);
  dikey.attach(4);
  gripper.attach(5);
pinMode(button,INPUT);
pinMode(led,OUTPUT);
pinMode(led2,OUTPUT);
pinMode(Play,INPUT);
mbase = 90;
myatay = 1;
mdikey = 170;
mgripper = 179;
}

void loop() {  
x1pos = analogRead(x1pin);
y1pos = analogRead(y1pin);

x2pos = analogRead(x2pin);
y2pos = analogRead(y2pin);

HareketEt();

buttonst= digitalRead(button);

  if (buttonst==HIGH) {
VerileriGonder();
  }
  else digitalWrite(led,LOW);
  
  
playstate = digitalRead(Play); // oynatma girişi kontrol

if (playstate == HIGH) {
digitalWrite(led2,HIGH);
if (Serial.available() && counter == 0){
  
 mbase2 = Serial.parseInt();
 myatay2=Serial.parseInt();
 mdikey2 = Serial.parseInt();
 mgripper2 = Serial.parseInt();
 counter = 1;
}
if (counter ==1) {
  while(mbase != mbase2) {
  if(mbase>mbase2) mbase-=1;
  else {mbase+=1;}
  base.write(mbase);
  delay(5);
 }
 
 while(myatay2!=myatay) {
   if (myatay>myatay2) myatay-=1;
   else {myatay+=1;} 
   yatay.write(myatay);
 delay(5);
 }
 
 
 while (mdikey2!=mdikey) {
   if(mdikey>mdikey2) mdikey-=1;
   else { mdikey+=1; }
 dikey.write(mdikey);
 delay(5);
 }

 counter =0;
} 
}
else digitalWrite(led2,LOW);
}



void HareketEt() 

{
 if (x1pos > 900 && mbase<180) {
  mbase+=1;
  delay(1);
}
if(x1pos < 100 && mbase >0) {
  mbase-=1;
  delay(1l);
}

if (y1pos > 900 && mdikey>0) {
  mdikey-=1;
  delay(5);
}
if(y1pos < 100 && mdikey <180) {
  mdikey+=1;
  delay(5);
}


if (x2pos > 700 && myatay>0) {
  myatay-=1;
  delay(5);
}
if(x2pos < 100 && myatay < 180) {
  myatay+=1;
  delay(5);
}

if (y2pos > 700 && mgripper>150) {
  myatay-=1;
  delay(5);
}
if(y2pos < 100 && mgripper < 180) {
  myatay+=1;
  delay(5);
}

base.write(mbase); // arka
dikey.write(mdikey);
yatay.write(myatay);
gripper.write(mgripper);

delay(15); 
}
//  ROBOTUN BULUNDUĞU KONUMU RASPBERRY'YE GÖNDER
void VerileriGonder() {
  
 digitalWrite(led,HIGH);
 Serial.println(mbase);
 delay(15);
 Serial.println(myatay);
  delay(15);
 Serial.println(mdikey);
  delay(15);
 Serial.println(mgripper);
  delay(1500);
}
// RASPBERRY ÜZERİNDEKİ KAYITLI POZİSYONLARI ARDUİNOYA AKTAR

