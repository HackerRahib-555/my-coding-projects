// Pin definitions
#define VRX A0        // Joystick X-axis
#define VRY A1        // Joystick Y-axis
#define SW 5          // Joystick switch
#define BUTTONA 3
#define BUTTONB 4

void setup() {
  Serial.begin(9600);
  
  pinMode(SW, INPUT_PULLUP);       // Joystick button
  pinMode(BUTTONA, INPUT_PULLUP);  // Button A
  pinMode(BUTTONB, INPUT_PULLUP);  // Button B
}

void loop() {
  // Read joystick axes
  int xVal = analogRead(VRX);
  int yVal = analogRead(VRY);

  // Read joystick button and other buttons
  bool joystickPressed = digitalRead(SW) == LOW;
  bool buttonAState = digitalRead(BUTTONA) == LOW;
  bool buttonBState = digitalRead(BUTTONB) == LOW;

  // Send joystick data
  Serial.print("Joystick X: "); Serial.println(xVal);
  Serial.print("Joystick Y: "); Serial.println(yVal);
  Serial.print("Joystick Pressed: "); Serial.println(joystickPressed ? "PRESSED" : "RELEASED");

  // Send button states
  Serial.print("ButtonA: "); Serial.println(buttonAState ? "PRESSED" : "RELEASED");
  Serial.print("ButtonB: "); Serial.println(buttonBState ? "PRESSED" : "RELEASED");

  delay(1000);}
