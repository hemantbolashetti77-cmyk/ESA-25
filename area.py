import sys
import math

def calculate_area(radius):
    return math.pi * radius * radius

def calculate_circumference(radius):
    return 2 * math.pi * radius


if __name__ == "__main__":
    radius = float(sys.argv[1])

    area = calculate_area(radius)
    circumference = calculate_circumference(radius)

    print("Radius:", radius)
    print("Area of Circle:", area)
    print("Circumference of Circle:", circumference)
