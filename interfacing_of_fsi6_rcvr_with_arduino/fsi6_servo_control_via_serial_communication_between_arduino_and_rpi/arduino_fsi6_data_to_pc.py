byte PWM_PIN1 = 3;
byte PWM_PIN2 = 5;
byte PWM_PIN3 = 6;
byte PWM_PIN4 = 9;
byte PWM_PIN5 = 10;
byte PWM_PIN6 = 11;
 
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

  String allData = String(pwm_value1)+" "+String(pwm_value2)+" "+String(pwm_value3)+" "+String(pwm_value4)+" "+String(pwm_value5)+" "+String(pwm_value6);
#   Serial.println(pwm_value1);
#   Serial.println(pwm_value2);
#   Serial.println(pwm_value3);
#   Serial.println(pwm_value4);
#   Serial.println(pwm_value5);
#   Serial.println(pwm_value6);
}
