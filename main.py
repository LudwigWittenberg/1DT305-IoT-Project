from time import sleep_ms, sleep

# ------------ IMPORTS -----------
from lib.PicoLed import PicoLed
from services.TemperatureService import TemperatureService
from lib.IrReciver import IrReciver
from adapter.JsonIRStorage  import JsonIRStorage
from config.DeviceConfig import DeviceConfig
# --------------------------------

# ------------- PINS -------------
dhtSensorPin = 16
yellowLedPin = 13
greenLedPin = 15
redLedPin = 14
IrReciverPin = 19
# --------------------------------

# ----------- MAX_TEMP -----------
MAX_TEMP = 25
# --------------------------------

# ------------- INIT -------------
picoLed = PicoLed()
ir = IrReciver(IrReciverPin)
irCodes = JsonIRStorage()
device = DeviceConfig(ir, yellowLedPin, greenLedPin)
# --------------------------------

# ------------- START -------------
# First we need to set up a config for the device
if not device.is_configured():
  print('--------- Setup Started ---------')
  device.start_setup_process()
  print('-------- Setup Completed --------')
  # Make sure the config is in place
  sleep(2)


# -------------- TESTING ------------------------
# Can be removed

temperatureService = TemperatureService(dhtSensorPin, greenLedPin, redLedPin, MAX_TEMP)

while True:
  picoLed.blink()

  temperatureService.check_temp()

  # stop infinit loop
  sleep_ms(500)
