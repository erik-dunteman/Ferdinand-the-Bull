#include <Servo.h>
Servo Right;
Servo Left; 
Servo Hips; 
String inByte;
int pos;
int positions[3];

void setup() {
  Right.attach(9);
  Left.attach(8);
  Hips.attach(7);
  Serial.begin(9600);
}

void loop()
{    
  if(Serial.available())  // if data available in serial port
  {
    int i = 0;
    while (i<3) {
      inByte = Serial.readStringUntil('\n'); // read data until newline
      positions[i]=inByte.toInt();
      i+=1;
    }
    pos = inByte.toInt();   // change datatype from string to integer        
    Right.write(positions[0]);     // move servo
    Left.write(positions[1]);     // move servo
    Hips.write(positions[2]);     // move servo
    Serial.print("Servo in positions: ");  
    for (int i=0; i<3; i++){
      Serial.println(positions[i]);
    }

    }
}
