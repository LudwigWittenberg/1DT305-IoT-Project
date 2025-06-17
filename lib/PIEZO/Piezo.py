from machine import Pin, PWM
from utime import sleep
from lib.PIEZO.Tones import tones

class Piezo:
  def __init__(self, piezoPin):
    self.piezo = PWM(Pin(piezoPin))
  
  def playtone(self, frequency):
    self.piezo.duty_u16(1000)
    self.piezo.freq(frequency)

  def bequiet(self):
    self.piezo.duty_u16(0)

  def playsong(self, mysong):
    for i in range(len(mysong)):
      if (mysong[i] == "P"):
        self.bequiet()
      else:
        self.playtone(tones[mysong[i]])
      sleep(0.3)
    self.bequiet()