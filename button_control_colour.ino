const int buttonPin = 3;

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  if(digitalRead(buttonPin) == LOW) {
    Serial.println("BUTTON");
    delay(300); // simple debounce
  }
}
