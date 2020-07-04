import math


def pizza_area(diameter):
    radius = diameter / 2
    area = math.pi * radius ** 2
    return area


def calculate_price_area(pizza_price, area):
    price_area = pizza_price / area
    return round(price_area, 2)


def main():
    diameter = 12
    pizza_price = 100
    area = pizza_area(diameter)
    print('Pizza squerinc price: ', calculate_price_area(pizza_price, area), 'kr')


main()
