#include <LiquidCrystal.h>
#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>
#include <ArduinoJson.h>


// DHT Sensor information
#define DHTPIN 6 
#define DHTTYPE    DHT11
DHT_Unified dht(DHTPIN, DHTTYPE);

uint32_t delayMS;

// LCD information
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);


void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  dht.begin();
  lcd.begin(16, 2);
  // lcd.setCursor(4, 0);
  // lcd.print(" - Dim");

  sensor_t sensor;
  dht.temperature().getSensor(&sensor);
  dht.humidity().getSensor(&sensor);
  delayMS = sensor.min_delay / 1000;
}

void loop() {
  delay(500);
  sensors_event_t event;
  dht.temperature().getEvent(&event);
  DynamicJsonDocument jsonDoc(200);

  if (isnan(event.temperature)) {
    Serial.println(F("Error reading temperature!"));
  }
  else {
    
    lcd.clear();
    lcd.setCursor(4, 0);
    lcd.print(event.temperature);
    //lcd.print("   C");
    lcd.print( " \xDF" "C");
    jsonDoc["temperature"] = event.temperature;

    
  }
  // Get humidity event and print its value.
  dht.humidity().getEvent(&event);
  if (isnan(event.relative_humidity)) {
    Serial.println(F("Error reading humidity!"));
  }
  else {
    //Serial.print(F("Humidity: "));
    //Serial.print(event.relative_humidity);
    //Serial.println(F("%"));
    lcd.setCursor(4, 1);
    lcd.print(event.relative_humidity);
    lcd.print(F("%"));
    jsonDoc["humidity"] = event.relative_humidity;

  }
   // send to serial as json



    // Populate the JSON object
    jsonDoc["light"] = analogRead(A0);  // You can adjust the time for the second set
    jsonDoc["sound"] =  analogRead(A1);  // You can adjust the distance for the second set

    // Serialize the JSON object to a string
    String jsonData;
    serializeJson(jsonDoc, jsonData);

    // Send the JSON data over Bluetooth
    Serial.println(jsonData);
  
}
