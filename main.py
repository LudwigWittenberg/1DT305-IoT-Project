from time import sleep

# ------------ IMPORTS -----------
from lib.PicoLed import PicoLed
from services.TemperatureService import TemperatureService
from lib.IR.RawIRRecorder import RawIRRecorder
from config.DeviceConfig import DeviceConfig
from lib.System import System
from lib.Led import Led
from lib.PIEZO.Piezo import Piezo
# --------------------------------

# ---------- LOAD_CONFIG ---------
from config.PinConfig import *
from config.ValueConfig import *
# --------------------------------

# ------------- PINS -------------
dhtSensorPin = DHT_SENSOR_PIN or 16
yellowLedPin = YELLOW_LED_PIN or 13
greenLedPin = GREEN_LED_PIN or 15
redLedPin = RED_LED_PIN or 14
irReciverPin = IR_RECIVER_PIN or 19
irTransmitterPin = IR_TRANSMITTER_PIN or  20
photoPin = PHOTO_PIN or 28
piezoPin = PIEZO_PIN or 27
# --------------------------------

# ----------- MAX_TEMP -----------
max_temp = MAX_TEMP or 25
# --------------------------------

# -------- DARKNESS_LEVEL --------
darkness_level = DARKNESS_LEVEL or 70
# --------------------------------

# ------------- INIT -------------
picoLed = PicoLed()
yellowLed = Led(yellowLedPin)
greenLed = Led(greenLedPin)
redLed = Led(redLedPin)
piezo = Piezo(piezoPin)
ir = RawIRRecorder(irReciverPin)
device = DeviceConfig(ir, yellowLed, greenLed)
temperatureService = TemperatureService(dhtSensorPin, greenLed, redLed, max_temp, irTransmitterPin, piezo)
system = System(yellowLed, greenLed, redLed, ir, photoPin, piezo, darkness_level)
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
    sleep(1)

run()
  