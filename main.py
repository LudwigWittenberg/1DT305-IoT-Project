from time import sleep

from lib.PicoLed import PicoLed
from lib.DHTSensor import DHTSensor
from lib.Led import Led
from services.TemperatureService import TemperatureService

# ------------- PINS -------------
dhtSensorPin = 16
greenLedPin = 15
redLedPin = 14
# --------------------------------

picoLed = PicoLed()

maxTemp = 25
temperatureService = TemperatureService(dhtSensorPin, greenLedPin, redLedPin, maxTemp)

while True:
  picoLed.blink()

  temperatureService.check_temp()
  # stop infinit loop
  sleep(2)