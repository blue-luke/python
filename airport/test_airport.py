from airport import *
from plane import *

# def test_airport_full():
#   airport = Airport(Plane, 1)
#   plane1 = getattr(airport, 'planes')[0]
#   plane2 = getattr(airport, 'planes')[1]
#   airport.land(plane1)
#   assert airport.land(plane2) == "Airport is full"

def test_definable_capacity():
  capacity = 2
  airport = Airport(Plane, capacity)
  assert getattr(airport, 'capacity') == 2
