#include <Servo.h>


Servo RightLeg;
Servo LeftLeg;
Servo Hips;  // create servo object to control a servo


int hips_pos;
int right_pos;
int left_pos;
int positions[3];
int hips_home = 140;
int right_home = 65;
int left_home = 130;
int range_val = 25;
float timer = 0;
float pi = 3.14159;
String dir;

void get_pos(int hips_home, int right_home, int left_home, float pi, int range_val, float timer, int positions[3]){
    hips_pos = hips_home + range_val*sin(timer);
    right_pos =  right_home + range_val*sin(timer + (3*pi/2)); // delay the period of the legs, as they are supposed to be half swing at bottom
    left_pos =  left_home + range_val*sin(timer - (pi/2));
    positions[0] = hips_pos;
    positions[1] = right_pos;
    positions[2] = left_pos;
}


void setup() {
  RightLeg.attach(9);  // attaches the servo on pin 9 to the servo object
  LeftLeg.attach(10);
  Hips.attach(11);   
  dir = "Up";
  Serial.begin(9600);
}

void loop() {
  get_pos(hips_home, right_home, left_home, pi, range_val, timer, positions);
  hips_pos = positions[0];
  right_pos = positions[1];
  left_pos = positions[2];
//  hips_pos = hips_home + range_val*sin(timer);
//  right_pos =  right_home + range_val*sin(timer - (pi/2)); // delay the period of the legs, as they are supposed to be half swing at bottom
//  left_pos =  left_home + range_val*sin(timer - (pi/2));
  timer += pi/100;
    
  Serial.println(left_pos);
  RightLeg.write(right_pos);                  // sets the servo position according to the scaled value
  LeftLeg.write(left_pos);
  Hips.write(hips_pos);
  delay(5);
}
