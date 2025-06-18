class DataService:
  def __init__(self, dhtSensor, photoSensor, system, temperatureService):
    self.dht = dhtSensor
    self.phot = photoSensor
    self.system = system
    self.temperatureService = temperatureService
    
  def get_data(self):
    self.dht.measure()
    temp = self.dht.get_temp()
    hum = self.dht.get_humidity()
    
    self.phot.calculate_darkness()
    darkness = self.phot.get_darkness_level()
    
    system_status = self.system.get_system_status()
    ac_status = self.temperatureService.get_ac_status()
    
    data = {
      'temperature': temp,
      'humidity': hum,
      'darkness': darkness,
      'system_status': system_status,
      'ac_status': ac_status
    }
    
    return data