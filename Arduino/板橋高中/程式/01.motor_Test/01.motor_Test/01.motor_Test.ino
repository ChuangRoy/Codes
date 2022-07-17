void setup() {
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);

  analogWrite(5, 200);
  analogWrite(6, 0);
  analogWrite(9, 200);
  analogWrite(10, 0);

  delay(3000);
  analogWrite(5, 0);
  analogWrite(6, 0);
  analogWrite(9, 0);
  analogWrite(10, 0);
  
}

void loop() {
  

}
