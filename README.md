# The Dragon Cache
An interactive story-driven puzzle Geocache.

## Arduino Sketch
This code runs on the ESP32 directly. It provides a web server and various other functions for features such as opening the lock and submitting Geocaching logs.

## RenPy Source Code
This code is meant to be used with the RenPy SDK and contains the game users will interact with when connecting to the ESP32's hotspot. It interfaces with the API end-points defined in the Arduino Sketch.

## Setting up the SD Card
An SD card needs to be setup approprietly. To this extent, the following operations must be performed.

1. Export the RenPy game to the web platform.
2. Load the files onto the SD card for the web server to serve. Make sure `index.html` is at the root of the SD card.

## Credits
- Component selection, programming and writing by Bluefire.
- Assembly and PCB by Filip.
- `Teleportation loop.wav` by zagi2 (https://freesound.org/s/188168/), licensed under CC Attribution NonCommercial 4.0.
