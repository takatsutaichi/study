#define LED_PIN 13
unsigned long echo = 0;
int signalPin = 9,d;

void setup() {
  Serial.begin(9600);
  pinMode(LED_PIN,OUTPUT);
}
void loop() {
  pinMode(signalPin,OUTPUT);
  digitalWrite(signalPin,LOW);
  digitalWrite(signalPin,HIGH); 
  delayMicroseconds(5);
  digitalWrite(signalPin,LOW);
  pinMode(signalPin,INPUT); 
  echo = pulseIn(signalPin,HIGH)/2; 
  int distance = echo * 344 / 1000 ; 
  Serial.println(distance);
  d=255-distance;
  if (d<0){
  digitalWrite(LED_PIN,LOW);
  }else{
  analogWrite(LED_PIN,d);
  }
  delay(1000);
}