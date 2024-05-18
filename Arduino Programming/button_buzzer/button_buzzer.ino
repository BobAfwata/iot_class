int buzzer = 8;
int button = 4;
bool button_status = false;

void setup() {
  pinMode(button, INPUT);
  pinMode(buzzer, OUTPUT);
}

void loop() {
  button_status = digitalRead(button);
  if (button_status == false) {
    int i = 0;
    while (i < 3) {
      digitalWrite(buzzer, HIGH);
      delay(100);
      digitalWrite(buzzer, LOW);
      delay(100);
      i++;
    }
  }
  else {
    digitalWrite(buzzer, LOW);
  }
}
