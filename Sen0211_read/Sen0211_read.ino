int Analog0 = 2;

void setup() {
  Serial.begin(9600);
  pinMode(Analog0, INPUT);
}

void loop() {
  int Sen0211_value = analogRead(Analog0);

  Serial.println(Sen0211_value);
  delay(100);
    }
  
