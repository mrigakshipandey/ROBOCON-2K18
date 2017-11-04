/*
 >^/M! (FL)       \^< M2 (FR)
   ----------------
  |                |
  |                |
  |                |
  |                |
  |                |
   ----------------
 >v\M3 (BL)       /v< M4 (BR)
 left - ACW <
 right - CW >
 */

#include <SPI.h>
#include <PS3BT.h>
#include <Servo.h>

Servo servo1;
Servo servo2;

USB Usb;
BTD Btd(&Usb);
PS3BT PS3(&Btd);
int sp=255;

int Led = 13;
int x1, x2, y1, y2, p1, p2, p3, p4, s, vec;
int m11 = 3; //FL
int m12 = 4;
int m21 = 11; //FR
int m22 = 12;
int m31 = 7; //BL
int m32 = 8;
int m41 = 5; //BR
int m42 = 6;
boolean b1 = false,b2 = false;
int s1 = 44;
int s2 = 45;
int posAtt1 = 140,posAtt2 = 130,posRel1 = 0,posRel2 = 0;
void setup() {

   Serial.begin(115200);

   if (Usb.Init() == -1) {
    Serial.print(F("\r\nOSC did not start"));
    while (1); //halt
  }
  servo1.attach(s1);
  servo2.attach(s2);
  servo1.write(posAtt1);
  servo2.write(posAtt2);
  
  Serial.print(F("\r\nPS3 Bluetooth Library Started"));
  pinMode(m11, OUTPUT);
  pinMode(m21, OUTPUT);
  pinMode(m31, OUTPUT);
  pinMode(m41, OUTPUT);
  pinMode(m12, OUTPUT);
  pinMode(m22, OUTPUT);
  pinMode(m32, OUTPUT);
  pinMode(m42, OUTPUT);
  analogWrite(m11, 0);
  analogWrite(m21, 0);
  analogWrite(m31, 0);
  analogWrite(m41, 0);

}

void loop() {

  Usb.Task();
  if (PS3.PS3Connected || PS3.PS3NavigationConnected) {
    //Taking Analog input from joystick
    x1 =  map(PS3.getAnalogHat(LeftHatX), 0, 255, -122, 123);
    y1 =  map(PS3.getAnalogHat(LeftHatY), 0, 255, -122, 123);
    x2 =  map(PS3.getAnalogHat(RightHatX), 0, 255, -122, 123);
    y2 =  map(PS3.getAnalogHat(RightHatY), 0, 255, -122, 123);
    b1 = PS3.getButtonClick(L1);
    b2 = PS3.getButtonClick(R1);
    
    Serial.println(x1);
    Serial.println(y1);
    Serial.println(x2);
    Serial.println(y2);
    Serial.println(b1);
    Serial.println(b2);
    
    s = sqrt(2);
    p1 = x1-y1/s;
    p2 = -x1-y1/s;
    p3 = x1-y1/s;
    p4 = -x1-y1/s;

    if(b1)
    {
      servo1.write(posAtt1);
      servo2.write(posAtt2);
    }
    if(b2)
    {
      servo1.write(posRel1);
      servo2.write(posRel2);
    }
    
    if (x2 == 0) {
    if (p1>0) {
      Serial.println("I");
      p1 = map(p1, 0, 173, 0, sp);
      analogWrite(m11, p1);
      digitalWrite(m12, LOW);
    }
    else {
      Serial.println("II");
      p1 = map(p1, -173, 0, sp, 0);
      analogWrite(m11, p1);
      digitalWrite(m12, HIGH);
    }
    if (p2>0) {
      Serial.println("III");
      p2 = map(p2, 0, 173, 0, sp);
      analogWrite(m21, p2);
      digitalWrite(m22, LOW);
    }
    else {
      Serial.println("IV");
      p2 = map(p2, -173, 0, sp, 0);
      analogWrite(m21, p2);
      digitalWrite(m22, HIGH);
    }
    if (p3>0) {
      Serial.println("V");
      p3 = map(p3, 0, 173, 0, sp);
      analogWrite(m31, p3);
      digitalWrite(m32, LOW);
    }
    else {
      Serial.println("VI");
      p3 = map(p3, -173, 0, sp, 0);
      analogWrite(m31, p3);
      digitalWrite(m32, HIGH);
    }
    if (p4>0) {
      Serial.println("VII");
      p4 = map(p4, 0, 173, 0, sp);
      analogWrite(m41, p4);
      digitalWrite(m42, LOW);
    }
    else {
      Serial.println("VIII");
      p4 = map(p4, -173, 0, sp, 0);
      analogWrite(m41, p4);
      digitalWrite(m42, HIGH);
    }
  }

  else {
  if (x2>0) { //CW turn
    vec = map(x2, 0, 123, 0, sp);
    analogWrite(m11, vec);
    analogWrite(m21, vec);
    analogWrite(m31, vec);
    analogWrite(m41, vec);
    digitalWrite(m12, LOW);
    digitalWrite(m22, HIGH);
    digitalWrite(m32, HIGH);
    digitalWrite(m42, LOW);    
  }
  else { //ACW turn
    vec = map(x2, -122, 0, sp, 0);
    analogWrite(m11, vec);
    analogWrite(m21, vec);
    analogWrite(m31, vec);
    analogWrite(m41, vec);
    digitalWrite(m12, HIGH);
    digitalWrite(m22, LOW);
    digitalWrite(m32, LOW);
    digitalWrite(m42, HIGH);
  }
  }
  
  if (PS3.getButtonClick(UP)) {

    digitalWrite(Led, HIGH);
    Serial.print(F("\r\nUp"));

     if (PS3.PS3Connected) {
      PS3.setLedOff();
      PS3.setLedOn(LED1);
    }

  }

}

  Serial.println("------------");
}

