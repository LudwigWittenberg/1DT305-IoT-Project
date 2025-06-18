from lib.PIEZO.PiezoSongs import start_signal, end_signal

class System:
  def __init__(self, yellowLed, greenLed, redLed, irReciver, photoSensor, piezo, darkness_level):
    self.system_status = True
    self.yellowLed = yellowLed
    self.greenLed = greenLed
    self.redLed = redLed
    self.ir = irReciver
    self.photo = photoSensor
    self.piezo = piezo
    self.darkness_level = darkness_level
    
  # Sets the status of the system (on/off)
  def check_system_status(self):
    self.photo.calculate_darkness()
    darkness_level = self.photo.get_darkness_level()
    
    self.set_system_status(darkness_level)
  
  # Set the action of the darknes level
  def set_system_status(self, darkness):
    if darkness >= self.darkness_level and self.system_status:
      self.system_offline()
    elif not self.system_status: 
      self.system_online()

  # Turn the system On
  def system_online(self):
    self.piezo.playsong(start_signal)
    self.system_status = True
    
  # Turns the system Off
  def system_offline(self):
    self.piezo.playsong(end_signal)
    self.system_status = False
    self.yellowLed.off()
    self.greenLed.off()
    self.redLed.off()
  
  # Returns the current system status (on/off)
  def get_system_status(self):
    return self.system_status