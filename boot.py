# boot.py -- run on boot-up
from services.ConnectWifi import ConnectWifi
from services.MQTT import MQTT

wifi = ConnectWifi()
wifi.connect()

mqtt = MQTT()
mqtt.connect()
mqtt.publish()