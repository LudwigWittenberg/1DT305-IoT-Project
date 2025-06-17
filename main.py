from time import sleep_ms, sleep

# ------------ IMPORTS -----------
from lib.PicoLed import PicoLed
from services.TemperatureService import TemperatureService
from lib.IR.RawIRRecorder import RawIRRecorder
from config.DeviceConfig import DeviceConfig
from lib.System import System
from lib.Led import Led
from lib.PIEZO.Piezo import Piezo
# --------------------------------

# ------------- PINS -------------
dhtSensorPin = 16
yellowLedPin = 13
greenLedPin = 15
redLedPin = 14
irReciverPin = 19
irTransmitterPin = 20
photoPin = 28
piezoPin = 27
# --------------------------------

# ----------- MAX_TEMP -----------
MAX_TEMP = 25
# --------------------------------

# ------------- INIT -------------
picoLed = PicoLed()
yellowLed = Led(yellowLedPin)
greenLed = Led(greenLedPin)
redLed = Led(redLedPin)
piezo = Piezo(piezoPin)
ir = RawIRRecorder(irReciverPin)
device = DeviceConfig(ir, yellowLed, greenLed)
temperatureService = TemperatureService(dhtSensorPin, greenLed, redLed, MAX_TEMP, irTransmitterPin, piezo)
system = System(yellowLed, greenLed, redLed, ir, photoPin, piezo)
# --------------------------------

# ------------- SETUP -------------
# First we need to set up a config for the device
if not device.is_configured():
  print('--------- Setup Started ---------')
  device.start_setup_process()
  print('-------- Setup Completed --------')
  # Make sure the config is in place
  sleep(2)

# ------------- START -------------
def run():
  while True:
    system.check_system_status()
    if system.get_system_status():
      temperatureService.check_temp()

    # stop infinit loop
    sleep_ms(500)

run()  
  