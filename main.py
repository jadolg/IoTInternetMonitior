import gc
import time
import network
import urequests
from machine import Pin

pin = machine.Pin(2, machine.Pin.OUT)
pin.on()

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

while True:
    try:
        wlan.connect("user", "password")
        response = urequests.get("http://clients3.google.com/generate_204")
        print(response.status_code)
        if response.status_code == 204:
            print("online")
            pin.off()
        elif response.status_code == 200:
            print("portal")
            pin.off()
            time.sleep(1)
            pin.on()
        else:
            print("offline")
            pin.on()
    except:
        print("error")
        pin.on()
    gc.collect()

    time.sleep(10)
