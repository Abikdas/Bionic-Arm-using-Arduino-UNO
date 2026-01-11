#include <Servo.h>

Servo servo[5]; 
int servoPins[5] = { 3, 5, 8, 9, 10 };

// SAFE ANGLES FOR SG90
int openAngle[5] =  { 60, 0, 0, 0, 0 };
int closeAngle[5] ={ 160, 170, 170, 170, 170};

String input;

void setup() {
  Serial.begin(9600);

  for (int i = 0; i < 5; i++) {
    servo[i].attach(servoPins[i]);
    servo[i].write(openAngle[i]);
  }
}

void loop() {
  if (Serial.available()) {
    input = Serial.readStringUntil('\n');

    int f[5];
    if (sscanf(input.c_str(), "%d,%d,%d,%d,%d",
               &f[0], &f[1], &f[2], &f[3], &f[4])
        == 5) {

      for (int i = 0; i < 5; i++) {
        servo[i].write(f[i] ? closeAngle[i] : openAngle[i]);
      }
    }
  }
}