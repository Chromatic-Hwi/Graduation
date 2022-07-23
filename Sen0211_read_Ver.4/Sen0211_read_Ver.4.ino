void setup() {
  Serial.begin(9600);
}

void loop() {
  float I = 0;
  float Watt = 0;
  float I_sum = 0;
  float Watt_sum = 0;
  
  for(int i = 0; i < 100;)
  {
    i = i + 1;
    float I = get_ampere();
    float Watt = I * 220.0;
    I_sum = I_sum + I;
    Watt_sum = Watt_sum + Watt;
    delay(10);
    }
    
  I = I_sum / 100;
  Watt = Watt_sum / 100;

  /*
  Serial.print("Current: ");
  Serial.print(I, 3);
  Serial.print("A  |  Power: ");
  Serial.print(Watt, 3);
  Serial.println("W");
  */
  Serial.println(Watt, 3);
  
    }


float get_ampere()
{
  float Sensor_value;
  float Sensor_value_sum = 0;
  float Current = 0;

  Sensor_value = analogRead(A0)*1.1;
  
  if(Sensor_value < 40)
  {
    Sensor_value = 160;
    }
    
  Sensor_value = -(Sensor_value - 160)/1024;
  Current = Sensor_value * 20.0;
  return(Current);
  }
  
