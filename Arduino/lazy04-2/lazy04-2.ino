boolean state = false;
boolean buttonUp = true;

void setup() {
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
  pinMode(7, INPUT);
  digitalWrite(7, HIGH);
}

void loop() {
  if(digitalRead(7) != HIGH && buttonUp == true) {
    state = !state;
    digitalWrite(13, state);
    buttonUp = false;
  }
  else if(digitalRead(7) == HIGH && buttonUp != true) {
    buttonUp = true;
  }
  delay(10); // Delay 時間可視情況調整
}
