from machine import Pin, PWM
import ujson

# IR transmitter module
class RawIRPlayer:
  def __init__(self, transmitter_pin, filename="ir_codes.json", scaling=1.0):
    self.transmitter_pin = transmitter_pin
    self.filename = filename
    self.data = None  

    self.ir_pin = Pin(self.transmitter_pin, Pin.OUT)
    self.pwm = PWM(self.ir_pin)
    self.pwm.freq(38000)
    self.pwm.duty_u16(0)

  # Plays the IR signal
  def play(self, code_name):
    with open(self.filename, "r") as f:
      self.data = ujson.load(f)
      if code_name not in self.data:
        print(f"Cant find the code: '{code_name}'")
        return
      raw = self.data[code_name]

    raw = raw[1:]  # Ignorera startvärdet
