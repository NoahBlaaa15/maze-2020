#include "Wire.h"

String message;

const byte gray1 = A0;

const byte button1 = 27;

const int threshold_tile_left = 200;
const int threshold_tile_right = 250;
const int threshold_turn_left = 500;
const int threshold_turn_right = 600;

const int EncoderLH = 15;
int realPosLH = 0;
long oldPositionLH  = 0;
long newPositionLH;
int target_posLH;

const int EncoderLV = 14;
int realPosLV = 0;
long oldPositionLV  = 0;
long newPositionLV;
int target_posLV;

const int EncoderRV = 11;
int realPosRV = 0;
long oldPositionRV  = 0;
long newPositionRV;
int target_posRV;

const int EncoderRH = 10;
int realPosRH = 0;
long oldPositionRH  = 0;
long newPositionRH;
int target_posRH;

int MLH = 4;//MotorLinksHinten    Enable Pin
int MLV = 8;//MotorLinksVorne     Enable Pin
int MRV = 7;//MotorRechtsVorne    Enable Pin
int MRH = 3;//MotorRechtsHinten   Enable Pin

int ELH = 2;
int ELV = 6;
int ERV = 9;
int ERH = 5;

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

volatile int IRlinkshinten = 0;
volatile int IRlinksvorne = 0;
volatile int IRvorne = 0;
volatile int IRrechtsvorne = 0;
volatile int IRrechtshinten = 0;

int grayscale = 0;

int touch = 0;

void read_data() {
  read_ir();
  read_gyro();
  read_temperature();
  read_grayscale();
  read_touch();
}

void read_ir() {
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

void serialEvent() {
  //Listen on serial port for command
  Serial.println("interrupt#");
  while(Serial.available()) {
    message = Serial.readStringUntil('#');
    if (message == "pls") {
      //Daten formatieren
        read_data();
        delay(10);
      Serial.println(String("[ " + String(IRlinkshinten) + ", " + String(IRlinksvorne) + ", " + String(IRvorne) + ", " + String(IRrechtsvorne) + ", " + String(IRrechtshinten) + ", "+gyro_x+", "+gyro_y+", "+gyro_z+", "+grayscale+", "+touch+" ]"));
      message = "";
    }
    else if (message == "straight") {
      //Fahren und encoder die ganze Zeit mit updaten
        target_posLH = realPosLH + threshold_tile_left;
        target_posLV = realPosLV + threshold_tile_left;
        target_posRV = realPosRV + threshold_tile_right;
        target_posRH = realPosRH + threshold_tile_right;
        digitalWrite(MLH,HIGH);
        digitalWrite(MLV,HIGH);
        digitalWrite(MRV,HIGH);
        digitalWrite(MRH,HIGH);
        
        digitalWrite(ELH,HIGH);
        digitalWrite(ELV,HIGH);
        digitalWrite(ERV,LOW);//Muss low weil die reversed sind
        digitalWrite(ERH,LOW);//Muss low weil die reversed sind
        while(true) {
          //Motor links hinten auslesen
          newPositionLH = digitalRead(EncoderLH);
          if (newPositionLH != oldPositionLH) {
            oldPositionLH = newPositionLH;
            realPosLH = realPosLH + 1;
          }
          //Motor links vorne auslesen
          newPositionLV = digitalRead(EncoderLV);
          if (newPositionLV != oldPositionLV) {
            oldPositionLV = newPositionLV;
            realPosLV = realPosLV + 1;
          }
          //Motor rechts vorne auslesen
          newPositionRV = digitalRead(EncoderRV);
          if (newPositionRV != oldPositionRV) {
            oldPositionRV = newPositionRV;
            realPosRV = realPosRV + 1;
          }
          //Motor rechts hinten auslesen
          newPositionRH = digitalRead(EncoderRH);
          if (newPositionRH != oldPositionRH) {
            oldPositionRH = newPositionRH;
            realPosRH = realPosRH + 1;
          }

          //Ist Motor links hinten am Ziel?
          if (realPosLH >= target_posLH) {
            //Speed 0
            digitalWrite(MLH,LOW);
            digitalWrite(ELH, LOW);
            realPosLH = target_posLH;
          }
          //Ist Motor links vorne am Ziel?
          if (realPosLV >= target_posLV) {
            //Speed 0
            digitalWrite(MLV,LOW);
            digitalWrite(ELV, LOW);
            realPosLV = target_posLV;
          }
          //Ist Motor rechts vorne am Ziel?
          if (realPosRV >= target_posRV) {
            //Speed 0
            digitalWrite(MRV,LOW);
            digitalWrite(ERV, LOW);
            realPosRV = target_posRV;
          }
          //Ist Motor rechts hinten am Ziel?
          if (realPosRH >= target_posRH) {
            //Speed 0
            digitalWrite(MRH,LOW);
            digitalWrite(ERH, LOW);
            realPosRH = target_posRH;
          }
          //Sind alle am Ziel?
          if (realPosLH == target_posLH && realPosLV == target_posLV && realPosRV == target_posRV && realPosRH == target_posRH) {
            digitalWrite(MRH,LOW);
            digitalWrite(ERH, LOW);
            realPosRH = 0;

            digitalWrite(MRV,LOW);
            digitalWrite(ERV, LOW);
            realPosRV = 0;

            digitalWrite(MLH,LOW);
            digitalWrite(ELH, LOW);
            realPosLH = 0;

            digitalWrite(MLV,LOW);
            digitalWrite(ELV, LOW);
            realPosLV = 0;
            
            Serial.println("Alle da!#");
            break;
          }
        }
      Serial.write("angekommen#");
      message = "";
    }
    else if (message.substring(0, 4) == "turn") {
      int degrees = message.substring(4).toInt();

      if (degrees == 90) {
        target_posLH = realPosLH + threshold_turn_left;
        target_posLV = realPosLV + threshold_turn_left;
        target_posRV = realPosRV + threshold_turn_right;
        target_posRH = realPosRH + threshold_turn_right;
        digitalWrite(MLH,HIGH);
        digitalWrite(MLV,HIGH);
        digitalWrite(MRV,HIGH);
        digitalWrite(MRH,HIGH);

        digitalWrite(ELH,HIGH);
        digitalWrite(ELV,HIGH);
        digitalWrite(ERV,HIGH);//High weil reversed
        digitalWrite(ERH,HIGH);//High weil reversed
      }
      else if (degrees == 180) {
        target_posLH = realPosLH + (2 * threshold_turn_left);
        target_posLV = realPosLV + (2 * threshold_turn_left);
        target_posRV = realPosRV + (2 * threshold_turn_right);
        target_posRH = realPosRH + (2 * threshold_turn_right);

        digitalWrite(MLH,HIGH);
        digitalWrite(MLV,HIGH);
        digitalWrite(MRV,HIGH);
        digitalWrite(MRH,HIGH);
        
        digitalWrite(ELH,HIGH);
        digitalWrite(ELV,HIGH);
        digitalWrite(ERV,HIGH);//High weil reversed
        digitalWrite(ERH,HIGH);//High weil reversed
      }
      else if (degrees == -90) {
        target_posLH = realPosLH + threshold_turn_left;
        target_posLV = realPosLV + threshold_turn_left;
        target_posRV = realPosRV + threshold_turn_right;
        target_posRH = realPosRH + threshold_turn_right;
        digitalWrite(MLH,HIGH);
        digitalWrite(MLV,HIGH);
        digitalWrite(MRV,HIGH);
        digitalWrite(MRH,HIGH);

        digitalWrite(ELH,LOW);
        digitalWrite(ELV,LOW);
        digitalWrite(ERV,LOW);//Low weil reversed
        digitalWrite(ERH,LOW);//Low weil reversed
      }
        while(true) {
          //Motor links hinten auslesen
          newPositionLH = digitalRead(EncoderLH);
          if (newPositionLH != oldPositionLH) {
            oldPositionLH = newPositionLH;
            realPosLH = realPosLH + 1;
          }
          //Motor links vorne auslesen
          newPositionLV = digitalRead(EncoderLV);
          if (newPositionLV != oldPositionLV) {
            oldPositionLV = newPositionLV;
            realPosLV = realPosLV + 1;
          }
          //Motor rechts vorne auslesen
          newPositionRV = digitalRead(EncoderRV);
          if (newPositionRV != oldPositionRV) {
            oldPositionRV = newPositionRV;
            realPosRV = realPosRV + 1;
          }
          //Motor rechts hinten auslesen
          newPositionRH = digitalRead(EncoderRH);
          if (newPositionRH != oldPositionRH) {
            oldPositionRH = newPositionRH;
            realPosRH = realPosRH + 1;
          }

          //Ist Motor links hinten am Ziel?
          if (realPosLH >= target_posLH) {
            //Speed 0
            digitalWrite(MLH,LOW);
            digitalWrite(ELH,LOW);
            realPosLH = target_posLH;
          }
          //Ist Motor links vorne am Ziel?
          if (realPosLV >= target_posLV) {
            //Speed 0
            digitalWrite(MLV,LOW);
            digitalWrite(ELV,LOW);
            realPosLV = target_posLV;
          }
          //Ist Motor rechts vorne am Ziel?
          if (realPosRV >= target_posRV) {
            //Speed 0
            digitalWrite(MRV,LOW);
            digitalWrite(ERV,LOW);
            realPosRV = target_posRV;
          }
          //Ist Motor rechts vorne am Ziel?
          if (realPosRH >= target_posRH) {
            //Speed 0
            digitalWrite(MRH,LOW);
            digitalWrite(ERH,LOW);
            realPosRH = target_posRH;
          }
          //Sind alle am Ziel?
          if (realPosLH == target_posLH && realPosLV == target_posLV && realPosRV == target_posRV && realPosRH == target_posRH) {
            digitalWrite(MRH,LOW);
            digitalWrite(ERH,LOW);
            realPosRH = 0;

            digitalWrite(MRV,LOW);
            digitalWrite(ERV,LOW);
            realPosRV = 0;

            digitalWrite(MLH,LOW);
            digitalWrite(ELH,LOW);
            realPosLH = 0;

            digitalWrite(MLV,LOW);
            digitalWrite(ELV,LOW);
            realPosLV = 0;
            Serial.println("Alle sind da#");
            break;
          }
        }
      Serial.write("angekommen#");
      message = "";
    }
  }
}

void setup() {
  
  //Init all sensors
  Serial.begin(9600);
  Serial.println("Serial started#");

  pinMode(MLH, OUTPUT); //MotorLinksHinten    Signal Pin.
  pinMode(MLV, OUTPUT); //MotorLinksVorne     Signal Pin.
  pinMode(MRV, OUTPUT); //MotorRechtsVorne    Signal Pin.
  pinMode(MRH, OUTPUT); //MotorRechtsHinten   Signal Pin.
  
  pinMode(button1, INPUT);
  /*
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
  }*/
  Serial.println("Done with setup#");
}

void loop() { 
}
