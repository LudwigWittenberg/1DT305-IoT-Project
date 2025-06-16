from machine import Pin
from time import sleep_ms
from lib.ir_rx.nec import NEC_8

# Class for Ir Reciver. Calls himself when he recives ir.
class IrReciver:
  def __init__(self, pin: int, yellowLed):
    self.ir_reciver = NEC_8(Pin(pin, Pin.IN), self.callback)
    self.last_code = None
    self.yellowLed = yellowLed
    
  # Returns the ir code
  def callback(self, data, addr, ctrl):
    if data > 0:
      self.last_code = data
      self.toggleLed()
      return data
    
  def toggleLed(self):
    sleep_ms(200)
    self.yellowLed.off()
    sleep_ms(100)
    self.yellowLed.on()
    sleep_ms(100)
    self.yellowLed.off()
  
  # returns the last code and resets if after a call
  def get_last_code(self):
    code = self.last_code
    
    # reset the last code
    self.last_code = None 
    
    return code