#include <Adafruit_GFX.h>    // Core graphics library
#include <Adafruit_ST7735.h> // Hardware-specific library for ST7735
#include <SPI.h>
#include "DHT.h"

#define TFT_CS   9
#define TFT_RST  7
#define TFT_DC   8
#define DHTPIN   2
#define DHTTYPE  DHT11

DHT dht(DHTPIN, DHTTYPE);
Adafruit_ST7735 tft = Adafruit_ST7735(TFT_CS, TFT_DC, TFT_RST);

const uint16_t Display_Color_Black = 0x0000;
const uint16_t Display_Color_White = 0xFFFF;
const uint16_t Display_Color_Red = 0xF800;

const int graphWidth = 128;
const int graphHeight = 160;
const int graphX = 20; // Adjust to leave space for Y axis labels
const int graphY = 20; // Adjust to leave space for X axis labels
const int maxDataPoints = 20;
int temperatureData[maxDataPoints] = {0};
int dataIndex = 0;

void setup() {
  tft.initR(INITR_BLACKTAB);  // Init ST7735S chip, black tab
  tft.setRotation(0);
  tft.fillScreen(Display_Color_White);
  tft.setTextColor(Display_Color_Black);
  tft.setTextSize(0.5);
  dht.begin();

  // Draw static graph elements
  tft.drawLine(graphX, graphY, graphX, graphY + graphHeight, Display_Color_Black);                             // Y axis
  tft.drawLine(graphX, graphY + graphHeight, graphX + graphWidth, graphY + graphHeight, Display_Color_Black);  // X axis

  // Draw axis labels
  tft.setCursor(0, 0);
  tft.print("Temp(C)");
  tft.setCursor(graphX + graphWidth / 2, graphY + graphHeight + 20);
  tft.print("Time(s)");
}

void loop() {
  delay(5000);

  float t = dht.readTemperature();  // Read temperature as Celsius
  if (isnan(t)) {
    tft.setCursor(0, 0);
    tft.fillScreen(Display_Color_White);
    tft.print("Error reading from DHT sensor");
    return;
  }

  // Update data array
  temperatureData[dataIndex] = (int)t;
  dataIndex = (dataIndex + 1) % maxDataPoints;

  // Clear previous graph
  tft.fillRect(graphX + 1, graphY + 1, graphWidth - 1, graphHeight - 1, Display_Color_White);

  // Redraw static elements
  tft.drawLine(graphX, graphY, graphX, graphY + graphHeight, Display_Color_Black);                             // Y axis
  tft.drawLine(graphX, graphY + graphHeight, graphX + graphWidth, graphY + graphHeight, Display_Color_Black);  // X axis

  // Redraw axis labels
  tft.setCursor(0, 0);
  tft.print("Temp(C)");
  tft.setCursor(graphX + graphWidth / 2, graphY + graphHeight + 10);
  tft.print("Time(s)");

  // Draw new graph
  drawGraph();
}

void drawGraph() {
  float xScale = (float)graphWidth / (maxDataPoints - 1);
  float yScaleTemp = (float)graphHeight / 30.0;  // Assuming the max temperature value is 50 for better scaling

  // Draw temperature graph
  for (int i = 0; i < maxDataPoints - 1; i++) {
    int x0 = graphX + (int)(i * xScale);
    int y0 = graphY + graphHeight - (int)(temperatureData[i] * yScaleTemp);
    int x1 = graphX + (int)((i + 1) * xScale);
    int y1 = graphY + graphHeight - (int)(temperatureData[(i + 1) % maxDataPoints] * yScaleTemp);

    tft.drawLine(x0, y0, x1, y1, Display_Color_Red);  // Plot the temperature line between points
  }

  // Draw Y axis labels for temperature
  for (int i = 0; i <= 30; i += 10) {
    int y = graphY + graphHeight - (int)(i * yScaleTemp);
    tft.setCursor(0, y - 3);
    tft.print(i);
  }

  // Draw X axis labels for time (in seconds)
  for (int i = 0; i < maxDataPoints; i += 5) {
    int x = graphX + (int)(i * xScale);
    tft.setCursor(x - 5, graphY + graphHeight + 2);
    tft.print(i * 5);
  }
}
