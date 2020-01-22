#include <Wire.h>

const int IRV = A0;
const int IRRV = A0;
const int IRRH = A0;
const int IRLV = A0;
const int IRLH = A0;

int IRvV = 0;
int IRvRV = 0;
int IRvRH = 0;
int IRvLV = 0;
int IRvLH = 0;

const int MINI_ADDR = 0x1F;

void setup() {
  Wire.begin(MINI_ADDR);
  Serial.begin(4800);
  Serial.println("Ready! :1");
  Wire.onReceive(receiveEvent);
  Wire.onRequest(requestEvent);
}

void loop() {
  float lh = analogRead(IRLH)*0.0048828125;
  IRvLH = 13*pow(lh, -1);
  float lv = analogRead(IRLV)*0.0048828125;
  IRvLV = 13*pow(lv, -1);
  float v = analogRead(IRV)*0.0048828125;
  IRvV = 13*pow(v, -1);
  float rv = analogRead(IRRV)*0.0048828125;
  IRvRV = 13*pow(rv, -1);
  float rh = analogRead(IRRH)*0.0048828125;
  IRvRH = 13*pow(rh, -1);
  delay(10);
}

void receiveEvent( int bytes ){
  while(Wire.available()){
    byte rw = Wire.read();
    if(rw == 9){
    Serial.println(rw);
    //Rettungskit starten
    }
  }
}
void requestEvent(void ){
  Wire.write((byte) IRvV);
  Wire.write((byte) IRvLV);
  Wire.write((byte) IRvLH);
  Wire.write((byte) IRvRV);
  Wire.write((byte) IRvRH);
  Serial.println("Sending");
}
