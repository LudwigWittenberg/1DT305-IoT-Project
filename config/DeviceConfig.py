from time import sleep

# ---------- ALL CODES ----------
keys = [
  'PICO_ON', 
  'PICO_OFF',
  'AC_ON',
  'AC_OFF'
]
# -------------------------------

class DeviceConfig:
  def __init__(self, irReciver, yelloLed, greenLed):
    self.irReciver = irReciver
    self.yellowLed = yelloLed
    self.greenLed = greenLed
    
  def is_configured(self):
    return (self.irReciver.get_length() == len(keys))
      
  def start_setup_process(self):
    for key in keys:
      self.irReciver.record(key)