#include "ACS712.h"
ACS712 sensor(ACS712_30A, A0);

void setup() {
  Serial.begin(9600);
  sensor.calibrate();
}

void loop() {
  float I = sensor.getCurrentAC();
  if (I < 0.09) {
    I = 0;
  }
  Serial.println(I)
  delay(300);
}
