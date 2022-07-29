#define CURRENT 30

void setup() {
  Serial.begin(9600);
  pinMode(A0, INPUT);
}

void loop() {
  float volt = analogRead(A0) * (5.0 / 1024);
  float current = -(volt - 2.5) * (CURRENT / 2);
  float power = current * 220;
  
  Serial.print("volt :\t");
  Serial.print(volt);
  Serial.print("  |  current :\t");
  Serial.print(current);
  Serial.print("  |  power :\t");
  Serial.print(power);
  Serial.println();
  delay(10);
}
