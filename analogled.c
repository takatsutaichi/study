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
for (i=0;i<=256;i++){
  analogWrite(LED_PIN,i);
  delay(500);
}
for (h=256;h>0;h--){
  analogWrite(YELLOW_PIN,h);
  delay(500);
}
}