from plane import *

class Airport(Plane):
  def __init__(self, Plane):
    self.plane1 = Plane()
    self.plane2 = Plane()
    self.planes = [self.plane1, self.plane2]
    self.capacity = 1
    self.landed_planes = 0

  def land(self, plane):
    if self.landed_planes == self.capacity:
      return "Airport is full"
    else:
      self.landed_planes += 1
      return plane.land()
        

  def plane1(self):
    return self.plane1
