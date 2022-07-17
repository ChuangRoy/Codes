void setup() {
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);

  Serial.begin(9600);
  /*設定腳位的工作模式:  pinMode(腳位, 狀態);
    腳位:A0、A1，狀態:INPUT、OUTPUT */
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);

}

void loop() {
  byte IR_L = digitalRead(A0);
  byte IR_R = digitalRead(A1);
  Serial.print("IR_L: ");
  Serial.print(IR_L);
  Serial.print(", IR_R: ");
  Serial.println(IR_R);
  delay(300);
}
