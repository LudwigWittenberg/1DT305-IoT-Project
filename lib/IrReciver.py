from machine import Pin
from time import sleep
from lib.ir_rx.nec import NEC_8

# Class for Ir Reciver. Calls himself when he recives ir.
class IrReciver:
  def __init__(self, pin: int):
    self.ir_reciver = NEC_8(Pin(pin, Pin.IN), self.callback)
    self.last_code = None
    
  # Returns the ir code
  def callback(self, data, addr, ctrl):
    if data > 0:
      # print(data)
      self.last_code = data
      return data
  
  # returns the last code and resets if after a call
  def get_last_code(self):
    code = self.last_code
    
    # reset the last code
    self.last_code = None 
    
    return code