from lib.DHTSensor import DHTSensor
from lib.Led import Led

# Temperature service that toggles LEDS to show if the temp is good or bad.
class TemperatureService:
  def __init__(self, dhtSensorPin: int, greenLedPin: int, redLedPin: int, maxTemp):
    self.dhtSensor = DHTSensor(dhtSensorPin)
    self.greenLed = Led(greenLedPin)
    self.redLed = Led(redLedPin)
    self.MAX_TEMP = maxTemp
    
  def check_temp(self):
    temp = self.dhtSensor.get_temp()
    
    if temp >= self.MAX_TEMP:
      self.greenLed.off()
      self.redLed.on()
    else:
      self.greenLed.on()
      self.redLed.off()
      
  def get_max_temp(self):
    return self.MAX_TEMP