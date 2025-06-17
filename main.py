import asyncio
from time import sleep_ms, sleep

# ------------ IMPORTS -----------
from lib.PicoLed import PicoLed
from services.TemperatureService import TemperatureService
from lib.IR.RawIRRecorder import RawIRRecorder
from config.DeviceConfig import DeviceConfig
from lib.System import System
from lib.Led import Led
# --------------------------------

# ------------- PINS -------------
dhtSensorPin = 16
yellowLedPin = 13
greenLedPin = 15
redLedPin = 14
irReciverPin = 19
irTransmitterPin = 20
# --------------------------------

# ----------- MAX_TEMP -----------
MAX_TEMP = 25
# --------------------------------

# ------------- INIT -------------
picoLed = PicoLed()
yellowLed = Led(yellowLedPin)
greenLed = Led(greenLedPin)
redLed = Led(redLedPin)
ir = RawIRRecorder(irReciverPin)
device = DeviceConfig(ir, yellowLed, greenLed)
temperatureService = TemperatureService(dhtSensorPin, greenLed, redLed, MAX_TEMP, irTransmitterPin)
system = System(yellowLed, greenLed, redLed, ir)
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

while True:        
  if system.get_system_status():
    picoLed.blink()
    temperatureService.check_temp()
    
    print('System PÅ')
    
  elif not system.get_system_status():
    print('System AV')

  # stop infinit loop
  sleep_ms(500)
  
  