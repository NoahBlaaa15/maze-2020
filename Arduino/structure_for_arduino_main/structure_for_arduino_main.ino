#include "Wire.h"

//Pin where interrupts happen
const byte interruptPin = 2;
//Variable for status of interruptPin
volatile byte state = LOW;

String message;

const int threshold_tile = 500;
int target_posLH = 0;
int target_posLV = 0;
int target_posRV = 0;
int target_posRH = 0;
long newPositionLH;
long newPositionLV;
long newPositionRV;
long newPositionRH;

const byte gray1 = UNDEFINED;

const byte button1 = UNDEFINED;

const int EncoderLinksHinten = 12;
int realPosLH = 0;
long oldPositionLH  = -999;

const int EncoderLinksVorne = 12;
int realPosLV = 0;
long oldPositionLV  = -999;

const int EncoderRechtsVorne = 12;
int realPosRV = 0;
long oldPositionRV  = -999;

const int EncoderRechtsHinten = 12;
int realPosRH = 0;
long oldPositionRH  = -999;

int ELH = UNDEFINED;//MotorLinksHinten    Enable Pin
int ELV = UNDEFINED;//MotorLinksVorne     Enable Pin
int ERV = UNDEFINED;//MotorRechtsVorne    Enable Pin
int ERH = UNDEFINED;//MotorRechtsHinten   Enable Pin

int MLH = UNDEFINED;
int MLV = UNDEFINED;
int MRV = UNDEFINED;
int MRH = UNDEFINED;

const int MINI_ADDR = 0x1F;
const int MPU_ADDR = 0x68;// I2C address of the MPU-6050.
int16_t accelerometer_x, accelerometer_y, accelerometer_z; // variables for accelerometer raw data
int16_t gyro_x, gyro_y, gyro_z; // variables for gyro raw data
int16_t temperature; // variables for temperature data
char tmp_str[7]; // temporary variable used in convert function
char* convert_int16_to_str(int16_t i) { // converts int16 to string. Moreover, resulting strings will have the same length in the debug monitor.
  sprintf(tmp_str, "%6d", i);
  return tmp_str;
}

int IRlinkshinten = 0;
int IRlinksvorne = 0;
int IRvorne = 0;
int IRrechtsvorne = 0;
int IRrechtshinten = 0;

int gyro_x = 0;
int gyro_y = 0;
int gyro_z = 0;

int grayscale = 0;

int touch = 0;

void setup() {
  //Configure the interruptPin for interrupts
  pinMode(interruptPin, INPUT_PULLUP);
  //Attach the interrupt to the interrupt pin and connect with the interrupt function
  attachInterrupt(digitalPinToInterrupt(interruptPin), interrupt_detected, RISING);
  
  //Init all sensors
  Serial.begin(9600);

  pinMode(MLH, OUTPUT); //MotorLinksHinten    Signal Pin.
  pinMode(MLV, OUTPUT); //MotorLinksVorne     Signal Pin.
  pinMode(MRV, OUTPUT); //MotorRechtsVorne    Signal Pin.
  pinMode(MRH, OUTPUT); //MotorRechtsHinten   Signal Pin.
  
  pinMode(touch1, INPUT);

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
  delay(10);
}

void read_data() {
  read_ir();
  read_gyro();
  read_temperature();
  read_grayscale();
  read_touch();
}

void read_ir() {
  Wire.beginTransmission();
  Wire.requestFrom(MINI_ADDR, 5, true);
  IRlinkshinten = Wire.read();
  IRlinksvorne = Wire.read();
  IRvorne = Wire.read();
  IRrechtsvorne = Wire.read();
  IRrechtshinten = Wire.read();
  Wire.endTransmission();
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
  grayscale = analogRead(gray1);
}

void read_touch() {
  touch = digitalRead(button1);
}

void interrupt_detected() {
  //Listen on serial port for command
  if (Serial.available()) {
    message = Serial.readStringUntil('#');
    if (message == "pls") {
      //Daten formatieren
      Serial.write("[ "IRsensorLinksHinten", "IRsensorLinksVorne", "IRsensorVorneLinks", "IRsensorVorneRechts", "IRsensorRechtsVorne", "IRsensorRechtsHinten", "gyro_x", "gyro_y", "gyro_z", "grayscale", "touch" ]");
      message = "";
    }
    else if (message == "straight") {
      //Fahren und encoder die ganze Zeit mit updaten
        target_posLH = realPosLH + threshold_tile;
        target_posLV = realPosLV + threshold_tile;
        target_posRV = realPosRV + threshold_tile;
        target_posRH = realPosRH + threshold_tile;
        digitalWrite(MLH,HIGH);
        digitalWrite(MLV,HIGH);
        digitalWrite(MRV,HIGH);
        digitalWrite(MRH,HIGH);
        analogWrite(ELH, 255);   //PWM Speed Control
        analogWrite(ELV, 255);   //PWM Speed Control
        analogWrite(ERV, 255);   //PWM Speed Control
        analogWrite(ERH, 255);   //PWM Speed Control
        while true {
          //Motor links hinten auslesen
          if (newPositionLH != oldPositionLH) {
            long newPositionLH = EncoderLinksHinten.read();
            oldPositionLH = newPositionLH;
            realPosLH = realPosLH + 1;
          }
          //Motor links vorne auslesen
          if (newPositionLV != oldPositionLV) {
            long newPositionLV = EncoderLinksVorne.read();
            oldPositionLV = newPositionLV;
            realPosLV = realPosLV + 1;
          }
          //Motor rechts vorne auslesen
          if (newPositionRV != oldPositionRV) {
            long newPositionRV = EncoderRechtsVorne.read();
            oldPositionRV = newPositionRV;
            realPosRV = realPosRV + 1;
          }
          //Motor rechts hinten auslesen
          if (newPositionRH != oldPositionRH) {
            long newPositionRH = EncoderRechtsHinten.read();
            oldPositionRH = newPositionRH;
            realPosRH = realPosRH + 1;
          }

          //Ist Motor links hinten am Ziel?
          if (realPosLH >= target_posLH) {
            //Speed 0
            digitalWrite(MLH,LOW);
            analogWrite(ELH, 0);
            realPosLH = target_posLH;
          }
          //Ist Motor links vorne am Ziel?
          if (realPosLV >= target_posLV) {
            //Speed 0
            digitalWrite(MLV,LOW);
            analogWrite(ELV, 0);
            realPosLV = target_posLV;
          }
          //Ist Motor rechts vorne am Ziel?
          if (realPosRV >= target_posRV) {
            //Speed 0
            digitalWrite(MRV,LOW);
            analogWrite(ERV, 0);
            realPosRV = target_posRV;
          }
          //Ist Motor rechts vorne am Ziel?
          if (realPosRH >= target_posRH) {
            //Speed 0
            digitalWrite(MRH,LOW);
            analogWrite(ERH, 0);
            realPosRH = target_posRH;
          }
          //Sind alle am Ziel?
          if (realPosLH == target_posLH && realPosLV == target_posLV && realPosRV == target_posRV && realposRH == target_posRH) {
            break;
          }
        }
      Serial.write("angekommen#");
      message = "";
    }
    else if (message.substring(0, 4) == "turn") {
      int degrees = message.substring(4).toInt();
      target_posLH = realPosLH + threshold_tile;
      target_posLV = realPosLV + threshold_tile;
      target_posRV = realPosRV + threshold_tile;
      target_posRH = realPosRH + threshold_tile;
      digitalWrite(MLH,LOW);
      digitalWrite(MLV,LOW);
      digitalWrite(MRV,HIGH);
      digitalWrite(MRH,HIGH);
      analogWrite(ELH, 255);   //PWM Speed Control
      analogWrite(ELV, 255);   //PWM Speed Control
      analogWrite(ERV, 255);   //PWM Speed Control
      analogWrite(ERH, 255);   //PWM Speed Control
      while true {
          //Motor links hinten auslesen
          if (newPositionLH != oldPositionLH) {
            long newPositionLH = EncoderLinksHinten.read();
            oldPositionLH = newPositionLH;
            realPosLH = realPosLH + 1;
          }
          //Motor links vorne auslesen
          if (newPositionLV != oldPositionLV) {
            long newPositionLV = EncoderLinksVorne.read();
            oldPositionLV = newPositionLV;
            realPosLV = realPosLV + 1;
          }
          //Motor rechts vorne auslesen
          if (newPositionRV != oldPositionRV) {
            long newPositionRV = EncoderRechtsVorne.read();
            oldPositionRV = newPositionRV;
            realPosRV = realPosRV + 1;
          }
          //Motor rechts hinten auslesen
          if (newPositionRH != oldPositionRH) {
            long newPositionRH = EncoderRechtsHinten.read();
            oldPositionRH = newPositionRH;
            realPosRH = realPosRH + 1;
          }

          //Ist Motor links hinten am Ziel?
          if (realPosLH >= target_posLH) {
            //Speed 0
            digitalWrite(MLH,LOW);
            analogWrite(ELH, 0);
            realPosLH = target_posLH;
          }
          //Ist Motor links vorne am Ziel?
          if (realPosLV >= target_posLV) {
            //Speed 0
            digitalWrite(MLV,LOW);
            analogWrite(ELV, 0);
            realPosLV = target_posLV;
          }
          //Ist Motor rechts vorne am Ziel?
          if (realPosRV >= target_posRV) {
            //Speed 0
            digitalWrite(MRV,LOW);
            analogWrite(ERV, 0);
            realPosRV = target_posRV;
          }
          //Ist Motor rechts vorne am Ziel?
          if (realPosRH >= target_posRH) {
            //Speed 0
            digitalWrite(MRH,LOW);
            analogWrite(ERH, 0);
            realPosRH = target_posRH;
          }
          //Sind alle am Ziel?
          if (realPosLH == target_posLH && realPosLV == target_posLV && realPosRV == target_posRV && realposRH == target_posRH) {
            break;
          }
        }
      Serial.write("angekommen#");
      message = "";
    }
  }
}
