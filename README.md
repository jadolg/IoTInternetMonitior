# Micropython ESP8266 connectivity checker

## What to expect

When you are online, the integrated LED (PIN2 in the WemOS D1 mini) will be on.
When on captive portal LED will be blinking.
When offline LED will be off.

## Configure

Open the **main.py** file and enter your WiFi credentials there. Maybe you will also want to use an external LED or do some other modifications. That's up to you :)

## How to flash

`ampy -p /dev/ttyUSB3 put main.py`

## Story

My parents have this Cuban internet connection using ADSL but it is too expensive to keep it on all the time and it has a captive portal you have to login to in order to have internet. I just wanted to have an indicator telling me when I can use the WiFi.
