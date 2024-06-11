#include <WiFi.h>
#include <HTTPClient.h>
#include <Arduino_JSON.h>

#include <SPI.h>
#include "Ucglib.h"

const int button = 1;
bool button_status = false;

Ucglib_ST7735_18x128x160_HWSPI ucg(/*cd=*/ 16, /*cs=*/ 5, /*reset=*/ 17);

const char* ssid = "xxxyyy";
const char* password = "xxrrrx";

// Your Domain name with URL path or IP address with path
String openWeatherMapApiKey = "";
// Example:
//String openWeatherMapApiKey = "bd939aa3d23ff33d3c8f5dd1dd435";

// Replace with your country code and city
String city = "Nairobi";
String cities[5] = {"Nairobi", "Kisumu", "Mombasa", "Eldoret", "Nyeri"};
String countryCode = "KE";

// THE DEFAULT TIMER IS SET TO 10 SECONDS FOR TESTING PURPOSES
// For a final application, check the API call limits per hour/minute to avoid getting blocked/banned
unsigned long lastTime = 0;
// Timer set to 10 minutes (600000)
//unsigned long timerDelay = 600000;
// Set timer to 10 seconds (10000)
unsigned long timerDelay = 10000;

String jsonBuffer;

bool isDisplayVisible = false;
const size_t data_size = 16;
char data[data_size] = { 0 };
void setup() {
  pinMode(button , INPUT);
  delay(1000);
  ucg.begin(UCG_FONT_MODE_TRANSPARENT);
  ucg.clearScreen();


  Serial.begin(115200);

  WiFi.begin(ssid, password);
  Serial.println("Connecting");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to WiFi network with IP Address: ");
  Serial.println(WiFi.localIP());

  Serial.println("Timer set to 10 seconds (timerDelay variable), it will take 10 seconds before publishing the first reading.");
}

void loop() {
  // Send an HTTP GET request
  int i = 0;
  button_status = digitalRead(button);
  if (button_status == true) {
    for (i++;)
    {


      if (WiFi.status() == WL_CONNECTED) {
        String serverPath = "http://api.openweathermap.org/data/2.5/weather?q=" + cities[i] + "," + countryCode + "&APPID=" + openWeatherMapApiKey;

        jsonBuffer = httpGETRequest(serverPath.c_str());
        // Serial.println(jsonBuffer);
        JSONVar myObject = JSON.parse(jsonBuffer);

        // JSON.typeof(jsonVar) can be used to get the type of the var
        if (JSON.typeof(myObject) == "undefined") {
          Serial.println("Parsing input failed!");
          return;
        }
        Serial.println("----------------------------------");
        Serial.println(cities[i]);
        Serial.print("Temperature: ");
        Serial.println(myObject["main"]["temp"]);
        Serial.print("Pressure: ");
        Serial.println(myObject["main"]["pressure"]);
        Serial.print("Humidity: ");
        Serial.println(myObject["main"]["humidity"]);
        Serial.print("Wind Speed: ");
        Serial.println(myObject["wind"]["speed"]);
        Serial.println("----------------------------------");

        ucg.clearScreen();
        ucg.setFont(ucg_font_ncenR12_tr);
        ucg.setColor(255, 255, 255);

        ucg.setColor(1, 255, 0, 0);

        ucg.setPrintPos(25, 25);
        ucg.print(cities[i]);
        ucg.setPrintPos(10, 55);
        ucg.setColor(255, 255, 0);
        ucg.print("Temp : ");
        ucg.print(myObject["main"]["temp"]);

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


      else {
        Serial.println("WiFi Disconnected");
      }
    }
//    lastTime = millis();
  }
}

String httpGETRequest(const char* serverName) {
  WiFiClient client;
  HTTPClient http;

  // Your Domain name with URL path or IP address with path
  http.begin(client, serverName);

  // Send HTTP POST request
  int httpResponseCode = http.GET();

  String payload = "{}";

  if (httpResponseCode > 0) {
    Serial.print("HTTP Response code: ");
    Serial.println(httpResponseCode);
    payload = http.getString();
  }
  else {
    Serial.print("Error code: ");
    Serial.println(httpResponseCode);
  }
  // Free resources
  http.end();

  return payload;
}
