#define TILT_PIN 11
#define BUZZER_PIN 10

bool sensorActive = true;

void setup() {
  Serial.begin(9600);
  pinMode(TILT_PIN, INPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  digitalWrite(BUZZER_PIN, LOW);
}

void loop() {
  // Check for serial commands
  if (Serial.available() > 0) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim(); // remove whitespace/newlines

    if (cmd.equalsIgnoreCase("ON")) {
      sensorActive = true;
      Serial.println("Tilt sensor activated");
    } else if (cmd.equalsIgnoreCase("OFF")) {
      sensorActive = false;
      digitalWrite(BUZZER_PIN, LOW); // turn off buzzer
      Serial.println("Tilt sensor deactivated");
    }
  }

  // Only process tilt sensor if active
  if (sensorActive) {
    int tiltState = digitalRead(TILT_PIN);

    if (tiltState == HIGH) { 
      tone(BUZZER_PIN, 3000); // buzzer on
      Serial.println("STOLEN");
    } else {
      noTone(BUZZER_PIN); // buzzer off
      Serial.println("NOT STOLEN");
    }
  }

  delay(200); // small delay to avoid spamming serial
}
