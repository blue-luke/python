class Plane():
  def __init__(self, is_landed = True):
    self.is_landed = is_landed

  def land(self):
    if not self.is_landed:
      self.is_landed = True
      return "Plane has landed"
    else:
      return "Error: plane has already landed"

  def take_off(self):
      if self.is_landed:
        self.is_landed = False
        return "Plane has taken off"
      else:
        return "Error: plane has already taken off"

  def airborne(self):
    return not self.is_landed

  def parked(self):
    return self.is_landed