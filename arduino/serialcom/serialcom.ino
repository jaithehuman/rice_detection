int x;

void setup() {
  pinMode(8,OUTPUT);
  digitalWrite(8,LOW);
  
  Serial.begin(115200);
  Serial.setTimeout(1);
}

void loop() {
//  digitalWrite(8,HIGH);
//  delay(1000);
//  digitalWrite(8,LOW);
//  delay(1000);
//  while (!Serial.available());
//  x = Serial.readString().toInt();
////  digitalWrite(8,HIGH);
//  if(x)Serial.print(x+1);

    if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    // if it's a capital H (ASCII 72), turn on the LED:
    if (incomingByte == 'H') {
      digitalWrite(ledPin, HIGH);
    }
    // if it's an L (ASCII 76) turn off the LED:
    if (incomingByte == 'L') {
      digitalWrite(ledPin, LOW);
    }
  }
}
