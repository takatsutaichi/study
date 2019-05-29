#define LED_PIN 13
#define YELLOW_PIN 12
int i;

void setup() {
  // put your setup code here, to run once:
  pinMode(LED_PIN,OUTPUT);
  pinMode(YELLOW_PIN,OUTPUT);
}
void loop() {
  // put your main code here, to run repeatedly:
for (i=0;i<256;i++){
  analogWrite(LED_PIN,i);
  analogWrite(YELLOW_PIN,255-i);
  delay(10);
}

for (i=255;i>0;i--){
  analogWrite(LED_PIN,i);
  analogWrite(YELLOW_PIN,255-i);
  delay(10);
}
}