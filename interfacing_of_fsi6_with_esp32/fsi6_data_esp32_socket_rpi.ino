#include <WiFi.h>
 
const char* ssid = "AE";
const char* password =  "5143851438";
 
const uint16_t port = 8091; // Port
const char * host = "192.168.43.13"; // IP address of RPi

byte PWM_PIN1 = 13;  // PWM pins for reading the PWM signals
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
String allData;
 
void setup()
{ 
  pinMode(PWM_PIN1, INPUT); // Initializing PWM pins as input
  pinMode(PWM_PIN2, INPUT);
  pinMode(PWM_PIN3, INPUT);
  pinMode(PWM_PIN4, INPUT);
  pinMode(PWM_PIN5, INPUT);
  pinMode(PWM_PIN6, INPUT);
 
  Serial.begin(115200);
 
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("...");
  }
 
  Serial.print("WiFi connected with IP: ");
  Serial.println(WiFi.localIP());


 
}
 
void loop()
{

  WiFiClient client;
    if (!client.connect(host, port)) {
 
        Serial.println("Connection to host failed"); // If connection between RPi and esp fails print "Connection to host failed"
        delay(1000);
        return;
    }
    
    pwm_value1 = pulseIn(PWM_PIN1, HIGH); // Reading PWM signals
    pwm_value2 = pulseIn(PWM_PIN2, HIGH);
    pwm_value3 = pulseIn(PWM_PIN3, HIGH);
    pwm_value4 = pulseIn(PWM_PIN4, HIGH);
    pwm_value5 = pulseIn(PWM_PIN5, HIGH);
    pwm_value6 = pulseIn(PWM_PIN6, HIGH);
    
    allData = String(pwm_value1)+" "+String(pwm_value2)+" "+String(pwm_value3)+" "+String(pwm_value4)+" "+String(pwm_value5)+" "+String(pwm_value6); 
    Serial.println(allData);
    client.print(allData); // sending all PWM signals to RPi

}
