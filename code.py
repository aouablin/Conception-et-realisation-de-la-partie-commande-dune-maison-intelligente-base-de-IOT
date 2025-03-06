#include  "thingProperties.h"
// DHT sensor library - Version: Latest
#include  <DHT.h>
#include  <DHT_U.h>
// Configuration du capteur DHT22
const int DHTPIN = 12;             // Broche de donnees du capteur DHT22
#define DHTTYPE DHT22      // Type de capteur DHT (DHT 11 ou DHT22) 
 DHT dht(DHTPIN, DHTTYPE);
// Configuration du relais
const int relayPin = 14;               // Broche de donnees du capteur Relais
void setup() {
   Serial.begin(9600); // Initialize serial and wait for port to open:
  pinMode(relayPin, OUTPUT);   // Initialisation du relais donc configuration de la broche du relais en sortie
  dht.begin();
  // Defined in thingProperties.h
  initProperties();
 // Connect to Arduino IoT Cloud
  ArduinoCloud.begin(ArduinoIoTPreferredConnection);
  setDebugMessageLevel(2);
  ArduinoCloud.printDebugInfo();
}
void loop() {
  ArduinoCloud.update();
  DHT_SENSOR_READ();
  onAutoChangeChange();
}
void onRelaySwitchChange()  {
  if (relay_switch) {
    digitalWrite(relayPin, LOW);    // eteindre le relais 
  } else {
     digitalWrite(relayPin, HIGH);     // allumer le relais 
  }
}
void  DHT_SENSOR_READ() {
  float hum = dht.readHumidity();
  float temp = dht.readTemperature();
 if (isnan(hum) || isnan(temp)  ) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }
  humidity = hum;
  temperature = temp;
  Serial.print("Temperature: ");
  Serial.print(temp);
  Serial.print("C");
 Serial.print(" Humidity: ");
 Serial.print(hum);
  Serial.print("%");
Serial.println();
  delay(1000);
}
void onAutoChangeChange()  {
  if (autoChange) {
   if (temperature >= 30 || humidity >= 70) {
       digitalWrite(relayPin, LOW);   // eteindre le relais 
    } else {
       digitalWrite(relayPin, HIGH);   // allumer le relais 
    }
  } else {
    onRelaySwitchChange();
  }
