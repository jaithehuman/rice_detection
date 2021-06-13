#include <Servo.h>

Servo myservo;
void setup()
{
  myservo.attach(9);
  myservo.write(0);
  pinMode(9, OUTPUT); //servo

  
  Serial.begin(9600);
}


void loop(){
//  for(int i = 0;i < 180;i++){
//   myservo.write(i);
//   delay(15);
//  }
//  for(int i = 180;i > 0;i--){
//   myservo.write(i);
//   delay(15);
//  }
}
