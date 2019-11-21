String message;
String status_now = "idle";

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (status_now == "idle") {
    if (Serial.available()){
      message = Serial.readStringUntil('#');
      if (message == "start") {
        status_now = "running";
      }
    }
  }

  if (status_now == "running") {
    if (Serial.available()) {
      message = Serial.readStringUntil('#');
      if (message == "pls") {
        //Hier halt sonst Daten messen
        Serial.write("ey, yo habs gelesen#");
        message = "";
      }
      if (message == "fahren") {
        //Fahren
        Serial.write("angekommen#");
      }
    }
  }
}
