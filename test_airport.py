from airport import *
from plane import *

def test_airport_full():
  airport = Airport(Plane)
  plane1 = airport.plane1
  plane2 = airport.plane2
  airport.land(plane1)
  assert airport.land(plane2) == "Airport is full"

