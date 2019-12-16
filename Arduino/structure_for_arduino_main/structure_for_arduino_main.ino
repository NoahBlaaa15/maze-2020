#include "Wire.h"
#include <Encoder.h>

//Pin where interrupts happen
const byte interruptPin = 2;
//Variable for status of interruptPin
volatile byte state = LOW;

String message;

const byte IRsensorLinksHinten = UNDEFINED;
const byte IRsensorLinksVorne = UNDEFINED;
const byte IRsensorVorneLinks = UNDEFINED;
const byte IRsensorVorneRechts = UNDEFINED;
const byte IRsensorRechtsVorne = UNDEFINED;
const byte IRsensoRechtsHinten = UNDEFINED;

const byte gray1 = UNDEFINED;

Encoder EncoderLinksHinten(UNDEFINED,UNDEFINED);
int realPosLH = 0;
long oldPositionLH  = -999;
Encoder EncoderLinksVorne(UNDEFINED,UNDEFINED);
int realPosLV = 0;
long oldPositionLV  = -999;
Encoder EncoderRechtsVorne(UNDEFINED,3UNDEFINED);
int realPosRV = 0;
long oldPositionRV  = -999;
Encoder EncoderRechtsHinten(UNDEFINED,UNDEFINED);
int realPosRH = 0;
long oldPositionRH  = -999;

int ELH = UNDEFINED;
int ELV = UNDEFINED;
int ERV = UNDEFINED;
int ERH = UNDEFINED;

int MLH = UNDEFINED;
int MLV = UNDEFINED;
int MRV = UNDEFINED;
int MRH = UNDEFINED;

const int MPU_ADDR = 0x68;// I2C address of the MPU-6050.
int16_t accelerometer_x, accelerometer_y, accelerometer_z; // variables for accelerometer raw data
int16_t gyro_x, gyro_y, gyro_z; // variables for gyro raw data
int16_t temperature; // variables for temperature data
char tmp_str[7]; // temporary variable used in convert function
char* convert_int16_to_str(int16_t i) { // converts int16 to string. Moreover, resulting strings will have the same length in the debug monitor.
  sprintf(tmp_str, "%6d", i);
  return tmp_str;
}

void setup() {
  //Configure the interruptPin for interrupts
  pinMode(interruptPin, INPUT_PULLUP);
  //Attach the interrupt to the interrupt pin and connect with the interrupt function
  attachInterrupt(digitalPinToInterrupt(interruptPin), interrupt_detected, RISING);
  
  //Init all sensors
  Serial.begin(9600);

  pinMode(MLH, OUTPUT);
  pinMode(MLV, OUTPUT);
  pinMode(MRV, OUTPUT);
  pinMode(MRH, OUTPUT);

  Wire.begin();
  Wire.beginTransmission(MPU_ADDR); // Begins a transmission to the I2C slave (GY-521 board)
  Wire.write(0x6B); // PWR_MGMT_1 register
  Wire.write(0); // set to zero (wakes up the MPU-6050)
  Wire.endTransmission(true);
  
  //Wait until start command from raspberry pi arrives (serial)
  while (Serial.available() == 0) {
    continue;

  if (Serial.available()){
      message = Serial.readStringUntil('#');
      if (message == "start") {
        break;
      }

  }
}

void loop() {  
  read_data();
}

void read_data() {
  read_ir();
  read_gyro();
  read_temperature();
  read_grayscale();
  read_touch();
}

void read_ir() {
  float lh = analogRead(IRsensorLinksHinten)*0.0048828125;
  int IRlinkshinten = 13*pow(lh, -1);
  float lv = analogRead(IRsensorLinksVorne)*0.0048828125;
  int IRlinksvorne = 13*pow(lv, -1);
  float vl = analogRead(IRsensorVorneLinks)*0.0048828125;
  int IRvornelinks = 13*pow(vl, -1);
  float vr = analogRead(IRsensorVorneRechts)*0.0048828125;
  int IRvornerechts = 13*pow(vr, -1);
  float rv = analogRead(IRsensorRechtsVorne)*0.0048828125;
  int IRrechtsvorne = 13*pow(rv, -1);
  float rh = analogRead(IRsensorRechtsHinten)*0.0048828125;
  int IRrechtshinten = 13*pow(rh, -1);
}

void read_gyro() {
  Wire.beginTransmission(MPU_ADDR);
  Wire.write(0x3B); // starting with register 0x3B (ACCEL_XOUT_H) [MPU-6000 and MPU-6050 Register Map and Descriptions Revision 4.2, p.40]
  Wire.endTransmission(false); // the parameter indicates that the Arduino will send a restart. As a result, the connection is kept active.
  Wire.requestFrom(MPU_ADDR, 7*2, true); // request a total of 7*2=14 registers

  accelerometer_x = Wire.read()<<8 | Wire.read(); // reading registers: 0x3B (ACCEL_XOUT_H) and 0x3C (ACCEL_XOUT_L)
  accelerometer_y = Wire.read()<<8 | Wire.read(); // reading registers: 0x3D (ACCEL_YOUT_H) and 0x3E (ACCEL_YOUT_L)
  accelerometer_z = Wire.read()<<8 | Wire.read(); // reading registers: 0x3F (ACCEL_ZOUT_H) and 0x40 (ACCEL_ZOUT_L)
  temperature = Wire.read()<<8 | Wire.read(); // reading registers: 0x41 (TEMP_OUT_H) and 0x42 (TEMP_OUT_L)
  gyro_x = Wire.read()<<8 | Wire.read(); // reading registers: 0x43 (GYRO_XOUT_H) and 0x44 (GYRO_XOUT_L)
  gyro_y = Wire.read()<<8 | Wire.read(); // reading registers: 0x45 (GYRO_YOUT_H) and 0x46 (GYRO_YOUT_L)
  gyro_z = Wire.read()<<8 | Wire.read(); // reading registers: 0x47 (GYRO_ZOUT_H) and 0x48 (GYRO_ZOUT_L)
}

void read_temperature() {
  //read temperature values
  //return temperature values
}

void read_grayscale() {
  val=analogRead(gray1);
}

void read_touch() {
  //read touch values
  //return touch values
}

void interrupt_detected() {
  //Listen on serial port for command
  if (Serial.available()) {
    message = Serial.readStringUntil('#');
    if (message == "pls") {
      //Daten formatieren
      Serial.write(/*Hier alle Daten rein*/);
      message = "";
    }
    else if (message == "straight") {
      //Fahren und encoder die ganze Zeit mit updaten
        digitalWrite(MLH,HIGH);
        digitalWrite(MLV,HIGH);
        digitalWrite(MRV,HIGH);
        digitalWrite(MRH,HIGH);
        analogWrite(ELH, 255);   //PWM Speed Control
        analogWrite(ELV, 255);   //PWM Speed Control
        analogWrite(ERV, 255);   //PWM Speed Control
        analogWrite(ERH, 255);   //PWM Speed Control
        while true {
          long newPositionLinksHinten = EncoderLinksHinten.read();
          long newPositionLinksVorne = EncoderLinksVorne.read();
          long newPositionRechtsVorne = EncoderRechtsVorne.read();
          long newPositionRechtsHinten = EncoderRechtsHinten.read();
          oldPositionLH = newPositionLinksHinten;
          oldPositionLV = newPositionLinksVorne;
          oldPositionRV = newPositionRechtsVorne;
          oldPositionRH = newPositionRechtsHinten;
          realPos = realPos + 1;
          if (realPosLH == target_posLH) {
            //Speed 0 and break
          }
        }
      Serial.write("angekommen#");
      message = "";
    }
    else if (message.substring(0, 4) == "turn") {
      int degrees = message.substring(4).toInt();
      //Fahren und encoder die ganze Zeit mit updaten
      Serial.write("angekommen#");
      message = "";
    }
  }
}
