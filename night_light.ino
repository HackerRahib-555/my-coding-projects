// Pins
const int photoPin = A0;   // Photoresistor input
const int ledPin = 11;      // LED on PWM pin

// States
bool photoEnabled = true;
bool ledEnabled = true;

void setup() {
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  int lightValue = 0;
  int brightness = 0;

  // Only read photoresistor if enabled
  if (photoEnabled) {
    lightValue = analogRead(photoPin); // range 0-1023
    brightness = map(lightValue, 0, 255, 1023, 0); // darker = brighter LED
  }

  // Only write to LED if enabled
  if (ledEnabled) {
    analogWrite(ledPin, brightness);
  } else {
    analogWrite(ledPin, 0);
  }

  // Send serial data
  Serial.print("Light: ");
  Serial.print(lightValue);
  Serial.print(" | Brightness: ");
  Serial.print(brightness);
  Serial.print(" | LED: ");
  Serial.print(ledEnabled ? "ON" : "OFF");
  Serial.print(" | Photo: ");
  Serial.println(photoEnabled ? "ENABLED" : "DISABLED");

  // Check for serial commands
  if (Serial.available()) {
    char cmd = Serial.read();

    switch (cmd) {
      case 'P': // Toggle photoresistor
        photoEnabled = !photoEnabled;
        Serial.println(photoEnabled ? "Photoresistor ENABLED" : "Photoresistor DISABLED");
        break;

      case 'L': // Toggle LED
        ledEnabled = !ledEnabled;
        Serial.println(ledEnabled ? "LED ENABLED" : "LED DISABLED");
        break;

      case 'p': // Force photo OFF
        photoEnabled = false;
        Serial.println("Photoresistor DISABLED");
        break;

      case 'l': // Force LED OFF
        ledEnabled = false;
        Serial.println("LED DISABLED");
        break;
    }
  }

  delay(200); // update rate
}
