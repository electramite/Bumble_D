
int pot_pin = A0;

int pot_value;

void setup() {
  Serial.begin(115200);
}
void loop() {

  pot_value = analogRead(pot_pin);
  Serial.println(pot_value);
}
