from dht import DHT11
from machine import Pin

# Class for talking to DHT11 sensor
class DHTSensor:
  # Connecs to the sensor
  def __init__(self, pin: int):
    self.sensor = DHT11(Pin(pin))
    
  def measure(self):
    self.sensor.measure()

  # Returns the temperature and the humidity
  def get_temp(self):
    return self.sensor.temperature()
  
  def get_humidity(self):
    return self.sensor.humidity()