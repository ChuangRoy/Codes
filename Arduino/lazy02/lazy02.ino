void setup() {
  // put your setup code here, to run once:
  pinMode(13,OUTPUT);
  pinMode(7,INPUT);
  digitalWrite(7,HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(7)==HIGH){
    digitalWrite(13,HIGH);
  }else{
    digitalWrite(13,LOW);
  }
} 
