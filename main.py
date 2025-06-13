from time import sleep_ms, sleep

# ------------ IMPORTS -----------
from lib.PicoLed import PicoLed
from lib.DHTSensor import DHTSensor
from lib.Led import Led
from services.TemperatureService import TemperatureService
from lib.IrReciver import IrReciver
from adapter.JsonIRStorage  import JsonIRStorage
from config.configured import Config
# --------------------------------

# ------------- PINS -------------
dhtSensorPin = 16
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
csv = JsonIRStorage()
config = Config(ir)
# --------------------------------

# ------------- START -------------
# First we need to set up a config for the device
if not config.is_configured():
  # TODO: SETUP CONFIG SCRIPT
  config.start_setup_process()
  print('JAAAAAAAAAAAA')
  # Make sure the config is in place
  sleep(2)


# -------------- TESTING ------------------------
# Can be removed
sleep_ms(1000)

print('started')

temperatureService = TemperatureService(dhtSensorPin, greenLedPin, redLedPin, MAX_TEMP)

# Can be removed
# csv.add_code('offfffaaaadawdawdwadawd', 1119)
# csv.save()
codes = csv.get_all_codes()

print('All Codes')
print(codes)

for c in codes:
  print(c.get_code())


while True:
  picoLed.blink()

  temperatureService.check_temp()

#   stop infinit loop
  sleep_ms(500)
  

# from machine import Pin
# import time

# ir_receiver = Pin(19, Pin.IN)

# print('Started')

# while True:
#     if ir_receiver.value() == 0:
#         print("IR-signal mottagen!")
#     else:
#         print("Ingen signal")
#     time.sleep(0.1)
