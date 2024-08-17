#define TRIG_PIN 5
#define ECHO_PIN 19
#define DISTANCE_THRESHOLD 50   // Adjust this threshold for detecting a person
#define EXIT_THRESHOLD 100      // Adjust this threshold to detect when the person leaves

long lastDistance = 0;
int peopleCount = 0;
bool enteringDetected = false;  // Detect the first threshold (entering)
bool exitingDetected = false;   // Detect the second threshold (exiting)

void setup() {
  Serial.begin(115200);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
}

void loop() {
  // Clear the trigger pin
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);

  // Send a pulse to the TRIG pin
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  // Measure the duration of the pulse on the ECHO pin
  long duration = pulseIn(ECHO_PIN, HIGH);

  // Calculate distance in centimeters
  float distance = duration * 0.0344 / 2;

  // Print distance to serial monitor
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  // Detect when a person enters the detection zone
  if (distance < DISTANCE_THRESHOLD && !enteringDetected) {
    enteringDetected = true; // Person is entering
    exitingDetected = false; // Reset exit detection
  }

  // Detect when the person exits the detection zone
  if (enteringDetected && distance > EXIT_THRESHOLD && !exitingDetected) {
    exitingDetected = true; // Person has exited
    peopleCount++;          // Count one person
    enteringDetected = false; // Reset for the next person
    Serial.print("People count: ");
    Serial.println(peopleCount);
  }

  delay(1000); // Wait for 500 milliseconds before the next measurement
}
