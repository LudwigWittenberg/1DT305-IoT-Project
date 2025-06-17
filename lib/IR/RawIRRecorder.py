from machine import Pin
import time
import ujson

class RawIRRecorder:
  def __init__(self, receiver_pin, filename="ir_codes.json"):
    self.receiver_pin = receiver_pin
    self.filename = filename
    self.ir_pin = Pin(self.receiver_pin, Pin.IN)
    self.data = None
    self.last_call = None
    self.load()

  def record(self, code_name):
    print(f"Väntar på signal för '{code_name}'...")
    raw = self._capture_raw()
    print(f"Signal mottagen, längd: {len(raw)} pulser")
    self.data[code_name] = raw
    self._save()

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

  def _save(self):
    try:
      with open(self.filename, "w") as f:
        ujson.dump(self.data, f)
        f.flush()
      print(f"Signal sparad i {self.filename}")
    except Exception as e:
      print("Kunde inte spara:", e)
        
  def load(self):
    with open(self.filename, "r") as f:
      self.data = ujson.load(f)
        
  def get_length(self):
    return len(self.data)
  
  def get_all_signals(self):
    print(self.data)
    return self.data
  
  def get_last_call(self):
    call = self._capture_raw()
    
    return call
  
  def listen_for_call(self):
    pass