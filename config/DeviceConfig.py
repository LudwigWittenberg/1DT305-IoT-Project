from time import sleep_ms

# ---------- ALL CODES ----------
keys = [
  'AC_ON',
  'AC_OFF'
]
# -------------------------------

class DeviceConfig:
  def __init__(self, irReciver, yelloLed, greenLed):
    self.irReciver = irReciver
    self.yellowLed = yelloLed
    self.greenLed = greenLed
  
  # Check if the device is configured (mapped all IR Signals)
  def is_configured(self):
    return (self.irReciver.get_length() == len(keys))
  
  # Start the process to setup the device and configure the IR signals
  def start_setup_process(self):
    for key in keys:
      self.yellowLed.on()
      self.irReciver.record(key)
      sleep_ms(200)
      self.greenLed.on()
      sleep_ms(200)
      self.greenLed.off()
    
    self.setup_completed()
    
  # Creates a signal when the setup is completed
  def setup_completed(self):
    sleep_ms(1000)
    for i in range(5):
      sleep_ms(200)
      self.greenLed.on()
      sleep_ms(200)
      self.greenLed.off()
    
    self.yellowLed.off()