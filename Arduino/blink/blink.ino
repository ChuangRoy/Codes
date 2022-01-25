int led = 13;


void setup() {         // put your setup code here, to run once:
  pinMode(led, OUTPUT); // sets the digital pin as output
}

void loop() {             // put your main code here, to run repeatedly:
  digitalWrite(led, HIGH); // sets the digital pin on/off
  delay(1000);            // waits a few milliseconds
  digitalWrite(led, LOW);  // sets the digital pin on/off
  delay(1000);            // waits a few milliseconds
}
