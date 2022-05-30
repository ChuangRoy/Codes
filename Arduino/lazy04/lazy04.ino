
boolean state = false;

void setup() {
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
  pinMode(7, INPUT);
  digitalWrite(7, HIGH);
}

void loop() {
  if(digitalRead(7) != HIGH){
    state = !state;
    digitalWrite(13, state);
    delay(200);
  }
  else{
  }
}
