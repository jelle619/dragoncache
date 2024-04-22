#include <Arduino.h>
#include <WiFi.h>
#include <AsyncTCP.h>
#include <ESPAsyncWebServer.h>
#include "FS.h"
#include "SD.h"
#include "SPI.h"
#include "pitches.h"

// Define pins
#define BUZZZER_PIN  21
#define RELAY_PIN 32

// Define variabkes
bool openLockRequested = false;

// Replace with your network credentials
const char* ssid = "The Dragon Cache";
const char* password = "summonthedr@gon";
const int channel = 1;
const int ssid_hidden = 0;
const int max_connection = 1;
IPAddress ip(192,168,1,1);
IPAddress gateway(192,168,1,1);
IPAddress subnet(255,255,255,0);

// Create AsyncWebServer object on port 80
AsyncWebServer server(80);

void playSound() {
    // https://esp32io.com/tutorials/esp32-piezo-buzzer

    int melody[] = {
      // NOTE_C4, NOTE_G3, NOTE_G3, NOTE_A3, NOTE_G3, 0, NOTE_B3, NOTE_C4
      NOTE_D4, NOTE_G3, NOTE_A3, NOTE_B3, NOTE_C4, 0, NOTE_E4, 0, NOTE_B4, 0, NOTE_G4
    };

    int noteDurations[] = {
      4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4
    };

    for (int thisNote = 0; thisNote < 11; thisNote++) {
      int noteDuration = 1000 / noteDurations[thisNote];
      tone(BUZZZER_PIN, melody[thisNote], noteDuration);
      int pauseBetweenNotes = noteDuration * 1.30;
      delay(pauseBetweenNotes);
      noTone(BUZZZER_PIN);
  }
}

void initSDCard() {
  int attempts = 0;
  while (!SD.begin() && attempts < 5) { // Retry for a maximum of 5 attempts
    Serial.println("Mounting SD card failed. Retrying...");
    delay(2000); // Wait for 2 seconds before retrying
    attempts++;
  }

  if (attempts == 5) {
    Serial.println("Failed to mount SD card after multiple attempts.");
    return;
  }

  uint8_t cardType = SD.cardType();

  if(cardType == CARD_NONE){
    Serial.println("No SD card attached.");
    return;
  }

  Serial.print("SD card type: ");
  if(cardType == CARD_MMC){
    Serial.println("MMC");
  } else if(cardType == CARD_SD){
    Serial.println("SDSC");
  } else if(cardType == CARD_SDHC){
    Serial.println("SDHC");
  } else {
    Serial.println("UNKNOWN");
  }
  uint64_t cardSize = SD.cardSize() / (1024 * 1024);
  Serial.printf("SD card size: %lluMB\n", cardSize);
}

void submitLog() {

}

void openLock() {
  Serial.println("Starting lock cycle...");
  Serial.println("Entering power saving mode...");
  // WiFi.setSleep(true);
  setCpuFrequencyMhz(40);
  delay(250);
  Serial.println("Opening lock...");
  digitalWrite(RELAY_PIN, HIGH); // unlock the door
  delay(5000);
  Serial.println("Closing lock...");
  digitalWrite(RELAY_PIN, LOW);  // lock the door
  Serial.println("Exiting power saving mode...");
  // WiFi.setSleep(false);
  // setCpuFrequencyMhz(240);
  Serial.println("Cooling lock down...");
  delay(4750);
  Serial.println("Lock cycle complete, now open to new lock cycles.");
}

void initWiFi() {
  WiFi.mode(WIFI_AP);
  WiFi.softAPConfig(ip, gateway, subnet);
  WiFi.softAP(ssid, password, channel, ssid_hidden, max_connection);

  Serial.print("Access point created: ");
  Serial.println(WiFi.softAPIP());
}

void setup() {
  Serial.begin(115200);
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, LOW);  // ensure lock is closed

  Serial.print("Status of ASyncTCP watchdog: ");
  if (CONFIG_ASYNC_TCP_USE_WDT == 1) {
    Serial.println("Enabled");
  } else {
    Serial.println("Disabled");
  }

  initWiFi();
  initSDCard();
  playSound();

  // Route for lock endpoint
  server.on("/open", HTTP_POST, [](AsyncWebServerRequest *request){
    Serial.println("Request to open lock received");
    openLockRequested = true;
    request->send(200); // Respond with HTTP 200 OK
  });

  // Route for submission endpoint
  server.on("/submit", HTTP_POST, [](AsyncWebServerRequest *request){
    request->send(200); // Respond with HTTP 200 OK
    if (request->hasParam("name") && request->hasParam("date") && request->hasParam("time")) {
      String name = request->getParam("name")->value();
      String date = request->getParam("date")->value();
      String time = request->getParam("time")->value();

      // Write to file on SD card
      File file = SD.open("/log.txt", FILE_APPEND);
      if (file) {
        file.println(name + "," + date + "," + time);
        file.close();
        Serial.println("Log submitted: " + name + "," + date + "," + time);
      } else {
        Serial.println("Error opening log file");
      }
    } else {
      Serial.println("Incomplete parameters in request");
    }
  });

  // Route to serve files from SD card
  server.onNotFound([](AsyncWebServerRequest *request) {
    if (request->method() == HTTP_GET) {
      String path = request->url();
      if (path.endsWith("/")) {
        path += "index.html"; // Serve index.html if the URL ends with a "/"
      }

      if (SD.exists(path)) {
        request->send(SD, path, getContentType(path));
      } else {
        request->send(404, "text/plain", "File Not Found");
      }
    } else {
      request->send(405, "text/plain", "Method Not Allowed");
    }
  });

  server.begin();
}

void loop() {
    // Open lock request
    if (openLockRequested) {

        openLock(); // Open the lock
        openLockRequested = false; // Reset the flag
    }
}

String getContentType(String filename) {
  if (filename.endsWith(".html")) return "text/html";
  else if (filename.endsWith(".css")) return "text/css";
  else if (filename.endsWith(".js")) return "application/javascript";
  else if (filename.endsWith(".png")) return "image/png";
  else if (filename.endsWith(".jpg") || filename.endsWith(".jpeg")) return "image/jpeg";
  else if (filename.endsWith(".gif")) return "image/gif";
  else if (filename.endsWith(".ico")) return "image/x-icon";
  else if (filename.endsWith(".xml")) return "text/xml";
  else if (filename.endsWith(".pdf")) return "application/x-pdf";
  else if (filename.endsWith(".zip")) return "application/x-zip";
  else if (filename.endsWith(".gz")) return "application/x-gzip";
  else if (filename.endsWith(".wasm")) return "application/wasm";
  return "text/plain";
}