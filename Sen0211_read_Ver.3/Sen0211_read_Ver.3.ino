//float Analog0 = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  
  float I = get_ampere();
  float Watt = I * 220.0;

  //Serial.println(analogRead(A0));
  
  Serial.print("Current: ");
  Serial.print(I, 3);
  Serial.print("A  |  Power: ");
  Serial.print(Watt, 3);
  Serial.println("W");
  
  //Serial.println(Watt, 3);
  //delay(1000);
    }


float get_ampere()
{
  float Sensor_value;
  float Current = 0;
  float Sum = 0;
  long time = millis();
  int N = 0;
  
  while(millis() - time<500)
  {
    Sensor_value = analogRead(A0) * (1 / 1023.0);
    Current = Sensor_value * 20.0;
    Sum = Sum+sq(Current);
    N = N+1;
    delay(1);
    }
    Sum=Sum * 2;
    Current = sqrt(Sum / N);
    return(Current);
  }
  
