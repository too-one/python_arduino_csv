//Sends random data to python scrip who will save it into a csv file
int counter = 1;
int dato_recibido = 0;

void setup() {
  Serial.begin(9600);  // Start up Serial Port
  delay(1000);         // Wait for Serial to settle
  Serial.print(u8"Arduino Comunication Ready \U0001f60e!");
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  // Wait for computer to send chara
  // Once character received, start sending data to computer
  if (Serial.available() > 0) {
    dato_recibido = Serial.read();

    if (dato_recibido == 120) {//if letter x is receive it means python is ready to receive
      digitalWrite(LED_BUILTIN, HIGH);
      // Send data to computer via Serial
      Serial.print("Nombre");
        Serial.print(",");
        Serial.print("Edad");
        Serial.print(",");
        Serial.print("Altura");
        Serial.print("!"); //! means last character of message

      for (counter; counter < 6; counter++) { //random data
        Serial.print(counter);
        Serial.print(",");
        Serial.print(counter + 1);
        Serial.print(",");
        Serial.print(counter + 2);
        Serial.print("!");
      }
      
      Serial.print("stop!");
      Serial.flush();//waits until all have been send
    }
  }
}
