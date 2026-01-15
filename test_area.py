import math
from app import calculate_area, calculate_circumference

def test_circle_calculation():
    radius = 1
    assert calculate_area(radius) == math.pi
    assert calculate_circumference(radius) == 2 * math.pi
