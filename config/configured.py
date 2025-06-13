from time import sleep
from adapter.JsonIRStorage import JsonIRStorage
from lib.IrReciver import IrReciver

# ---------- ALL CODES ----------
keys = [
  'pico_on', 
  'pico_off',
  'ac_on',
  'ac_off'
]
# -------------------------------

class Config:
  def __init__(self, irReciver: IrReciver):
    self.jsonFile = JsonIRStorage()
    self.irReciver = irReciver
    
  def is_configured(self):
    return len(self.jsonFile.get_all_codes()) > 0
  
  # Start the setup process
  def start_setup_process(self):
    for key in keys:
      self.set_code(key, self.get_code())
  
  # Saves each code to it corresponding key
  def set_code(self, key, code):
    self.jsonFile.add_code(key, code)
      
  # Get the code from the IR reciver
  # If the input is valid we returns the code 
  def get_code(self):
    valid_input = True
    while valid_input:
      input = self.wait_for_input()
      
      if self.is_input_valid(input):
        print('Added value:', input)
        valid_input = False
        return input
    
  # Wait for input from the user
  def wait_for_input(self):
    code = self.irReciver.get_last_code()
    sleep(2)
    return code
  
  def is_input_valid(self, input):
    return not input == None