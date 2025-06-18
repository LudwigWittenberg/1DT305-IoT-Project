from lib.IR.RawIRPlayer import RawIRPlayer
from lib.PIEZO.PiezoSongs import high_temp_song, success_signal

# Temperature service that toggles LEDS to show if the temp is good or bad.
class TemperatureService:
  def __init__(self, dhtSensor, greenLed, redLed, maxTemp, irTransmitterPin: int, piezo):
    self.dhtSensor = dhtSensor
    self.greenLed = greenLed
    self.redLed = redLed
    self.MAX_TEMP = maxTemp
    self.ir_transmitter = RawIRPlayer(irTransmitterPin)
    self.over_limit = False
    self.piezo = piezo
    self.ac_status = False
  
  # Get the temp from the DHT11 Sensor and decides what action to take.
  def check_temp(self):
    self.dhtSensor.measure()
    temp = self.dhtSensor.get_temp()
    print('Temperature: ', temp, '°C')
    
    if temp >= self.MAX_TEMP:
      self.greenLed.off()
      self.redLed.on()
      
      if not self.over_limit:
        self.piezo.playsong(high_temp_song)
        self.ir_transmitter.play("AC_ON")
        self.over_limit = True
        self.ac_status = True
    else:
      self.greenLed.on()
      self.redLed.off()
      
      if self.over_limit:
        self.piezo.playsong(success_signal)
        self.ir_transmitter.play("AC_OFF")
        self.over_limit = False
        self.ac_status = False

  # Returns the max temp.
  def get_max_temp(self):
    return self.MAX_TEMP
  
  def get_ac_status(self):
    return self.ac_status