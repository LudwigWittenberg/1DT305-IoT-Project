from lib.DHTSensor import DHTSensor
from lib.IR.RawIRPlayer import RawIRPlayer
from lib.PIEZO.PiezoSongs import high_temp_song, success_signal

# Temperature service that toggles LEDS to show if the temp is good or bad.
class TemperatureService:
  def __init__(self, dhtSensorPin: int, greenLed, redLed, maxTemp, irTransmitterPin: int, piezo):
    self.dhtSensor = DHTSensor(dhtSensorPin)
    self.greenLed = greenLed
    self.redLed = redLed
    self.MAX_TEMP = maxTemp
    self.ir_transmitter = RawIRPlayer(irTransmitterPin)
    self.over_limit = False
    self.piezo = piezo
  
  # Get the temp from the DHT11 Sensor and decides what action to take.
  def check_temp(self):
    temp = self.dhtSensor.get_temp()
    
    if temp >= self.MAX_TEMP:
      self.greenLed.off()
      self.redLed.on()
      
      if not self.over_limit:
        self.piezo.playsong(high_temp_song)
        self.ir_transmitter.play("AC_ON")
        self.over_limit = True
    else:
      self.greenLed.on()
      self.redLed.off()
      
      if self.over_limit:
        self.piezo.playsong(success_signal)
        self.ir_transmitter.play("AC_OFF")
        self.over_limit = False

  # Returns the max temp.
  def get_max_temp(self):
    return self.MAX_TEMP