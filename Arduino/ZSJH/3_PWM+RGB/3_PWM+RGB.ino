// C++ code
//
int r=3,g=6,b=5;
void setup()
{
  pinMode(r, OUTPUT);
  pinMode(g, OUTPUT);
  pinMode(b, OUTPUT);
}

void loop()
{
  analogWrite(r, 1);
  analogWrite(g, 0);
  analogWrite(b, 255);
  delay(10); // Delay a little bit to improve simulation performance
}