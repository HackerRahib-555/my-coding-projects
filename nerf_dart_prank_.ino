#include <Servo.h>

#define TRIG_PIN 5
#define ECHO_PIN 6
#define SERVO_PIN 10
#define BUZZER_PIN 4
#define ON_BUTTON 13
#define OFF_BUTTON 12

Servo myServo;

bool systemOn = false;

  
void playWompWomp() {
  // Womp womp style notes (not exact, just vibe-y)
  tone(BUZZER_PIN, 233, 300); // A#3
  delay(350);
  tone(BUZZER_PIN, 185, 300); // F#3
  delay(350);
  tone(BUZZER_PIN, 174, 500); // F3
  delay(600);
  noTone(BUZZER_PIN);
}

void setup() {
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(ON_BUTTON, INPUT_PULLUP);
  pinMode(OFF_BUTTON, INPUT_PULLUP);
  
  myServo.attach(SERVO_PIN);
  myServo.write(90); // Start at center

  Serial.begin(9600);
}

void loop() {
  // Check buttons
  if (digitalRead(ON_BUTTON) == LOW) {
    systemOn = true;
    delay(300); // Debounce
  }

  if (digitalRead(OFF_BUTTON) == LOW) {
    systemOn = false;
    delay(300); // Debounce
  }

  if (!systemOn) return;

  // Get distance from ultrasonic
  long duration, distance;
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(0.5);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(0.5);
  digitalWrite(TRIG_PIN, LOW);

  duration = pulseIn(ECHO_PIN, HIGH);
  distance = duration * 0.034 / 2;

  if (distance > 0 && distance <= 18) {
    // Dart detected!
    int targetAngle = random(0, 181); // 90 to 180
    myServo.write(targetAngle);
    delay(2000);
    myServo.write(90);


    playWompWomp();
    // wait before checking again
  }
}
