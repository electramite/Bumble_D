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
    int c = 0;

    int d[6]={0};
    int x;
    for(int i=0;i<ch1.length();i++)
    {
      if(ch1[i]==' ')
      {
        c++;
      }else
      {
        x=ch1[i]-48;
        d[c]=d[c]*10 +x;
      }
    }
    
    int d1 = map(d[0], 995, 2000, 0, 180);
    int d2 = map(d[1], 995, 2000, 0, 180);
    int d3 = map(d[2], 995, 2000, 0, 180);
    int d4 = map(d[3], 995, 2000, 0, 180);
    int d5 = map(d[4], 995, 2000, 0, 180);
    int d6 = map(d[5], 995, 2000, 0, 180);
    
    s1.write(d1);
    s2.write(d2);
    s3.write(d3);
    s4.write(d4);
    s5.write(d5);
    s6.write(d6);
        
  }
}
