import network
from time import sleep
from lib.PicoLed import PicoLed

# ------- WIFI_CREDENTIALS -------
from config.WifiConfig import *
# --------------------------------

# Module for connecting to Wifi
class ConnectWifi:
  def __init__(self):
    self.picoLed = PicoLed()
  
  def connect(self):
    wlan = network.WLAN(network.STA_IF)  
    # Put modem on Station mode
    if not wlan.isconnected():                  # Check if already connected
      print('connecting to network...')
      wlan.active(True)                       # Activate network interface
      # set power mode to get WiFi power-saving off (if needed)
      wlan.config(pm = 0xa11140)
      wlan.connect(WIFI_SSID, WIFI_PASS)  # Your WiFi Credential
      print('Waiting for connection...', end='')
      # Check if it is connected otherwise wait
      while not wlan.isconnected() and wlan.status() >= 0:
        print('.', end='')
        sleep(1)
    # Print the IP assigned by router
    ip = wlan.ifconfig()[0]
    print('\nConnected on {}'.format(ip))
    self.togglePicoLed()
    return ip
  
  def togglePicoLed(self):
    for i in range(5):
      self.picoLed.blink()