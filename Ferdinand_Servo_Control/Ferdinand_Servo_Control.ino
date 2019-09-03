#include <Servo.h>

Servo Right;
Servo Left; 
Servo Hips; 
String inByte;
int pos;
int positions[3];
int pinRA = 3;  // Connected to CLK on KY-040
int pinRB = 4;  // Connected to DT on KY-040
int encoderPosCount = 0; 
int pinALast;  
int aVal;

void update_reward(){
   aVal = digitalRead(pinA);
   if (aVal != pinALast){ // Means the knob is rotating
     // if the knob is rotating, we need to determine direction
     // We do that by reading pin B.
     if (digitalRead(pinB) != aVal) {  // Means pin A Changed first - We're Rotating Clockwise
       encoderPosCount ++;
     } else {// Otherwise B changed first and we're moving CCW
       encoderPosCount--;
     }
   } 
   pinALast = aVal;
}
  

void setup() {
  Right.attach(9);
  Left.attach(8);
  Hips.attach(7);
  pinMode (pinA,INPUT);
  pinMode (pinB,INPUT);
  pinALast = digitalRead(pinA);   
  Serial.begin(9600);
}

void loop()
{
  update_reward() ;  
  if (Serial.available())  // if data available in serial port
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
//    Serial.print("Servo in positions: ");  
//    for (int i=0; i<3; i++){
//      Serial.println(positions[i]);
//    }
    String outstring = String(encoderPosCount);
    outstring += " ";
    outstring += String(encoderPosCount);
    Serial.println(outstring);
    }
}
