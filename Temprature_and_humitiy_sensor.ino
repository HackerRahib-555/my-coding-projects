#include <DHT.h>
#include <Servo.h>

// Pin setup
#define DHTPIN A0
#define DHTTYPE DHT11
#define SERVO_PIN 9

DHT dht(DHTPIN, DHTTYPE);
Servo myServo;

// Global variable
bool sensorEnabled = false;

void setup() {
  Serial.begin(9600);
  dht.begin();
  myServo.attach(SERVO_PIN);
  Serial.println("Send 'ON' or 'OFF' to control the DHT11 system.");
}

void loop() {
  // --- Read commands from Serial ---
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    command.trim(); // remove spaces/newlines
    if (command == "ON") {
      sensorEnabled = true;
      Serial.println("DHT11 ENABLED");
    } else if (command == "OFF") {
      sensorEnabled = false;
      Serial.println("DHT11 DISABLED");
      myServo.write(0); // reset servo
    }
  }

  // --- If sensor is enabled, read data and act ---
  if (sensorEnabled) {
    float h = dht.readHumidity();
    float t = dht.readTemperature();

    if (!isnan(h) && !isnan(t)) {
      // Send data to Python
      Serial.print("TEMP:");
      Serial.println(t);
      Serial.print("HUM:");
      Serial.println(h);

      // Send alert if temperature > 25°C
      if (t > 30) {
        Serial.println("ALERT: TEMPERATURE TOO HIGH");
      }

      // Servo speed/position simulation
      int servoPos;
      if (t > 30) {
        servoPos = 180; // Full speed
      } else if (t > 15) {
        servoPos = 120; // Medium
      } else if (t > 5) {
        servoPos = 60;  // Slow
      } else if (t > 0) {
        servoPos = 30;  // Very slow
      } else {
        servoPos = 0;   // Stop
      }
      myServo.write(servoPos);
    }

    delay(2000); // wait 2 seconds before next reading
  }
}
