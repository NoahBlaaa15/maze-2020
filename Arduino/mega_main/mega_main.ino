#include "Wire.h"
#include <Encoder.h>
#include <Adafruit_MLX90614.h>

String message;

const byte gray1 = A10;
const byte button1 = 27;

int temp_vl;
int temp_vr;
int temp_hr;
int temp_hl;

Adafruit_MLX90614 mlx_1 = Adafruit_MLX90614(0x5E);
Adafruit_MLX90614 mlx_2 = Adafruit_MLX90614(0x6F);
Adafruit_MLX90614 mlx_3 = Adafruit_MLX90614(0x7A);
Adafruit_MLX90614 mlx_4 = Adafruit_MLX90614(0x0B);

int threshold_tile_plus = 1400;
int threshold_tile_minus = -1 * threshold_tile_plus;
const int threshold_turn_fw = 1300;
const int threshold_turn_bw = -1 * threshold_turn_fw;

int ERV = 10;
int MRV = 11;
Encoder EncoderLH(18,22);
int ELV = 8;
int MLV = 7;
Encoder EncoderLV(19, 23);
int ELH = 12;
int MLH = 13;
Encoder EncoderRV(2, 24);
int ERH = 4;
int MRH = 5;
Encoder EncoderRH(3, 25);

int realPosLH = 0;
int realPosLV = 0;
int realPosRV = 0;
int realPosRH = 0;

int gvX, gvY, gvZ, gaX = 0;
const int ACCEL_OFFSET = 200;

const int MPU_ADDR = 0x68;// I2C address of the MPU-6050.

boolean ramp = false;


volatile float IRlinkshinten = 0;
volatile float IRlinksvorne = 0;
volatile float IRvorne = 0;
volatile float IRrechtsvorne = 0;
volatile float IRrechtshinten = 0;

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
  IRlinkshinten = analogRead(A4)*0.0048828125;
  IRlinkshinten = 13*pow(IRlinkshinten, -1);
  IRlinksvorne = analogRead(A5)*0.0048828125;
  IRlinksvorne = 13*pow(IRlinksvorne, -1);
  IRvorne = analogRead(A0)*0.0048828125;
  IRvorne = 13*pow(IRvorne, -1);
  IRrechtsvorne = analogRead(A1)*0.0048828125;
  IRrechtsvorne = 13*pow(IRrechtsvorne, -1);
  IRrechtshinten = analogRead(A2)*0.0048828125;
  IRrechtshinten = 13*pow(IRrechtshinten, -1);
}

void read_gyro() {
  Wire.beginTransmission(MPU_ADDR);
  Wire.write(0x3B); // starting with register 0x3B (ACCEL_XOUT_H) [MPU-6000 and MPU-6050 Register Map and Descriptions Revision 4.2, p.40]
  Wire.endTransmission(false); // the parameter indicates that the Arduino will send a restart. As a result, the connection is kept active.
  Wire.requestFrom(MPU_ADDR, 7*2, true); // request a total of 7*2=14 registers

  gvX = Wire.read()<<8 | Wire.read();
  gvY = Wire.read()<<8 | Wire.read();
  gvZ = Wire.read()<<8 | Wire.read();
 
  gvX = gvX - ACCEL_OFFSET;
  gvX = map(gvX, -16800, 16800, -90, 90);
  gaX = constrain(gvX, -90, 90);
  
  if(gaX <= 25){
    ramp == true;
  }else{
    ramp == false;
  }
}

void read_temperature() {
  temp_vl = mlx_1.readObjectTempC();
  temp_vr = mlx_2.readObjectTempC();
  temp_hr = mlx_3.readObjectTempC();
  temp_hl = mlx_4.readObjectTempC();
}

void read_grayscale() {
  grayscale = analogRead(gray1);
}

void read_touch() {
  touch = digitalRead(button1);
}

void straight() {
  EncoderLH.write(0);
  EncoderLV.write(0);
  EncoderRV.write(0);
  EncoderRH.write(0);
  delay(100);
  digitalWrite(MLH,HIGH);
  analogWrite(ELH,255);
  digitalWrite(MLV,HIGH);
  analogWrite(ELV,255);
  digitalWrite(MRV,HIGH);
  analogWrite(ERV,255);
  digitalWrite(MRH,HIGH);
  analogWrite(ERH,255);
  
  while (true) {
    realPosLH = EncoderLH.read();
    realPosLV = EncoderLV.read();
    realPosRV = EncoderRV.read();
    realPosRH = EncoderRH.read();

    if (realPosLH >= threshold_tile_plus) {
      digitalWrite(MLH, LOW);
      analogWrite(ELH, 0);
    }
    if (realPosLV >= threshold_tile_plus) {
      digitalWrite(MLV, LOW);
      analogWrite(ELV, 0);
    }
    if (realPosRV <= threshold_tile_minus) {
      digitalWrite(MRV, LOW);
      analogWrite(ERV, 0);
    }
    if (realPosRH <= threshold_tile_minus) {
      digitalWrite(MRH, LOW);
      analogWrite(ERH, 0);
    }
    if (realPosLH >= threshold_tile_plus && realPosLV > threshold_tile_plus && realPosRV <= threshold_tile_minus && realPosRH <= threshold_tile_minus) {
      break;
    }
  }
}

void reverse() {
  EncoderLH.write(0);
  EncoderLV.write(0);
  EncoderRV.write(0);
  EncoderRH.write(0);
  delay(100);
  digitalWrite(MLH,LOW);
  analogWrite(ELH,255);
  digitalWrite(MLV,LOW);
  analogWrite(ELV,255);
  digitalWrite(MRV,LOW);
  analogWrite(ERV,255);
  digitalWrite(MRH,LOW);
  analogWrite(ERH,255);

  while (true) {
    realPosLH = EncoderLH.read();
    realPosLV = EncoderLV.read();
    realPosRV = EncoderRV.read();
    realPosRH = EncoderRH.read();

    if (realPosLH <= threshold_tile_minus) {
      digitalWrite(MLH, LOW);
      analogWrite(ELH, 0);
    }
    if (realPosLV <= threshold_tile_minus) {
      digitalWrite(MLV, LOW);
      analogWrite(ELV, 0);
    }
    if (realPosRV >= threshold_tile_plus) {
      digitalWrite(MRV, LOW);
      analogWrite(ERV, 0);
    }
    if (realPosRH >= threshold_tile_plus) {
      digitalWrite(MRH, LOW);
      analogWrite(ERH, 0);
    }
    if (realPosLH <= threshold_tile_minus and realPosLV <= threshold_tile_minus and realPosRV >= threshold_tile_plus and realPosRH >= threshold_tile_plus) {
      break;
    }
  }
}

void right() {
  EncoderLH.write(0);
  EncoderLV.write(0);
  EncoderRV.write(0);
  EncoderRH.write(0);
  delay(100);
  digitalWrite(MLH,HIGH);
  analogWrite(ELH,255);
  digitalWrite(MLV,HIGH);
  analogWrite(ELV,255);
  digitalWrite(MRV,LOW);
  analogWrite(ERV,255);
  digitalWrite(MRH,LOW);
  analogWrite(ERH,255);

  while (true) {
    realPosLH = EncoderLH.read();
    realPosLV = EncoderLV.read();
    realPosRV = EncoderRV.read();
    realPosRH = EncoderRH.read();

    if (realPosLH >= threshold_turn_fw) {
      digitalWrite(MLH, LOW);
      analogWrite(ELH, 0);
    }
    if (realPosLV >= threshold_turn_fw) {
      digitalWrite(MLV, LOW);
      analogWrite(ELV, 0);
    }
    if (realPosRV >= threshold_turn_fw) {
      digitalWrite(MRV, LOW);
      analogWrite(ERV, 0);
    }
    if (realPosRH >= threshold_turn_fw) {
      digitalWrite(MRH, LOW);
      analogWrite(ERH, 0);
    }
    if (realPosLH >= threshold_turn_fw and realPosLV >= threshold_turn_fw and realPosRV >= threshold_turn_fw and realPosRH >= threshold_turn_fw) {
      break;
    }
  }
}

void left() {
  EncoderLH.write(0);
  EncoderLV.write(0);
  EncoderRV.write(0);
  EncoderRH.write(0);
  delay(100);
  digitalWrite(MLH,LOW);
  analogWrite(ELH,255);
  digitalWrite(MLV,LOW);
  analogWrite(ELV,255);
  digitalWrite(MRV,HIGH);
  analogWrite(ERV,255);
  digitalWrite(MRH,HIGH);
  analogWrite(ERH,255);

  while (true) {
    realPosLH = EncoderLH.read();
    realPosLV = EncoderLV.read();
    realPosRV = EncoderRV.read();
    realPosRH = EncoderRH.read();

    if (realPosLH <= threshold_turn_bw) {
      digitalWrite(MLH, LOW);
      analogWrite(ELH, 0);
    }
    if (realPosLV <= threshold_turn_bw) {
      digitalWrite(MLV, LOW);
      analogWrite(ELV, 0);
    }
    if (realPosRV <= threshold_turn_bw) {
      digitalWrite(MRV, LOW);
      analogWrite(ERV, 0);
    }
    if (realPosRH <= threshold_turn_bw) {
      digitalWrite(MRH, LOW);
      analogWrite(ERH, 0);
    }
    if (realPosLH <= threshold_turn_bw and realPosLV <= threshold_turn_bw and realPosRV <= threshold_turn_bw and realPosRH <= threshold_turn_bw) {
      break;
    }
  }
}

void setup() {
  Serial.begin(9600);

  mlx_1.begin();
  mlx_2.begin(); 
  mlx_3.begin();
  mlx_4.begin();

  pinMode(MLH,OUTPUT);
  pinMode(ELH,OUTPUT);
  pinMode(MLV,OUTPUT);
  pinMode(ELV,OUTPUT);
  pinMode(MRV,OUTPUT);
  pinMode(ERV,OUTPUT);
  pinMode(MRH,OUTPUT);
  pinMode(ERH,OUTPUT);
  
  pinMode(button1, INPUT);
  
  Wire.begin();
  Wire.beginTransmission(MPU_ADDR);
  Wire.write(0x6B);
  Wire.write(0);
  Wire.endTransmission();

}

void loop() {
  delay(25);
}

void serialEvent() {
  while(Serial.available()) {
    message = Serial.readStringUntil('#');
    if (message == "pls") {
      pinMode(LED_BUILTIN, OUTPUT);
      digitalWrite(LED_BUILTIN, HIGH);
      //Daten formatieren
        read_data();
        delay(10);
      Serial.println(String("[ " + String(IRlinkshinten)
      + ", " + String(IRlinksvorne) + ", " + String(IRvorne) + ", " + String(IRrechtsvorne) 
      + ", " + String(IRrechtshinten) + ", " + String(grayscale) + ", " + String(touch)
      + ", " + String(temp_vl) + ", " + String(temp_vr) + ", " + String(temp_hl) 
      + ", " + String(temp_hr) + ", " + String(gaX) + " ]#"));
      message = "";
    }
    else if (message == "straight") {
      straight();
    }
    else if (message == "reverse") {
      reverse();
    }
    else if (message == "right") {
      right();
    }
    else if (message == "left") {
      left();
    }
  }
}
