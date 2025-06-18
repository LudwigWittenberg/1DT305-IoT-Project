# boot.py -- run on boot-up
from services.ConnectWifi import ConnectWifi
from config.WifiConfig import WIFI_ENABLE

if WIFI_ENABLE:
  wifi = ConnectWifi()
  wifi.connect()