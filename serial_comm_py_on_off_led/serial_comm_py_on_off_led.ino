int LED = 5;
char c;

void setup() {
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    while (Serial.available() > 0) {
      c = Serial.read();
      if (c  == '1') {
        digitalWrite(LED, HIGH);
      } else  if (c  == '0') {
        digitalWrite(LED, LOW);
      }
      Serial.print(c);
    }
  }
}
