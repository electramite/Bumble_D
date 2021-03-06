
byte PWM_PIN1 = 13; 
byte PWM_PIN2 = 14; 
byte PWM_PIN3 = 15; 
byte PWM_PIN4 = 16; 
byte PWM_PIN5 = 17; 
byte PWM_PIN6 = 18;  
 
int pwm_value1;
int pwm_value2;
int pwm_value3;
int pwm_value4;
int pwm_value5;
int pwm_value6;
 
void setup() {
  pinMode(PWM_PIN1, INPUT);
  pinMode(PWM_PIN2, INPUT);
  pinMode(PWM_PIN3, INPUT);
  pinMode(PWM_PIN4, INPUT);
  pinMode(PWM_PIN5, INPUT);
  pinMode(PWM_PIN6, INPUT);
  Serial.begin(115200);
}
 
void loop() {
  pwm_value1 = pulseIn(PWM_PIN1, HIGH);
  pwm_value2 = pulseIn(PWM_PIN2, HIGH);
  pwm_value3 = pulseIn(PWM_PIN3, HIGH);
  pwm_value4 = pulseIn(PWM_PIN4, HIGH);
  pwm_value5 = pulseIn(PWM_PIN5, HIGH);
  pwm_value6 = pulseIn(PWM_PIN6, HIGH);
  Serial.print(pwm_value1);
  Serial.print(",");
  Serial.print(pwm_value2);
  Serial.print(",");
  Serial.print(pwm_value3);
  Serial.print(",");
  Serial.print(pwm_value4);
  Serial.print(",");
  Serial.print(pwm_value5);
  Serial.print(",");
  Serial.println(pwm_value6);
}
