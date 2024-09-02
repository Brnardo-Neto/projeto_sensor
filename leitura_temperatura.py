void setup() {
  Serial.begin(9600);
}

void loop() {
  int sensorValue = analogRead(A0);
  
  float voltage = sensorValue * (5.0 / 1023.0);
  
  float temperatureC = (voltage - 0.5) * 100;
  
  Serial.print("Temperatura: ");
  Serial.print(temperatureC);
  Serial.println(" *C");
  
  delay(1000);
}