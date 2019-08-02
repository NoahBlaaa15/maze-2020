#define l digitalRead(i)
#define r digitalRead(j)

long a = 0;
long b = 0;
short i = 8;
short j = 9;

int e = 4;
int m = 5;

bool x = false;
bool y = false;

int v = l*1 + r*2;

void setup() {
  pinMode(i, INPUT);
  pinMode(j, INPUT);
  Serial.begin(115200);
  Serial.println("Hallo");
  pinMode(e, OUTPUT);
  pinMode(m, OUTPUT);
  
}
/*
void loop() {
  if(digitalRead(i) == 1 && x == false){
      a++;
      Serial.println(a);
      while(digitalRead(i) == 1){}
    }
}*/

void loop() {

  while(a < 2100){
  analogWrite(e, 255);
  digitalWrite(m, HIGH);
  
  if(l*1+r*2 != v){
      v = l*1+r*2;
      //Serial.println(l*1+r*2);
      while(l*1+r*2 == v){}
    }

  if(v == 0 && l*1+r*2 == 1){
      a--;
      Serial.println(a);
      v = l*1+r*2;
    }
  if(v == 0 && l*1+r*2 == 2){
      a++;
      Serial.println(a);
      v = l*1+r*2;
    }
  if(v == 1 && l*1+r*2 == 0){
      a++;
      Serial.println(a);
      v = l*1+r*2;
    }
  if(v == 1 && l*1+r*2 == 3){
      a--;
      Serial.println(a);
      v = l*1+r*2;
    }
  if(v == 2 && l*1+r*2 == 0){
      a--;
      Serial.println(a);
      v = l*1+r*2;
    }
  if(v == 2 && l*1+r*2 == 3){
      a++;
      Serial.println(a);
      v = l*1+r*2;
    }
  if(v == 3 && l*1+r*2 == 1){
      a++;
      Serial.println(a);
      v = l*1+r*2;
    }
  if(v == 3 && l*1+r*2 == 2){
      a--;
      Serial.println(a);
      v = l*1+r*2;
    }

  }
  analogWrite(e, 0);
  digitalWrite(m, HIGH);
  Serial.println("Bin da Brudi!");
  delay(2000);
  while(a > 0){
  analogWrite(e, 100);
  digitalWrite(m, LOW);
   if(l*1+r*2 != v){
      v = l*1+r*2;
      //Serial.println(l*1+r*2);
      while(l*1+r*2 == v){}
    }

  if(v == 0 && l*1+r*2 == 1){
      a--;
      Serial.println(a);
      v = l*1+r*2;
    }
  if(v == 0 && l*1+r*2 == 2){
      a++;
      Serial.println(a);
      v = l*1+r*2;
    }
  if(v == 1 && l*1+r*2 == 0){
      a++;
      Serial.println(a);
      v = l*1+r*2;
    }
  if(v == 1 && l*1+r*2 == 3){
      a--;
      Serial.println(a);
      v = l*1+r*2;
    }
  if(v == 2 && l*1+r*2 == 0){
      a--;
      Serial.println(a);
      v = l*1+r*2;
    }
  if(v == 2 && l*1+r*2 == 3){
      a++;
      Serial.println(a);
      v = l*1+r*2;
    }
  if(v == 3 && l*1+r*2 == 1){
      a++;
      Serial.println(a);
      v = l*1+r*2;
    }
  if(v == 3 && l*1+r*2 == 2){
      a--;
      Serial.println(a);
      v = l*1+r*2;
    }
  }
  analogWrite(e, 0);
  digitalWrite(m, HIGH);
  Serial.println("Bin da Brudi!");
  delay(2000);
}