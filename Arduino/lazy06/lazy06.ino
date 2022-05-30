void setup() {
  Serial.begin(115200);

}

void loop() {
  if(Serial.available()){
    int num=Serial.parseInt();
    switch(num){
      case 1:
        Serial.println("A");
        break;
      case 2:
        Serial.println("B");
        break;
      case 3:
        Serial.println("C");
        break;
      case 4:
        Serial.println("D");
        break;
      case 5:
        Serial.println("E");
       break;
        default:
        Serial.println("Invalid number");
    }
  }
}
