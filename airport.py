from plane import *

class Airport(Plane):
  def __init__(self, Plane, capacity):
    self.planes = [Plane() for _ in range(capacity)]
    self.capacity = capacity
    self.landed_planes = 0

#Test the below
  def land(self, plane):
    if self.landed_planes == self.capacity:
      return "Airport is full"
    else:
      self.landed_planes += 1
      return plane.land()

