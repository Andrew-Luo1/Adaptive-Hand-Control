/*
  This is a test sketch for the Adafruit assembled Motor Shield for Arduino v2
  It won't work with v1.x motor shields! Only for the v2's with built in PWM
  control

  For use with the Adafruit Motor Shield v2
  ---->  http://www.adafruit.com/products/1438
*/

#include <Wire.h>
#include <Adafruit_MotorShield.h>

// Create the motor shield object with the default I2C address
Adafruit_MotorShield AFMS = Adafruit_MotorShield();
// Or, create it with a different I2C address (say for stacking)
// Adafruit_MotorShield AFMS = Adafruit_MotorShield(0x61);

// Select which 'port' M1, M2, M3 or M4. In this case, M1
Adafruit_DCMotor *myMotor = AFMS.getMotor(1);
// You can also make another motor on port M2
//Adafruit_DCMotor *myOtherMotor = AFMS.getMotor(2);
int angle = 0;
int analogPin = A1;
int read_byte = 0;
int torque = 0;
uint8_t i;
const byte numChars = 4; //reserve up to 4 bytes for the incoming serial data
char receivedChars[numChars];
boolean newData = false;

void setup() {
  Serial.begin(9600);           // set up Serial library at 9600 bps
  AFMS.begin(1600);  
  // Set the speed to start, from 0 (off) to 255 (max speed)
  myMotor->setSpeed(150);
  myMotor->run(FORWARD);
  myMotor->run(RELEASE);
  
}

void loop() {

  //angle ranges from 837 -> 233.
  //try to read from serial port
//  str_torque = Serial.readString();

//  torque = (str_torque.toInt());


//  myMotor->setSpeed(torque);
//  
//  if(torque > 1){ //I messed up my HW motor config so it needs to run backwards
//    myMotor->run(BACKWARD);
//  }
//  else{
//    myMotor->run(FORWARD);
//  }
  if (newData == true){
    angle = analogRead(analogPin);
    Serial.print(millis());
    Serial.print(" ");
    Serial.print(read_byte);
    Serial.print(" ");
    Serial.println(angle);
  }

}

void recvWithEndMarker() {
 static byte ndx = 0;
 char endMarker = '\n';
 char rc;
 
 // if (Serial.available() > 0) {
 while (Serial.available() > 0 && newData == false) {
   rc = Serial.read();
  
   if (rc != endMarker) {
   receivedChars[ndx] = rc;
   ndx++;
     if (ndx >= numChars) {
      ndx = numChars - 1;
     }
   }
   else {
     receivedChars[ndx] = '\0'; // terminate the string
     ndx = 0;
     newData = true;
   }
 }
}
