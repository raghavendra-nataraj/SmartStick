#include "RCSwitch.h"
RCSwitch mySwitch1 = RCSwitch(); 
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  // Transmitter is connected to Arduino Pin #10  
  mySwitch1.enableReceive(0);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (mySwitch1.available()) {
 
    int value = mySwitch1.getReceivedValue();
    int left = value & (1<<2);
    int right = value & (1<<1);
    int center = value & 01;
   Serial.print( left | right | center);
     
 
    mySwitch1.resetAvailable();
}
delay(200);
}
