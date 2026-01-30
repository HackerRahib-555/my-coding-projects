int led1Pin = 8;
int led2Pin = 7;
bool blinkMode = false;
unsigned long previousMillis = 0;
const long interval = 500; // 0.5s

void setup() {
  pinMode(led1Pin, OUTPUT);
  pinMode(led2Pin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // Check serial input
  if (Serial.available() > 0) {
    char cmd = Serial.read();

    if (cmd == '1') {
      digitalWrite(led1Pin, HIGH);
      Serial.println("LED 1 ON");
    } 
    else if (cmd == '0') {
      digitalWrite(led1Pin, LOW);
      Serial.println("LED 1 OFF");
    } 
    else if (cmd == '3') {
      digitalWrite(led2Pin, HIGH);
      Serial.println("LED 2 ON");
    } 
    else if (cmd == '4') {
      digitalWrite(led2Pin, LOW);
      Serial.println("LED 2 OFF");
    } 
    else if (cmd == '5') {
      blinkMode = true;
      Serial.println("Blink mode ON (alternating)");
    } 
    else if (cmd == '6') {
      blinkMode = false;
      digitalWrite(led1Pin, LOW);
      digitalWrite(led2Pin, LOW);
      Serial.println("Blink mode OFF (both LEDs OFF)");
    }
  }

  // Handle blink mode (alternate LEDs)
  if (blinkMode) {
    unsigned long currentMillis = millis();
    if (currentMillis - previousMillis >= interval) {
      previousMillis = currentMillis;

      // Alternate: LED1 = !LED1, LED2 = opposite of LED1
      bool led1State = digitalRead(led1Pin);
      digitalWrite(led1Pin, !led1State);
      digitalWrite(led2Pin, led1State);
    }
  }
}
