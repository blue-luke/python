# landings = 0

take_offs = 0

class Plane():
  def __init__(self, landings = 0, take_offs = 0):
    self.landings = landings
    self.take_offs = take_offs

  def land_plane(self):
    if self.landings <1:
      self.landings += 1
      return "Plane has landed"
    else:
      return "Error: plane has already landed"


  def take_off_plane(self):
      if self.take_offs <1:
        self.take_offs += 1
        return "Plane has taken off"
      else:
        return "Error: plane has already taken off"