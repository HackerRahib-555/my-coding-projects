#include <DHT.h>

#define DHTPIN A0
#define DHTTYPE DHT11
#define BUTTON_PIN 3
#define TRIG_PIN 5
#define ECHO_PIN 4
#define PHOTO_PIN A1

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
}

void loop() {
  // Button
  int buttonState = digitalRead(BUTTON_PIN);

  // Photoresistor
  int lightLevel = analogRead(PHOTO_PIN);

  // DHT11
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  // Ultrasonic
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  long duration = pulseIn(ECHO_PIN, HIGH);
  float distance = duration * 0.034 / 2;

  // Print data
  Serial.print("Button: ");
  if (buttonState == LOW) {
    Serial.println("ON");
  } else {
    Serial.println("OFF");
  }

  Serial.print("Light: ");
  Serial.println(lightLevel);

  if (!isnan(temperature) && !isnan(humidity)) {
    Serial.print("Temperature:");
    Serial.println(temperature);
    Serial.print("Humidity: ");
    Serial.println(humidity);
  } else {
    Serial.println("DHT11 Error");
  }

  Serial.print("Distance: ");
  Serial.println(distance);

  delay(1000);
}
