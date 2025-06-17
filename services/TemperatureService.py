from lib.DHTSensor import DHTSensor
from lib.IR.RawIRPlayer import RawIRPlayer

# Temperature service that toggles LEDS to show if the temp is good or bad.
class TemperatureService:
  def __init__(self, dhtSensorPin: int, greenLed, redLed, maxTemp, irTransmitterPin: int):
    self.dhtSensor = DHTSensor(dhtSensorPin)
    self.greenLed = greenLed
    self.redLed = redLed
    self.MAX_TEMP = maxTemp
    self.ir_transmitter = RawIRPlayer(irTransmitterPin)
    self.over_limit = False
    
  def check_temp(self):
    temp = self.dhtSensor.get_temp()
    
    print(temp)
    
    if temp >= self.MAX_TEMP:
      print('dwadaw')
      self.greenLed.off()
      self.redLed.on()
      
      if not self.over_limit:
        self.ir_transmitter.play("AC_ON")
        self.over_limit = True
    else:
      self.greenLed.on()
      self.redLed.off()
      
      if self.over_limit:
        print('Hdawdad')
        self.ir_transmitter.play("AC_OFF")
        self.over_limit = False
      
  def get_max_temp(self):
    return self.MAX_TEMP