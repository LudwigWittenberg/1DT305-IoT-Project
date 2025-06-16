from adapter.JsonIRStorage import JsonIRStorage

class System:
  def __init__(self, yellowLed, greenLed, redLed):
    self.system_status = True
    self.irCodes = JsonIRStorage()
    self.yellowLed = yellowLed
    self.greenLed = greenLed
    self.redLed = redLed
    
  # Sets the status of the system (on/off)
  def set_system_status(self, ir_code):
    if not self.system_status and ir_code == self.irCodes.get_code('pico_on').get_code():
      self.system_online()
    elif self.system_status and ir_code == self.irCodes.get_code('pico_off').get_code():
      self.system_offline()  
  
  # Turn the system On
  def system_online(self):
    self.system_status = True
    
  # Turns the system Off
  def system_offline(self):
    self.system_status = False
    self.yellowLed.off()
    self.greenLed.off()
    self.redLed.off()
  
  # Returns the current system status (on/off)
  def get_system_status(self):
    return self.system_status