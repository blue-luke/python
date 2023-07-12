from app import *

def test_land_plane():
  plane = Plane()
  assert plane.land_plane() == "Plane has landed"

def test_take_off_plane():
  plane = Plane()
  assert plane.take_off_plane() == "Plane has taken off"

def test_landed_plane_cannot_land():
  plane = Plane()
  plane.land_plane()
  assert plane.land_plane() == "Error: plane has already landed"

def test_takenoff_plane_cannot_takeoff():
  plane = Plane()
  plane.take_off_plane()
  assert plane.take_off_plane() == "Error: plane has already taken off"