from machine import Pin, PWM
import time
import ujson

class RawIRPlayer:
  def __init__(self, transmitter_pin, filename="ir_codes.json", scaling=1.0):
    self.transmitter_pin = transmitter_pin
    self.filename = filename
    self.data = None  

    self.ir_pin = Pin(self.transmitter_pin, Pin.OUT)
    self.pwm = PWM(self.ir_pin)
    self.pwm.freq(38000)
    self.pwm.duty_u16(0)

  def play(self, code_name):
    with open(self.filename, "r") as f:
      self.data = ujson.load(f)
      if code_name not in self.data:
        print(f"Hittar ej koden '{code_name}'")
        return
      raw = self.data[code_name]

    raw = raw[1:]  # Ignorera startvärdet

    print(f"Spelar '{code_name}'")

    print("Playback klar")