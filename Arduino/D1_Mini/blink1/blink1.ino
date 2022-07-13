// FQBN:esp8266:esp8266:d1_mini

void setup() {
    pinMode(D4, OUTPUT);
}

void loop() {
    digitalWrite(D4, HIGH);
    delay(10);
    digitalWrite(D4, LOW);
    delay(10);
}
