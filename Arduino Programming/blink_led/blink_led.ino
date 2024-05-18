// this is a program that blinks an LED
int led = 13; // LED connected to pin 13
int buzzer = 3; // buzzer connected to pin 3
// part of code that runs once
void setup(){
  pinMode(led, OUTPUT); // LED set as output
  pinMode(buzzer, OUTPUT); // buzzer set as output
}

// part of code that runs continuously
void loop() {
  digitalWrite(led, HIGH); // turns on the LED
  delay(50);
  digitalWrite(led, LOW); // turns it off
  delay(50);
  digitalWrite(buzzer, HIGH);
  delay(500);
  digitalWrite(buzzer, LOW);
  delay(100);
}
