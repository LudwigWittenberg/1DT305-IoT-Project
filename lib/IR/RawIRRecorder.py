from machine import Pin
import time
import ujson

# IR Reciver module
class RawIRRecorder:
  def __init__(self, receiver_pin, filename="ir_codes.json"):
    self.receiver_pin = receiver_pin
    self.filename = filename
    self.ir_pin = Pin(self.receiver_pin, Pin.IN)
    self.data = None
    self.last_call = None
    self.load()

  # Records the IR signal and saves it to .json file
  def record(self, code_name):
    print(f"Waiting for signal '{code_name}'...")
    raw = self._capture_raw()
    self.data[code_name] = raw
    self._save()

  # Capture the ir signal
  def _capture_raw(self):
    raw = []
    last = self.ir_pin.value()
    start = time.ticks_us()

    while True:
      now = self.ir_pin.value()
      if now != last:
        duration = time.ticks_diff(time.ticks_us(), start)
        raw.append(duration)
        start = time.ticks_us()
        last = now

      if len(raw) > 0 and time.ticks_diff(time.ticks_us(), start) > 30000:
        break
      
    return raw

  # Saves the ir signal to the .json file
  def _save(self):
    try:
      with open(self.filename, "w") as f:
        ujson.dump(self.data, f)
        f.flush()
      print(f"Signal saved in {self.filename}")
    except Exception as e:
      print("Could not save: ", e)
   
  # Loads the already configured codes in to the system.     
  def load(self):
    with open(self.filename, "r") as f:
      self.data = ujson.load(f)
  
  def get_length(self):
    return len(self.data)
  
  # Returns all the loaded signals
  def get_all_signals(self):
    return self.data