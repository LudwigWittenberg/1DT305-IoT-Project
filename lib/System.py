from lib.PhotoResistor import PhotoResistor

class System:
  def __init__(self, yellowLed, greenLed, redLed, irReciver, photoPin):
    self.system_status = True
    self.yellowLed = yellowLed
    self.greenLed = greenLed
    self.redLed = redLed
    self.ir = irReciver
    self.photo = PhotoResistor(photoPin)
    
  # Sets the status of the system (on/off)
  def check_system_status(self):
    self.photo.calculate_darkness()
    darkness_level = self.photo.get_darkness_level()
    
    self.set_system_status(darkness_level)
  
  # Set the action of the darknes level
  def set_system_status(self, darkness):
    if darkness >= 70:
      self.system_offline()
    else: 
      self.system_online()

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