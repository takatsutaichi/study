#define LED_PIN 13
#define YELLOW_PIN 12
int i,h;
void setup() {
  // put your setup code here, to run once:
  pinMode(LED_PIN,OUTPUT);
  pinMode(YELLOW_PIN,OUTPUT);
}
void loop() {
  // put your main code here, to run repeatedly:
digitalWrite(LED_PIN, HIGH);
delay(10000);
for (i=0;i<=2;i++){
  digitalWrite(LED_PIN, LOW);
  delay(500);
  digitalWrite(LED_PIN, HIGH);
  delay(500);
}  
digitalWrite(LED_PIN, LOW);
digitalWrite(YELLOW_PIN, HIGH);
delay(10000);
for (h=0;h<=2;h++){
  digitalWrite(YELLOW_PIN, LOW);
  delay(500);
  digitalWrite(YELLOW_PIN, HIGH);
  delay(500);
}
digitalWrite(YELLOW_PIN, LOW);
}