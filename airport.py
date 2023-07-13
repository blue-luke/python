from plane import *

class Airport(Plane):
  def __init__(self, Plane):
    self.plane1 = Plane()
    self.plane2 = Plane()
    self.planes = [self.plane1, self.plane2]
    self.capacity = 1
    self.landed_planes = 0

  def plane1(self):
    return self.plane1

  # def plane_left_airport(self):
  #   if self.plane.take_off_plane() == "Plane has taken off":
  #     return True
    
  # def plane_at_airport(self, plane):
  #   if self.plane.land_plane() == "Plane has landed":
  #     return True 