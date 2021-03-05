#include <Servo.h>
Servo s1;
Servo s2;
Servo s3;
Servo s4;
Servo s5;
Servo s6;


void setup() {
  Serial.begin(115200);
  s1.attach(3, 1000, 2000);
  s2.attach(5, 1000, 2000);
  s3.attach(6, 1000, 2000);
  s4.attach(9, 1000, 2000);
  s5.attach(10, 1000, 2000);
  s6.attach(11, 1000, 2000);
}
void loop() {
  if (Serial.available() > 0) {

    String ch1 = Serial.readStringUntil('\n'); 
    String ch2 = Serial.readStringUntil('\n');
    String ch3 = Serial.readStringUntil('\n');
    String ch4 = Serial.readStringUntil('\n');
    String ch5 = Serial.readStringUntil('\n');
    String ch6 = Serial.readStringUntil('\n');
    
    int d1 = ch1.toInt();
    int d2 = ch2.toInt();
    int d3 = ch3.toInt();
    int d4 = ch4.toInt();
    int d5 = ch5.toInt();
    int d6 = ch6.toInt();
    
    d1 = map(d1, 995, 1990, 0, 180);
    d2 = map(d2, 995, 1990, 0, 180);
    d3 = map(d3, 995, 1990, 0, 180);
    d4 = map(d4, 995, 1990, 0, 180);
    d5 = map(d5, 995, 1990, 0, 180);
    d6 = map(d6, 995, 1990, 0, 180);
    
    s1.write(d1);
    s2.write(d2);
    s3.write(d3);
    s4.write(d4);
    s5.write(d5);
    s6.write(d6);
        
 }
}
