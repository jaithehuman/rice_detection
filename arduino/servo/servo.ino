#include <Servo.h>

Servo myservo;

const int ledPin = 8; // the pin that the LED is attached to
const int servoPin = 9;
int incomingByte;      // a variable to read incoming serial data into

void setup()
{
  pinMode(3, INPUT);//button
  pinMode(servoPin, OUTPUT); //servo
  pinMode(ledPin, INPUT);
  digitalWrite(ledPin,HIGH);
  Serial.begin(9600);
}

void loop(){              
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    // if it's a capital H (ASCII 72), turn on the LED:
    if (incomingByte == 'H') {
      servo_control();
    }
    // if it's an L (ASCII 76) turn off the LED:
//    if (incomingByte == 'L') {
//      digitalWrite(ledPin, LOW);
//    }
  }
}

void servo_control(){ //stops at 1,3,5,7,...
  myservo.attach(servoPin);
  myservo.write(0);
  for(int i = 0; i<9;i++){
    for(int j=0;j<5;j++){
      digitalWrite(ledPin, LOW);
      myservo.write(50);
      delay(100);
      myservo.write(0);
      delay(100);
    }
    digitalWrite(ledPin, HIGH);
    delay(1000);
  }
  myservo.detach();
}
