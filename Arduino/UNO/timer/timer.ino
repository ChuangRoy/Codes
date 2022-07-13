int _time ;

void setup(){  // put your setup code here, to run once:
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
  _time = 0 ;

}



void loop(){  // put your main code here, to run repeatedly:
  timer();
}

void timer() { //customised function
  Serial.print(_time); //print message
  Serial.print(" "); //print a blank
  Serial.println();
  _time = ( _time + 1 ) ;
  delay( 1000 ); // waits a few milliseconds 
}
