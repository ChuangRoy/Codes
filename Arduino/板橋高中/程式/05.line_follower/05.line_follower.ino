void setup() {
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);

  Serial.begin(9600);
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
}

void loop() {
  byte IR_L = digitalRead(A0);
  byte IR_R = digitalRead(A1);
  
  if (IR_L == 數位訊號 && IR_R == 數位訊號) {         /*向前  //數位訊號:0、1
    motor(輸出訊號, 0, 輸出訊號, 0);                  //輸出訊號:0~255(最高設到250就好)，前後兩個輸出訊號要相同喔!
  }                                                     
  else if (IR_L ==數位訊號  && IR_R == 數位訊號) {    /*向左  //數位訊號:0、1
    motor(輸出訊號, 0, 0, 0);                        //輸出訊號:0~255(最高設到250就好)
  }
  else if (IR_L == 0 && IR_R == 數位訊號) {          /*向右  //數位訊號:0、1
    motor(0, 0, 輸出訊號, 0);                        //輸出訊號:0~255(最高設到250就好) 
  }
  else {
    
  }
}

void motor(byte LA, byte LB, byte RA, byte RB) {
  analogWrite(9, LA);
  analogWrite(10, LB);
  analogWrite(6, RA);
  analogWrite(5, RB);
}
