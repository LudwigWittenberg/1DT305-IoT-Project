from machine import Pin

# Led Class Module
# Connects and handle everything with the led
class Led:
  def __init__(self, pin: int):
    self.led = Pin(pin, Pin.OUT)
    self.off()
  
  def on(self):
    self.led.on()
    
  def off(self):
    self.led.off()