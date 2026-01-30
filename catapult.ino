#include <Servo.h>

Servo s;
const int servoPin = 5;
const int buttonPin = 3;

int restAngle = 10;    // resting position
int loadAngle = 70;    // pulled-back position
int fireAngle = 120;   // launch position

unsigned long lastDeb = 0;
const unsigned long debDelay = 50;

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);  // button active LOW
  s.attach(servoPin);
  s.write(restAngle);                // start safe
  Serial.begin(115200);
}

void rampTo(int target, int stepDelay=10) {
  int cur = s.read();
  if (cur < target) {
    for (int a = cur; a <= target; a++) { s.write(a); delay(stepDelay); }
  } else {
    for (int a = cur; a >= target; a--) { s.write(a); delay(stepDelay); }
  }
}

void loop() {
  if (digitalRead(buttonPin) == LOW && millis() - lastDeb > debDelay) {
    lastDeb = millis();
    Serial.println("Loading...");
    rampTo(loadAngle, 8);    // pull back slowly
    delay(200);
    Serial.println("FIRE!");
    rampTo(fireAngle, 1);    // snap forward
    delay(250);              // let it swing
    rampTo(restAngle, 6);    // reset slowly
  }
}
