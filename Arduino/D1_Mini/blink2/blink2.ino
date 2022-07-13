#include <Arduino.h>

const int RED=D1;
const int YELLOW=D2;
const int GREEN=D3;
const int RED2=D5;
const int YELLOW2=D6;
const int GREEN2=D7;

void setup() {
    pinMode(RED, OUTPUT);
    pinMode(YELLOW, OUTPUT);
    pinMode(GREEN, OUTPUT);
    pinMode(RED2, OUTPUT);
    pinMode(YELLOW2, OUTPUT);
    pinMode(GREEN2, OUTPUT);
}

void loop() {
    // 1:Red Light
    // 2:Green Light & Blinking
    digitalWrite(RED, HIGH);
    digitalWrite(YELLOW, LOW);
    digitalWrite(GREEN, LOW);

    digitalWrite(RED2, LOW);
    digitalWrite(YELLOW2, LOW);
    digitalWrite(GREEN2, HIGH);
    delay(1000);
    // 2:Green Light Blinking
    for (int i = 0; i < 5; i++) {
        digitalWrite(GREEN2, HIGH);
        delay(100);
        digitalWrite(GREEN2, LOW);
        delay(100);
    }

    // 1:Red Light
    // 2:Yellow Light
    digitalWrite(RED2, LOW);
    digitalWrite(YELLOW2, HIGH);
    digitalWrite(GREEN2, LOW);
    delay(500);

    ///////////////////////////////////////////////

    // 1:Green Light
    // 2:Red Light
    digitalWrite(RED, LOW);
    digitalWrite(YELLOW, LOW);
    digitalWrite(GREEN, HIGH);
    digitalWrite(RED2, HIGH);
    digitalWrite(YELLOW2, LOW);
    digitalWrite(GREEN2, LOW);
    delay(1000);
    // 1:Green Light Blinking
    for (int i = 0; i < 5; i++) {
        digitalWrite(GREEN, HIGH);
        delay(100);
        digitalWrite(GREEN, LOW);
        delay(100);
    }
    
    // 1:Yellow Light
    // 2:Red Light
    digitalWrite(RED, LOW);
    digitalWrite(YELLOW, HIGH);
    digitalWrite(GREEN, LOW);
    delay(500);
}
