from umqtt.simple import MQTTClient

# ------- MQTT CREDENTIALS -------
from config.MQTTConfig import *
# --------------------------------

class MQTT:
  def __init__(self):
    self.client = MQTTClient(client_id='pico-client', server=MQTT_SERVER_IP, port=MQTT_SERVER_PORT, user=MQTT_USERNAME, password=MQTT_PASSWORD)
  
  def connect(self):
    self.client.connect()
    print('Connected')
  
  def publish(self):
    self.client.publish("test", "Hello from Pico WH")
    print('PUBLICERAT')
    
  def disconnect(self):
    self.client.disconnect()