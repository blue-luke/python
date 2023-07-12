from airport import *
from plane import *

def test_check_left_airport():
  airport = Airport(Plane)
  assert airport.plane_left_airport() == True

def test_check_at_airport():
  airport = Airport(Plane)
  assert airport.plane_at_airport() == True
