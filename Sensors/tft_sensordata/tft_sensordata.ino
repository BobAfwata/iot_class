#include <Adafruit_GFX.h>     // Core graphics library
#include <Adafruit_ST7735.h>  // Hardware-specific library for ST7735
#include <Adafruit_ST7789.h>  // Hardware-specific library for ST7789
#include <SPI.h>

#include "DHT.h"

#define TFT_CS 9
#define TFT_RST 7
#define TFT_DC 8


#define DHTPIN 2
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

Adafruit_ST7735 tft = Adafruit_ST7735(TFT_CS, TFT_DC, TFT_RST);

const uint16_t Display_Color_Black = 0x0000;
const uint16_t Display_Color_Blue = 0x001F;
const uint16_t Display_Color_Red = 0xF800;
const uint16_t Display_Color_Green = 0x07E0;
const uint16_t Display_Color_Cyan = 0x07FF;
const uint16_t Display_Color_Magenta = 0xF81F;
const uint16_t Display_Color_Yellow = 0xFFE0;
const uint16_t Display_Color_White = 0xFFFF;

uint16_t Display_Text_Color = Display_Color_Black;
uint16_t Display_Backround_Color = Display_Color_White;

bool isDisplayVisible = false;
const size_t data_size = 16;
char data[data_size] = { 0 };

void display_data(char* data) {
  tft.setCursor(0, 0);
  tft.setTextColor(Display_Backround_Color);
  tft.print("Hello");
}

void setup() {

  tft.initR(INITR_BLACKTAB);  // Init ST7735S chip, black tab
  tft.setRotation(1);


  // initialise the display
  tft.setFont();
  tft.fillScreen(Display_Backround_Color);
  tft.setTextColor(Display_Text_Color);
  tft.setTextSize(2);
  isDisplayVisible = true;

  dht.begin();
  drawGraph();
}

void loop() {
  delay(2000);
  float h = dht.readHumidity();
  // Read temperature as Celsius
  float t = dht.readTemperature();
  // Read temperature as Fahrenheit
  float f = dht.readTemperature(true);

  // tft.fillScreen(Display_Backround_Color);
  // tft.setCursor(0, 0);
  // tft.print("Hum:");
  // tft.print(h);
  // tft.print("\n");
  // //tft.print(" %\t");
  // tft.print("Temp:");
  // tft.print(t);
  // tft.print("*C ");


  // delay(100);
}

void drawGraph() {
  // Define the graph parameters
  int graphWidth = 128;
  int graphHeight = 160;
  int graphX = 0;
  int graphY = 0;

  // Draw the X and Y axes
  tft.drawLine(graphX, graphY, graphX, graphY + graphHeight, ST7735_WHITE);                             // Y axis
  tft.drawLine(graphX, graphY + graphHeight, graphX + graphWidth, graphY + graphHeight, ST7735_WHITE);  // X axis

  // Sample data points (for example purposes)
  int dataPoints[] = { 10, 20, 15, 30, 25, 35, 45, 40, 50, 60 };
  int numPoints = sizeof(dataPoints) / sizeof(dataPoints[0]);

  // Calculate the scaling factors
  float xScale = (float)graphWidth / (numPoints - 1);
  float yScale = (float)graphHeight / 60.0;  // Assuming the max value is 60

  // Draw the graph
  for (int i = 0; i < numPoints - 1; i++) {
    int x0 = graphX + (int)(i * xScale);
    int y0 = graphY + graphHeight - (int)(dataPoints[i] * yScale);
    int x1 = graphX + (int)((i + 1) * xScale);
    int y1 = graphY + graphHeight - (int)(dataPoints[i + 1] * yScale);

    tft.drawLine(x0, y0, x1, y1, ST7735_RED);  // Plot the line between points
  }
}