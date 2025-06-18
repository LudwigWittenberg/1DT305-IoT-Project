from machine import ADC, Pin

# Calculate the darkness in a room
class PhotoResistor:
  def __init__(self, photoPin: int):
    self.photo = ADC(Pin(photoPin))
    self.darkness = 0
  
  # Calculate the darkness level in the room
  def calculate_darkness(self):
    light = self.photo.read_u16()
    darkness = round(light / 65535 * 100, 2)
    
    self.darkness = darkness
  
  # Returns the darkness level
  def get_darkness_level(self):
    return self.darkness