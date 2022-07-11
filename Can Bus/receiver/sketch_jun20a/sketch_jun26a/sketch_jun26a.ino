 String b =":";
  int temp = 59;
  int temp1 = 30;
  int temp2 = 505;
  int temp3 = 70;
void setup() {
  //start serial connection
  Serial.begin(9600);
 
}

void loop() {
 
  Serial.println(temp  + b + temp1 + b + temp2 + b + temp3 );
delay (500);
 
}
