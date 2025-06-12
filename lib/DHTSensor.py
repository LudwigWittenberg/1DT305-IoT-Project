from dht import DHT11
from machine import Pin
import time

# Class for talking to DHT11 sensor
class DHTSensor:
  # Connecs to the sensor
  def __init__(self, pin: int):
    self.sensor = DHT11(Pin(pin))

  # returns the temperature and the humidity
  def get_values(self):
    self.sensor.measure()
    temperature = self.sensor.temperature()
    humidity = self.sensor.humidity()
    
    return { temperature, humidity }