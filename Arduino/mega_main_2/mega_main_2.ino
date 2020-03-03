#include "Wire.h"
#include <Encoder.h>
#include <Adafruit_MLX90614.h>

String message;

const byte gray1 = A10;
const byte button1 = 27;

int turn_time = 600;
int straight_time = 300;

int temp_vl;
int temp_hr;
int temp_hl;

Adafruit_MLX90614 mlx_1 = Adafruit_MLX90614(0x1A);
Adafruit_MLX90614 mlx_2 = Adafruit_MLX90614(0x2B);
Adafruit_MLX90614 mlx_3 = Adafruit_MLX90614(0x3C);

int threshold_tile_plus = 1450;
int threshold_tile_minus = -1 * threshold_tile_plus;
const int threshold_turn_plus = 1750;
const int threshold_turn_minus = -1 * threshold_turn_plus;
const int threshold_wall_plus = 400;
const int threshold_wall_minus = -1 * threshold_wall_plus;

int MLV = 10;
int ELV = 11;
Encoder EncoderRH(18,22);
int ERH = 8;
int MRH = 7;
Encoder EncoderRV(19, 23);
int ERV = 4;
int MRV = 9;
Encoder EncoderLV(2, 24);
int MLH = 5;
int ELH = 6;
Encoder EncoderLH(3, 25);

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
  //read_gyro();
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
  temp_hr = mlx_2.readObjectTempC();
  temp_hl = mlx_3.readObjectTempC();
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
  //Links
  digitalWrite(ELV, HIGH);
  digitalWrite(MLV,HIGH);
  digitalWrite(ELH, HIGH);
  digitalWrite(MLH,HIGH);
  //Rechts
  digitalWrite(ERV,HIGH);
  digitalWrite(MRV,HIGH);
  digitalWrite(ERH,HIGH);
  digitalWrite(MRH,HIGH);
  
  while (true) {
    realPosLH = EncoderLH.read();
    realPosLV = EncoderLV.read();
    realPosRV = EncoderRV.read();
    realPosRH = EncoderRH.read();
    if (realPosRV >= threshold_tile_plus) {
      
      digitalWrite(ERV,LOW);
      digitalWrite(MRV,LOW);
      digitalWrite(ERH,LOW);
      digitalWrite(MRH,LOW);
    }
    if (realPosLV-250 <= threshold_tile_minus) {
      
      digitalWrite(ELV, LOW);
      digitalWrite(MLV, LOW);
      digitalWrite(ELH, LOW);
      digitalWrite(MLH, LOW);
    
    }
    if (realPosRV >= threshold_tile_plus && realPosLV-250 <= threshold_tile_minus) {
      break;
    }
  }
}


void ausrichten(){
  //Links
  digitalWrite(ELV, HIGH);
  digitalWrite(MLV,HIGH);
  digitalWrite(ELH, HIGH);
  digitalWrite(MLH,HIGH);
  //Rechts
  digitalWrite(ERV,HIGH);
  digitalWrite(MRV,HIGH);
  digitalWrite(ERH,HIGH);
  digitalWrite(MRH,HIGH);
  delay(2000);
  digitalWrite(ERV,LOW);
  digitalWrite(MRV,LOW);
  digitalWrite(ERH,LOW);
  digitalWrite(MRH,LOW);
  digitalWrite(ELV, LOW);
  digitalWrite(MLV, LOW);
  digitalWrite(ELH, LOW);
  digitalWrite(MLH, LOW);
  
  EncoderLH.write(0);
  EncoderLV.write(0);
  EncoderRV.write(0);
  EncoderRH.write(0);
  delay(100);
    //Links
  digitalWrite(ELV, HIGH);
  digitalWrite(MLV,LOW);
  digitalWrite(ELH, HIGH);
  digitalWrite(MLH,LOW);
  //Rechts
  digitalWrite(ERV,LOW);
  digitalWrite(MRV,HIGH);
  digitalWrite(ERH,LOW);
  digitalWrite(MRH,HIGH);

  while (true) {
    realPosLH = EncoderLH.read();
    realPosLV = EncoderLV.read();
    realPosRV = EncoderRV.read();
    realPosRH = EncoderRH.read();
    if (realPosRV <= threshold_wall_minus) {
      
      digitalWrite(ERV,LOW);
      digitalWrite(MRV,LOW);
      digitalWrite(ERH,LOW);
      digitalWrite(MRH,LOW);
    }
    if (realPosLV+100 >= threshold_wall_plus) {
      
      digitalWrite(ELV, LOW);
      digitalWrite(MLV, LOW);
      digitalWrite(ELH, LOW);
      digitalWrite(MLH, LOW);
    
    }
    if (realPosRV <= threshold_wall_minus && realPosLV+250 >= threshold_wall_plus) {
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
    //Links
  digitalWrite(ELV, HIGH);
  digitalWrite(MLV,LOW);
  digitalWrite(ELH, HIGH);
  digitalWrite(MLH,LOW);
  //Rechts
  digitalWrite(ERV,LOW);
  digitalWrite(MRV,HIGH);
  digitalWrite(ERH,LOW);
  digitalWrite(MRH,HIGH);

  while (true) {
    realPosLH = EncoderLH.read();
    realPosLV = EncoderLV.read();
    realPosRV = EncoderRV.read();
    realPosRH = EncoderRH.read();
    if (realPosRV <= threshold_tile_minus) {
      
      digitalWrite(ERV,LOW);
      digitalWrite(MRV,LOW);
      digitalWrite(ERH,LOW);
      digitalWrite(MRH,LOW);
    }
    if (realPosLV+250 >= threshold_tile_plus) {
      
      digitalWrite(ELV, LOW);
      digitalWrite(MLV, LOW);
      digitalWrite(ELH, LOW);
      digitalWrite(MLH, LOW);
    
    }
    if (realPosRV <= threshold_tile_minus && realPosLV+250 >= threshold_tile_plus) {
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
    //Links
  digitalWrite(ELV, HIGH);
  digitalWrite(MLV,HIGH);
  digitalWrite(ELH, HIGH);
  digitalWrite(MLH,HIGH);
  //Rechts
  digitalWrite(ERV,LOW);
  digitalWrite(MRV,HIGH);
  digitalWrite(ERH,LOW);
  digitalWrite(MRH,HIGH);

  while (true) {
    realPosLH = EncoderLH.read();
    realPosLV = EncoderLV.read();
    realPosRV = EncoderRV.read();
    realPosRH = EncoderRH.read();
    Serial.println(realPosRV);
    if (realPosRV <= threshold_turn_minus) {
      
      digitalWrite(ERV,LOW);
      digitalWrite(MRV,LOW);
      digitalWrite(ERH,LOW);
      digitalWrite(MRH,LOW);
    }
    if (realPosLV <= threshold_turn_minus) {
      
      digitalWrite(ELV, LOW);
      digitalWrite(MLV, LOW);
      digitalWrite(ELH, LOW);
      digitalWrite(MLH, LOW);
    
    }
    if (realPosRV <= threshold_turn_minus && realPosLV-250 <= threshold_turn_minus) {
      break;
    }
  }
}

void left(){
  EncoderLH.write(0);
  EncoderLV.write(0);
  EncoderRV.write(0);
  EncoderRH.write(0);
  delay(100);
    //Links
  digitalWrite(ELV, HIGH);
  digitalWrite(MLV,LOW);
  digitalWrite(ELH, HIGH);
  digitalWrite(MLH,LOW);
  //Rechts
  digitalWrite(ERV,HIGH);
  digitalWrite(MRV,HIGH);
  digitalWrite(ERH,HIGH);
  digitalWrite(MRH,HIGH);

  while (true) {
    realPosLH = EncoderLH.read();
    realPosLV = EncoderLV.read();
    realPosRV = EncoderRV.read();
    realPosRH = EncoderRH.read();
    if (realPosRV >= threshold_tile_plus) {
      
      digitalWrite(ERV,LOW);
      digitalWrite(MRV,LOW);
      digitalWrite(ERH,LOW);
      digitalWrite(MRH,LOW);
    }
    if (realPosLV+250 >= threshold_tile_plus) {
        
        digitalWrite(ELV, LOW);
        digitalWrite(MLV, LOW);
        digitalWrite(ELH, LOW);
        digitalWrite(MLH, LOW);
      
      }
      if (realPosRV >= threshold_tile_plus  && realPosLV+250 >= threshold_tile_plus) {
        break;
      }
  }
}

void setup() {
  Serial.begin(9600);
  
  mlx_1.begin();
  mlx_2.begin(); 
  mlx_3.begin();

  pinMode(MLH,OUTPUT);
  pinMode(ELH,OUTPUT);
  pinMode(MLV,OUTPUT);
  pinMode(ELV,OUTPUT);
  pinMode(MRV,OUTPUT);
  pinMode(ERV,OUTPUT);
  pinMode(MRH,OUTPUT);
  pinMode(ERH,OUTPUT);
  
  pinMode(button1, INPUT);
  /*
  Wire.begin();
  Wire.beginTransmission(MPU_ADDR);
  Wire.write(0x6B);
  Wire.write(0);
  Wire.endTransmission();*/

}

void loop() {
}

void serialEvent() {
  while(Serial.available()) {
    message = Serial.readStringUntil('#');
    if (message == "pls") {
      //Daten formatieren
        read_data();
        delay(10);
      Serial.println(String("[ " + String(IRlinkshinten)
      + ", " + String(IRlinksvorne) + ", " + String(IRvorne) + ", " + String(IRrechtshinten) 
      + ", " + String(IRrechtshinten) + ", " + String(grayscale) + ", " + String(touch)
      + ", " + String(temp_vl) + ", 0, " + String(temp_hl) 
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
    else if(message == "ausrichten"){
      ausrichten();
    }
  }
}
