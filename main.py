from time import sleep

# ------------ IMPORTS -----------
from lib.PicoLed import PicoLed
from services.TemperatureService import TemperatureService
from lib.IR.RawIRRecorder import RawIRRecorder
from config.DeviceConfig import DeviceConfig
from lib.System import System
from lib.Led import Led
from lib.PIEZO.Piezo import Piezo
from services.MQTTService import MQTTService
from services.DataService import DataService
from lib.DHTSensor import DHTSensor
from lib.PhotoResistor import PhotoResistor
# --------------------------------

# ---------- LOAD_CONFIG ---------
from config.PinConfig import *
from config.ValueConfig import *
from config.WifiConfig import WIFI_ENABLE
from config.MQTTConfig import MQTT_ENABLE
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
dhtSensor = DHTSensor(dhtSensorPin)
photoSensor = PhotoResistor(photoPin)
temperatureService = TemperatureService(dhtSensor, greenLed, redLed, max_temp, irTransmitterPin, piezo)
system = System(yellowLed, greenLed, redLed, ir, photoSensor, piezo, darkness_level)
mqtt = None
dataService = None
# --------------------------------

# ------------- MQTT -------------
wifiEnable = WIFI_ENABLE or False
mqttEnable = MQTT_ENABLE or False


if wifiEnable and mqttEnable:
  mqtt = MQTTService()
  mqtt.connect()
  dataService = DataService(dhtSensor, photoSensor, system, temperatureService)
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
  try:
    while True:
      system.check_system_status()
      if system.get_system_status():
        temperatureService.check_temp()
      
      # If wifi is enabled we will puplish the data to MQTT
      if wifiEnable and mqttEnable:
        data = dataService.get_data()
        mqtt.publish(data)
        
      # stop infinit loop
      sleep(10)
  except Exception as e:
    print("Error in code: ", e)
    
run()