from plane import *
from airport import *

def test_land_plane():
  plane = Plane()
  assert plane.land_plane() == "Plane has landed"

def test_take_off_plane():
  plane = Plane()
  assert plane.take_off_plane() == "Plane has taken off"

def test_landed_plane_cannot_land():
  airport = Airport(Plane)
  airport.plane.land_plane()
  assert airport.plane.land_plane() == "Error: plane has already landed"

def test_takenoff_plane_cannot_takeoff():
  airport = Airport(Plane)
  airport.plane.take_off_plane()
  assert airport.plane.take_off_plane() == "Error: plane has already taken off"