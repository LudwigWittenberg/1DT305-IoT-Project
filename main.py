from lib.PicoLed import PicoLed
from lib.DHTSensor import DHTSensor

picoLed = PicoLed()
dHTSensor = DHTSensor(16)

while True:
  picoLed.blink()
  values = dHTSensor.get_values()