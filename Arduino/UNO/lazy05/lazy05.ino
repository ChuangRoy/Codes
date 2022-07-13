void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.println("攝氏轉華氏");
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()){
    int num=Serial.parseInt();
    Serial.print(num*9/5+32);
    Serial.println("℉");
  }
}
