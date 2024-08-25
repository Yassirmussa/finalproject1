const int buttonPin = 13;  // Pin connected to the button (e.g., G12)

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);  // Enable internal pull-up resistor
  Serial.begin(115200);
}

void loop() {
  int buttonState = digitalRead(buttonPin);  // Read the state of the button
  if (buttonState == LOW) {  // Button is pressed (active low)
    Serial.println("Button pressed!");
  } else {
    Serial.println("Button not pressed.");
  }
  delay(3000);
}
