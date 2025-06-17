# boot.py -- run on boot-up
from services.ConnectWifi import ConnectWifi

wifi = ConnectWifi()
wifi.connect()
