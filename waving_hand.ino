#include <Servo.h>

#define TRIG_PIN 6
#define ECHO_PIN 5
#define SERVO_PIN 7

Servo myServo;

bool sensorEnabled = true;
bool waving = false;

long getDistance() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  long duration = pulseIn(ECHO_PIN, HIGH);
  long distance = duration * 0.034 / 2; // cm
  return distance;
}

void waveServo() {
  waving = true;
  Serial.println("Servo is waving!");
  for (int i = 0; i < 3; i++) {   // wave 3 times
    myServo.write(60);
    delay(400);
    myServo.write(120);
    delay(400);
  }
  myServo.write(90); // reset to center
  waving = false;
}

void setup() {
  Serial.begin(9600);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  myServo.attach(SERVO_PIN);
  myServo.write(90);
  Serial.println("System Ready. Type ON/OFF/WAVE in Serial Monitor.");
}

void loop() {
  // Handle serial commands
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    command.trim();

    if (command.equalsIgnoreCase("ON")) {
      sensorEnabled = true;
      Serial.println("Sensor enabled.");
    } else if (command.equalsIgnoreCase("OFF")) {
      sensorEnabled = false;
      Serial.println("Sensor disabled.");
    } else if (command.equalsIgnoreCase("WAVE")) {
      waveServo();
    }
  }

  // Sensor logic
  if (sensorEnabled) {
    long distance = getDistance();
    Serial.print("Distance: ");
    Serial.print(distance);
    Serial.println(" cm");

    if (distance > 0 && distance < 20 && !waving) {
      waveServo();
    }
  }

  delay(300); // prevent spamming serial
}
