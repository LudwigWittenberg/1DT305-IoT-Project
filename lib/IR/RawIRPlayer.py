from machine import Pin, PWM
import ujson
import time

class RawIRPlayer:
  def __init__(self, transmitter_pin, filename="ir_codes.json", scaling=1.0):
    self.transmitter_pin = transmitter_pin
    self.filename = filename
    self.scaling = scaling
    self.data = None

    self.ir_pin = Pin(self.transmitter_pin, Pin.OUT)
    self.pwm = PWM(self.ir_pin)
    self.pwm.freq(38000)
    self.pwm.duty_u16(0)  # Av i början

  def play(self, code_name):
    with open(self.filename, "r") as f:
      self.data = ujson.load(f)
      if code_name not in self.data:
        print(f"Kan inte hitta IR-koden: '{code_name}'")
        return
      raw = self.data[code_name]

    raw = raw[1:]  # Ignorera första värdet om det är en startindikator

    for i, duration in enumerate(raw):
      duration = int(duration * self.scaling)
      if i % 2 == 0:
        self.pwm.duty_u16(32768)  # På (50 % duty cycle)
      else:
        self.pwm.duty_u16(0)      # Av
      time.sleep_us(duration)

    self.pwm.duty_u16(0)  # Se till att det är av i slutet

