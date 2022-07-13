
void setup() {
    pinMode(A0, INPUT);
    pinMode(D0, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    Serial.println(analogRead(A0));
    if (analogRead(A0) <= 850) {
        Serial.println("BEEP !!!");
        digitalWrite(D0, HIGH);
    }
    else
        digitalWrite(D0, LOW);
    delay(200);
}
