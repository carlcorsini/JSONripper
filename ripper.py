first_names = {"1": "gary", "2": "larry",}
last_names = {"1": "johnson", "2": "swanson"}



class KeyToValue():
  def __init__(self, **kwargs):
    self.dict = {}
    for key, value in kwargs.items():
      self.dict[key] = value

  def json(self):
    rip = {}
    for key, value in self.dict.items():
      rip[key] = value
    print(rip)


new = KeyToValue(**first_names)


new.json()
