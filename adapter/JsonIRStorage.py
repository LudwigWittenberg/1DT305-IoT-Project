import ujson  # json-modulen i MicroPython
from lib.IRCode import IRCode

import os

class JsonIRStorage:
  def __init__(self, filename="ir_codes.json"):
      self.filename = filename
      self.data = self.load()

  # Loads all the codes
  def load(self):
    with open(self.filename, "r") as f:
      content = f.read()
      raw_data = ujson.loads(content)

      # convert to object
      codes = []      
      for key, value in raw_data.items():
        code = IRCode(key, value['code'])
        codes.append(code)
              
      return codes
    return []
  
  # Save new codes
  def save(self):
    to_save = {code.get_type(): code.to_dict() for code in self.data}
    with open(self.filename, "w") as f:
      ujson.dump(to_save, f)
      f.flush()

  # Add a new code
  def add_code(self, key, code):
    code = IRCode(key, code)
    self.data.append(code)
    self.save()

  # Get akk codes
  def get_all_codes(self):
    # Lista alla filer och mappar i rotkatalogen
    return self.data
  
  def get_code(self, name: str):
    for code in self.data:
      if code.get_key() == name:
        return code

  # Resets the binds
  def reset_binds(self):
    self.data = []
    self.save()