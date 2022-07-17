#include <NewPing.h>

#define TRIGGER_PIN  11
#define ECHO_PIN     12
#define MAX_DISTANCE 200

NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE);

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (sonar.ping_cm() > 20) {
    motor(150, 0, 150, 0);
  }
  else {
    motor(0, 150, 150, 0);
  }
}

void motor(byte LA, byte LB, byte RA, byte RB) {
  analogWrite(9, LA);
  analogWrite(10, LB);
  analogWrite(6, RA);
  analogWrite(5, RB);
}
