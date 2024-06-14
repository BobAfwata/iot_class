#include <WiFi.h>
#include <HTTPClient.h>
#include <Arduino_JSON.h>
#include <SPI.h>
#include "Ucglib.h"

const int button = 35;
Ucglib_ST7735_18x128x160_HWSPI ucg(/*cd=*/16, /*cs=*/5, /*reset=*/17);

const char* ssid = "";
const char* password = "";
String openWeatherMapApiKey = "";
String city;
String countryCode = "KE";

unsigned long lastTime = 0;
unsigned long timerDelay = 10000;  // 10 seconds for testing

String jsonBuffer;
int buttonState = 0;
int lastButtonState = 0;
unsigned long lastDebounceTime = 0;
unsigned long debounceDelay = 50;

void setup() {
  pinMode(button, INPUT);
  ucg.begin(UCG_FONT_MODE_TRANSPARENT);
  ucg.clearScreen();

  ucg.setFont(ucg_font_ncenR12_tr);
  ucg.setColor(255, 255, 255);
  ucg.setPrintPos(10, 40);
  ucg.print("Connecting ...");
  ucg.setPrintPos(10, 60);
  ucg.print(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }

  ucg.clearScreen();
  ucg.setPrintPos(10, 40);
  ucg.print("Connected to:");
  ucg.setPrintPos(10, 60);
  ucg.print(ssid);
  ucg.setPrintPos(10, 80);
  ucg.print("IP: ");
  ucg.print(WiFi.localIP());

  delay(2000);  // Short delay before displaying weather information
}

int i = 0;

void loop() {
  int reading = digitalRead(button);

  if (reading != lastButtonState) {
    lastDebounceTime = millis();
  }

  if ((millis() - lastDebounceTime) > debounceDelay) {
    if (reading != buttonState) {
      buttonState = reading;
      if (buttonState == HIGH) {
        i++;
        if (i > 6) i = 1;
        updateDisplayForCity(i);
      }
    }
  }

  lastButtonState = reading;

  if ((millis() - lastTime) > timerDelay) {
    if (WiFi.status() == WL_CONNECTED) {
      updateDisplayForCity(i);
    }
    lastTime = millis();
  }
}

void updateDisplayForCity(int cityIndex) {
  switch (cityIndex) {
    case 1: city = "Nairobi"; break;
    case 2: city = "Mombasa"; break;
    case 3: city = "Kisumu"; break;
    case 4: city = "Eldoret"; break;
    case 5: city = "Nakuru"; break;
    case 6: city = "Nyeri"; break;
    default: city = "Nairobi"; break;
  }

  if (WiFi.status() == WL_CONNECTED) {
    String serverPath = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "," + countryCode + "&APPID=" + openWeatherMapApiKey;
    jsonBuffer = httpGETRequest(serverPath.c_str());
    JSONVar myObject = JSON.parse(jsonBuffer);

    if (JSON.typeof(myObject) == "undefined") {
      return;
    }

    //float temperatureK = myObject["main"]["temp"];
    //float temperatureC = temperatureK - 273.15;

    ucg.clearScreen();
    ucg.setFont(ucg_font_ncenR12_tr);
    ucg.setColor(255, 255, 255);
    ucg.setColor(1, 255, 0, 0);

    ucg.setPrintPos(25, 25);
    ucg.print(city);
    ucg.setPrintPos(10, 55);
    ucg.setColor(255, 255, 0);
    ucg.print("Temp : ");
    ucg.print(myObject["main"]["temp"]);
    ucg.print(" C");

    ucg.setPrintPos(10, 75);
    ucg.setColor(255, 255, 0);
    ucg.print("Pre : ");
    ucg.print(myObject["main"]["pressure"]);

    ucg.setPrintPos(10, 95);
    ucg.setColor(255, 255, 0);
    ucg.print("Hum : ");
    ucg.print(myObject["main"]["humidity"]);

    ucg.setPrintPos(10, 115);
    ucg.setColor(255, 255, 0);
    ucg.print("Wind : ");
    ucg.print(myObject["wind"]["speed"]);
  }
}

String httpGETRequest(const char* serverName) {
  WiFiClient client;
  HTTPClient http;
  http.begin(client, serverName);

  int httpResponseCode = http.GET();
  String payload = "{}";

  if (httpResponseCode > 0) {
    payload = http.getString();
  }

  http.end();
  return payload;
}
