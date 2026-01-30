const int trigPin = 6;
const int echoPin = 5;
const int buzzerPin = 10;
const int ledPin = 11;

bool sensorEnabled = false;  // tracks whether sensor system is ON

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(buzzerPin, OUTPUT);
  pinMode(ledPin, OUTPUT);

  Serial.begin(9600);
  Serial.println("Ultrasonic Sensor System Ready");
}

void loop() {
  // Check for serial commands
  if (Serial.available() > 0) {
    char cmd = Serial.read();
    if (cmd == '1') {
      sensorEnabled = true;
      digitalWrite(ledPin, HIGH);
      Serial.println("Sensor Enabled");
    } 
    else if (cmd == '0') {
      sensorEnabled = false;
      digitalWrite(ledPin, LOW);
      digitalWrite(buzzerPin, LOW); // stop buzzer
      Serial.println("Sensor Disabled");
    }
  }

  if (sensorEnabled) {
    long duration, distance;

    // Trigger ultrasonic pulse
    digitalWrite(trigPin, LOW);
    delay(300);
    digitalWrite(trigPin, HIGH);
    delay(300);
    digitalWrite(trigPin, LOW);

    // Measure echo duration
    duration = pulseIn(echoPin, HIGH);

    // Convert to distance in cm
    distance = duration * 0.034 / 2;

    Serial.print("Distance: ");
    Serial.print(distance);
    Serial.println(" cm");

    // If object within 20cm, alert + beep
    if (distance > 0 && distance <= 20) {
      Serial.println("ALERT: Object detected within 20cm!");
      
      // Simple beep
      tone(buzzerPin, 2400, 400);
      delay(400);
      digitalWrite(buzzerPin, LOW);
      delay(400);
    }
  }
}
