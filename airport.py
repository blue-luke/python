from plane import *

class Airport(Plane):
  def __init__(self, Plane):
    self.plane = Plane()


  def plane_left_airport(self):
    if self.plane.take_off_plane() == "Plane has taken off":
      return True
    
  def plane_at_airport(self):
    if self.plane.land_plane() == "Plane has landed":
      return True 