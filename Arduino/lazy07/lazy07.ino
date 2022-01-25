void setup() {
  Serial.begin(115200);
  for(int num=1;num>=9;num++){
    
    for(int num2=1;num>=9;num++){
      Serial.println(num*num2);
      delay(1);
    }
  
  }
}

void loop() {
  
  

}
