
#include <SPI.h> //Library for using SPI Communication
#include <mcp2515.h> //Library for using CAN Communication
#include <Wire.h>
#include "MS5837.h"

MS5837 sensor;

int ThermistorPin = 0;
int Vo;
float R1 = 12000;
float logR2, R2, T, Tc, Tf;
float c1 = 1.009249522e-03, c2 = 2.378405444e-04, c3 = 2.019202697e-07;


struct can_frame canMsg;
MCP2515 mcp2515(10);

void setup(){
  while (!Serial);
  Serial.begin(9600);
  SPI.begin(); //Begins SPI communication
  
  mcp2515.reset();
  mcp2515.setBitrate(CAN_500KBPS, MCP_8MHZ); //Sets CAN at speed 500KBPS and Clock 8MHz
  mcp2515.setNormalMode();


    Serial.println("Starting");
  
  Wire.begin();

  // Initialize pressure sensor
  // Returns true if initialization was successful
  // We can't continue with the rest of the program unless we can initialize the sensor
  while (!sensor.init()) {
    Serial.println("Init failed!");
    Serial.println("Are SDA/SCL connected correctly?");

    Serial.println("\n\n\n");
    delay(5000);
     }
  
  sensor.setModel(MS5837::MS5837_30BA);
  sensor.setFluidDensity(997); // kg/m^3 (freshwater, 1029 for seawater)
}

void loop(){
  sensor.read();

  Serial.print("wheel Pressure: "); 
  float psi = 0.0145038 * sensor.pressure();
  Serial.print(psi); 
  Serial.println(" psi");
  Serial.print("wheel Temperature: "); 
  Serial.print(sensor.temperature()); 
  Serial.println(" deg C");
  

  
  Vo = analogRead(ThermistorPin);
  R2 = R1 * (1023.0 / (float)Vo - 1.0);
  logR2 = log(R2);
  T = (1.0 / (c1 + c2*logR2 + c3*logR2*logR2*logR2));
  Tc = T - 273.15;
  Tf = (Tc * 9.0)/ 5.0 + 32.0; 

  Serial.print("Temperature: "); 
 
  Serial.print(Tc);
  Serial.println(" C"); 
 
  canMsg.can_id = 0x036; //CAN id as 0x036
  canMsg.can_dlc = 8; //CAN data length as 8
  canMsg.data[0] = psi; //Update humidity value in [0]
  canMsg.data[1] = Tc; //Update temperature value in [1]
  canMsg.data[2] = 0x00; //Rest all with 0
  canMsg.data[3] = sensor.temperature();
  canMsg.data[4] = 0x00;
  canMsg.data[5] = 0x00;
  canMsg.data[6] = 0x00;
  canMsg.data[7] = 0x00;
  mcp2515.sendMessage(&canMsg); //Sends the CAN message
  delay(1000);
}
