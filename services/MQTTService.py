from umqtt.simple import MQTTClient
import ujson

# ------- MQTT CREDENTIALS -------
from config.MQTTConfig import *
# --------------------------------

class MQTTService:
  def __init__(self):
    self.client = MQTTClient(client_id='pico-client', server=MQTT_SERVER_IP, port=MQTT_SERVER_PORT, user=MQTT_USERNAME, password=MQTT_PASSWORD)
  
  def connect(self):
    self.client.connect()
    print('Connected')
  
  def publish(self, data):
    jsonData = self._to_json(data)
    
    self.client.publish("sensor/data", jsonData)
    
  def _to_json(self, data):
    return ujson.dumps(data)
    
  def disconnect(self):
    self.client.disconnect()