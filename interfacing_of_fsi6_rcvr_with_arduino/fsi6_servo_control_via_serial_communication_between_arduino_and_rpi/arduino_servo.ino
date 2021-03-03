#include <Servo.h>
Servo bldc;


void setup() {
  Serial.begin(115200);
  bldc.attach(9);
}
void loop() {
  if (Serial.available() > 0) {

    String data = Serial.readStringUntil('\n');
    int x = data.toInt();
    x = map(x, 975, 1990, 0, 180);
    bldc.write(x);    
  }
}
