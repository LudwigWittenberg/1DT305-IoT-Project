from dht import DHT11
from machine import Pin

# Class for talking to DHT11 sensor
class DHTSensor:
  # Connecs to the sensor
  def __init__(self, pin: int):
    self.sensor = DHT11(Pin(pin))

  # returns the temperature and the humidity
  def get_temp(self):
    self.sensor.measure()
    temperature = self.sensor.temperature()
    
    return temperature