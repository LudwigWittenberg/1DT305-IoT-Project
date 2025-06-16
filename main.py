from time import sleep_ms, sleep

# ------------ IMPORTS -----------
from lib.PicoLed import PicoLed
from services.TemperatureService import TemperatureService
from lib.IrReciver import IrReciver
from adapter.JsonIRStorage  import JsonIRStorage
from config.DeviceConfig import DeviceConfig
from lib.System import System
from lib.Led import Led
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
yellowLed = Led(yellowLedPin)
greenLed = Led(greenLedPin)
redLed = Led(redLedPin)
ir = IrReciver(IrReciverPin, yellowLed)
irCodes = JsonIRStorage()
device = DeviceConfig(ir, yellowLed, greenLed)
temperatureService = TemperatureService(dhtSensorPin, greenLed, redLed, MAX_TEMP)
system = System(yellowLed, greenLed, redLed)
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
  irCode = ir.get_last_code()
  
  # Check if we have an ir code and if check what action it should do.
  if irCode:
    print(irCode)
    system.set_system_status(irCode)
      
  
  if system.get_system_status():
    picoLed.blink()
  
    temperatureService.check_temp()
    
  elif not system.get_system_status():
    pass

  # stop infinit loop
  sleep_ms(500)
  