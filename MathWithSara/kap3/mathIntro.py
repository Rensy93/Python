import math


# V= 4/3pir^3
# A = 4pir^2

def calculate_volume(radius):
    volume = ((4 / 3) * math.pi * radius ** 3)
    return volume


def calculate_area(radius):
    area = 4 * math.pi * radius ** 2
    return area


def main():
    radius = 4
    print('Volume with radius ', radius, ': ', calculate_volume(radius))
    print('Area with radius ', radius, ': ', calculate_area(radius))


main()
