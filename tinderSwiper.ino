#include<Servo.h>
Servo s1,s2;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  s1.attach(11);
  s2.attach(10);
  s1.write(170);
  s2.write(170);
}

int T = 500;
int m_t=0,m_r=170;
void loop() {
  while(Serial.available()) {
    char command = Serial.read();
    if (command == 'r') {
      swipeRight();
    } else if (command == 'c') {
      center();
    } else if (command == 'l') {
      swipeLeft();
    }
    Serial.write("Read");
    writeString(String(command));
  }
  

}

void writeString(String stringData) { // Used to serially push out a String with Serial.write()

  for (int i = 0; i < stringData.length(); i++)
  {
    Serial.write(stringData[i]);   // Push each char 1 by 1 on each loop pass
  }

}// end writeString

void center() {
  s1.write(170);
  delay(100);
  s2.write(90);
  delay(100);
}

void swipeRight() {
  s1.write(170);
  delay(100);
  s2.write(90-10);
  delay(100);
  s1.write(150);
  delay(100);
  s1.write(170);
}

void swipeLeft() {
  s1.write(170);
  delay(100);
  s2.write(90+5);
  delay(100);
  s1.write(150);
  delay(100);
  s1.write(170);
}

