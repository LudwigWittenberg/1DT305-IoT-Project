from machine import Pin

class Led:
  def __init__(self, pin: int):
    self.led = Pin(pin, Pin.OUT)
  
  def on(self):
    self.led.on()
    
  def off(self):
    self.led.off()