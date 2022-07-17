void setup() {
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
}

void loop() {
   /*向前    Forward(輸出訊號)
   輸出訊號:0~255(最高設到250就好) */
  Forward(250);
   /*等待時間，前一行指令持續(延遲)多久 
   delay(毫秒);   延遲設為1秒*/
  delay(1000);
  //有1行
  Stop();
   /*等待時間，前一行指令持續(延遲)多久 
   delay(毫秒);   延遲設為1秒*/
  delay(1000);
  /*向後    Backward(輸出訊號)
   輸出訊號:0~255(最高設到250就好) */
  Backward(250);
   /*等待時間，前一行指令持續(延遲)多久 
   delay(毫秒);   延遲設為1秒*/
  delay(1000);

  Stop();
   /*等待時間，前一行指令持續(延遲)多久 
   delay(毫秒);   延遲設為1秒*/
  delay(1000);

  /*向左    Left(輸出訊號)
   輸出訊號:0~255(最高設到250就好) */
  Left(250);
   /*等待時間，前一行指令持續(延遲)多久 
   delay(毫秒);   延遲設為1秒*/
  delay(1000);
  Stop();
   /*等待時間，前一行指令持續(延遲)多久 
   delay(毫秒);   延遲設為1秒*/
  delay(1000);

  /*向右    Right(輸出訊號)
   輸出訊號:0~255(最高設到250就好) */
  Right(250);
   /*等待時間，前一行指令持續(延遲)多久 
   delay(毫秒);   延遲設為1秒*/
  delay(1000);

  Stop();
  /*等待時間，前一行指令持續(延遲)多久 
   delay(毫秒);   延遲設為1秒*/
  delay(1000);

}

void Forward(byte sp) {
  analogWrite(6, sp);
  analogWrite(5, 0);
  analogWrite(9, sp);
  analogWrite(10, 0);
}

void Backward(byte sp) {
  analogWrite(6, 0);
  analogWrite(5, sp);
  analogWrite(9, 0);
  analogWrite(10, sp);
}

void Left(byte sp) {
  analogWrite(6, sp);
  analogWrite(5, 0);
  analogWrite(9, 0);
  analogWrite(10, sp);
}

void Right(byte sp) {
  analogWrite(6, 0);
  analogWrite(5, sp);
  analogWrite(9, sp);
  analogWrite(10, 0);
}

void Stop() {
  analogWrite(6, 0);
  analogWrite(5, 0);
  analogWrite(9, 0);
  analogWrite(10, 0);
}
