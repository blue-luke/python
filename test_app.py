from app import *

def test_land_plane():
  assert land_plane() == "Plane has landed"

def test_take_off_plane():
  assert take_off_plane() == "Plane has taken off"