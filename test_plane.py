from plane import *
from airport import *

def test_land_plane():
  plane = Plane()
  plane.take_off()
  assert plane.land() == "Plane has landed"

def test_take_off_plane():
  plane = Plane()
  assert plane.take_off() == "Plane has taken off"





def test_check_left_airport():
  plane = Plane()
  plane.take_off()
  assert plane.airborne() == True

def test_check_at_airport():
  plane = Plane()
  plane.land()
  assert plane.parked() == True





def test_landed_plane_cannot_land():
  plane = Plane()
  plane.land()
  assert plane.land() == "Error: plane has already landed"

def test_takenoff_plane_cannot_takeoff():
  plane = Plane()
  plane.take_off()
  assert plane.take_off() == "Error: plane has already taken off"

