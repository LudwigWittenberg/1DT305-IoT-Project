from lib.IR.IRMatcher import compare_ir_signals

class System:
  def __init__(self, yellowLed, greenLed, redLed, irReciver):
    self.system_status = True
    self.yellowLed = yellowLed
    self.greenLed = greenLed
    self.redLed = redLed
    self.ir = irReciver
    
  # Sets the status of the system (on/off)
  def set_system_status(self, incoming_signal):
    pass

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