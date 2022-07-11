#include <SPI.h> //Library for using SPI Communication 
#include <mcp2515.h> //Library for using CAN Communication
const int buttonPin = 6;     // the number of the pushbutton pin
int buttonState = 0;         // variable for reading the pushbutton status
struct can_frame canMsg; 
MCP2515 mcp2515(10); // SPI CS Pin 10 
​
void setup() {
  SPI.begin();   //Begins SPI communication
  Serial.begin(9600); //Begins Serial Communication at 9600 baud rate 
  mcp2515.reset();                          
  mcp2515.setBitrate(CAN_500KBPS,MCP_8MHZ); //Sets CAN at speed 500KBPS and Clock 8MHz 
  mcp2515.setNormalMode();  //Sets CAN at normal mode
  pinMode(buttonPin, INPUT);
}
​
void loop(){
​
//  buttonState = digitalRead(buttonPin);
//
//  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
//  if (buttonState == HIGH) {
//    // turn LED on:
//    Serial.println(" Door is open ");
//  } else {
//    // turn LED off:
//    Serial.println(" Door is close ");
//  }
 if ((mcp2515.readMessage(&canMsg) == MCP2515::ERROR_OK) && (canMsg.can_id == 0x036)){
        buttonState = digitalRead(buttonPin);
​
  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if (buttonState == HIGH) {
    // turn LED on:
   String  m ="Door is close";
  } else {
    // turn LED off:
    String m =" Door is open ";
  }     
    String p =":";
     int Tc = canMsg.data[1];
     int psi = canMsg.data[0];  
     int wTc = canMsg.data[3];    
     Serial.println(Tc + p + psi + p + wTc + p + m );
          
   }
}
