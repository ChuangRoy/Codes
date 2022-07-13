// FQBN:esp8266:esp8266:nodemcuv2

// motor settings
#define RIGHT_MOTOR_PIN1 4 // pin 1 of right motor(D2)
#define RIGHT_MOTOR_PIN2 5 // pin 2 of right motor(D1)
#define LEFT_MOTOR_PIN1 12 // pin 1 of left motor(D6)
#define LEFT_MOTOR_PIN2 14 // pin 2 of left motor(D5)
#define RIGHT_MOTOR_SPEED 1023 // speed for right motor (0-1023)
#define LEFT_MOTOR_SPEED 1023 // speed for left motor (0-1023)
#define LED_PIN 2 // built-in LED (D4)

void setup() {
     Serial.begin(115200);
     Serial.println("ESP8266 Wifi Car");
     pinMode(RIGHT_MOTOR_PIN1, OUTPUT);
     pinMode(RIGHT_MOTOR_PIN2, OUTPUT);
     pinMode(LEFT_MOTOR_PIN1, OUTPUT);
     pinMode(LEFT_MOTOR_PIN2, OUTPUT);
     pinMode(LED_PIN, OUTPUT);
     digitalWrite(LED_PIN, LOW);
}

void loop() {
        //stop
        digitalWrite(RIGHT_MOTOR_PIN1, LOW);
        digitalWrite(RIGHT_MOTOR_PIN2, LOW);
        digitalWrite(LEFT_MOTOR_PIN1, LOW);
        digitalWrite(LEFT_MOTOR_PIN2, LOW);
        delay(1000);
        //forward
        analogWrite(RIGHT_MOTOR_PIN1,
                      RIGHT_MOTOR_SPEED);
        digitalWrite(RIGHT_MOTOR_PIN2, LOW);
        analogWrite(LEFT_MOTOR_PIN1,
                      LEFT_MOTOR_SPEED);
        digitalWrite(LEFT_MOTOR_PIN2, LOW);
        delay(1000);
        // backward
        digitalWrite(RIGHT_MOTOR_PIN1, LOW);
        analogWrite(RIGHT_MOTOR_PIN2,
                      RIGHT_MOTOR_SPEED);
        digitalWrite(LEFT_MOTOR_PIN1, LOW);
        analogWrite(LEFT_MOTOR_PIN2,
                      LEFT_MOTOR_SPEED);
        delay(1000);
        // turn left
        analogWrite(RIGHT_MOTOR_PIN1,
                      RIGHT_MOTOR_SPEED);
        digitalWrite(RIGHT_MOTOR_PIN2, LOW);
        digitalWrite(LEFT_MOTOR_PIN1, LOW);
        analogWrite(LEFT_MOTOR_PIN2,
                      LEFT_MOTOR_SPEED);
        delay(1000);
        // turn right
        digitalWrite(RIGHT_MOTOR_PIN1, LOW);
        analogWrite(RIGHT_MOTOR_PIN2,
                      RIGHT_MOTOR_SPEED);
        analogWrite(LEFT_MOTOR_PIN1,
                      LEFT_MOTOR_SPEED);
        digitalWrite(LEFT_MOTOR_PIN2, LOW);
        delay(1000);
}
