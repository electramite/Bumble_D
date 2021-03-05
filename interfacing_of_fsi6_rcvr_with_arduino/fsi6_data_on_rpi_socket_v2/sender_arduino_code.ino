
byte PWM_PIN1 = 3; // ch1 
byte PWM_PIN2 = 5; // ch2
byte PWM_PIN3 = 6; // ch3
byte PWM_PIN4 = 9; // ch4
byte PWM_PIN5 = 10; // ch5
byte PWM_PIN6 = 11; // ch6
 
int pwm_value1; // PWM signal of ch1
int pwm_value2; // PWM signal of ch2
int pwm_value3; // PWM signal of ch3
int pwm_value4; // PWM signal of ch4
int pwm_value5; // PWM signal of ch5
int pwm_value6; // PWM signal of ch6
 
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
  pwm_value1 = pulseIn(PWM_PIN1, HIGH); // reading PWM signal of ch1 of fsi6
  pwm_value2 = pulseIn(PWM_PIN2, HIGH); // reading PWM signal of ch2 of fsi6
  pwm_value3 = pulseIn(PWM_PIN3, HIGH); // reading PWM signal of ch3 of fsi6
  pwm_value4 = pulseIn(PWM_PIN4, HIGH); // reading PWM signal of ch4 of fsi6
  pwm_value5 = pulseIn(PWM_PIN5, HIGH); // reading PWM signal of ch5 of fsi6
  pwm_value6 = pulseIn(PWM_PIN6, HIGH); // reading PWM signal of ch6 of fsi6
  String allData = String(pwm_value1)+" "+String(pwm_value2)+" "+String(pwm_value3)+" "+String(pwm_value4)+" "+String(pwm_value5)+" "+String(pwm_value6); // storing all PWM values in a string
  Serial.println(allData); // printing/sending all values to serial
}
