from machine import Pin
from time import sleep

# Class for blinking the LED on the Pico Board
class PicoLed:
  def __init__(self):
    self.led = Pin('LED', Pin.OUT)
    
  def blink(self):
    self.led.on()
    sleep(0.5)
    self.led.off()
    sleep(0.5)