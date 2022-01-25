/*
  序列埠練習02
*/

// constants won't change. They're used here to set pin numbers:

const int buttonPin = 7;     // the number of the pushbutton pin
const int ledPin =  13;      // the number of the LED pin

// variables will change:
int buttonState = 0; // variable for reading the pushbutton status 
int beforeState = 0; // variable for get last time on or off
int presstime = 1;
void setup() {
  //serial:傳輸，定義速率 = 9600
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
  Serial.println("hi~~按我~~");
}

void loop() {
  buttonState = digitalRead(buttonPin);
 if(buttonState==1 and beforeState==0) {
    Serial.println(presstime);//讓序列埠印出狀況，print"ln"換行
    if(presstime > 100){
    Serial.println("我受不了了，你贏了");
    presstime = 0;   
      }else{
    presstime = presstime+1;
      }
    delay(1);
 }
 if(buttonState!=beforeState){
  delay(50);
  
  }
 beforeState = buttonState;
 delay(1);
}
