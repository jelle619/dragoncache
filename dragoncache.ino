// Import libraries
#include <WiFi.h>
#include <WebServer.h>
#include <SD.h>
#include <ElegantOTA.h>
#include <SimpleFTPServer.h> // change FtpServerKey.h accordingly
#include "pitches.h"

// Set login info for adiminstrator
const char* admin_username = "admin";
const char* admin_password = "Pq3HwCf$yh!LgC";

// Define pins
#define BUZZER_PIN  21
#define RELAY_PIN 32

// Define variabkes
bool openLockRequested = false;

// Network credentials
const char* ssid = "The Dragon Cache";
const char* password = "summonthedr@gon";
const int channel = 1;
const int ssid_hidden = 0;
const int max_connection = 1;
IPAddress ip(192,168,1,1);
IPAddress gateway(192,168,1,1);
IPAddress subnet(255,255,255,0);
  
// Web server
WebServer server(80);

// FTP server
FtpServer ftpSrv;

void initWiFi() {
  WiFi.mode(WIFI_AP);
  WiFi.softAPConfig(ip, gateway, subnet);
  WiFi.softAP(ssid, password, channel, ssid_hidden, max_connection);

  Serial.print("Access point created: ");
  Serial.println(WiFi.softAPIP());
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

void openLock() {
  Serial.println("Starting lock cycle...");
  Serial.println("Opening lock...");
  digitalWrite(RELAY_PIN, HIGH); // unlock the door
  delay(10000);
  Serial.println("Closing lock...");
  digitalWrite(RELAY_PIN, LOW);  // lock the door
  Serial.println("Cooling lock down...");
  delay(10000);
  Serial.println("Lock cycle complete, now open to new lock cycles.");
}

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
      tone(BUZZER_PIN, melody[thisNote], noteDuration);
      int pauseBetweenNotes = noteDuration * 1.30;
      delay(pauseBetweenNotes);
      noTone(BUZZER_PIN);
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
  
void setup() {
  // Open serial connection
  Serial.begin(115200);

  // 
  pinMode(RELAY_PIN, OUTPUT);

  // Check lock state
  if (digitalRead(RELAY_PIN) == HIGH) {
    Serial.println("Lock is open, preparing to close lock...");
    Serial.println("Delaying start up...");
    delay(10000);
    Serial.println("Closing lock...");
    digitalWrite(RELAY_PIN, LOW);  // lock the door
    Serial.println("Lock has been closed, continuing start up...");
  }
  
  // Run intialization routines
  initWiFi();
  initSDCard();

  // Route for lock endpoint
  server.on("/open", HTTP_POST, [](){
    Serial.println("Request to open lock received");
    openLockRequested = true;
    server.send(200); // Respond with HTTP 200 OK    
  });

  // Route for serving files from SD card
  server.onNotFound([](){
    String path = server.uri();
    if (path.endsWith("/")) {
      path += "index.html"; // If no file specified, serve index.html
    }

    File file = SD.open(path); // Open the file
    if (!file) {
      server.send(404, "text/plain", "File not found");
      return;
    }
    
    server.streamFile(file, getContentType(path));
  });

  // ElegantOTA configuration
  ElegantOTA.setAuth(admin_username, admin_password); // set authentication
  ElegantOTA.setAutoReboot(true); // set auto reboot

  // Start web server
  ElegantOTA.begin(&server);
  server.begin();

  // Start FTP server
  ftpSrv.begin(admin_username, admin_password);

  // Play sound
  playSound();
}
  
void loop() {  
    ElegantOTA.loop(); // allows for reboot after firmware flash
    server.handleClient(); // handle web server requests
    ftpSrv.handleFTP(); // handle FTP server requests
    if (openLockRequested) { // hande open lock requests
        openLock(); // Open the lock
        openLockRequested = false; // Reset the flag
    }
}