import math


def calculate_area(a, b, c):
    s = calculate_s(a, b, c)
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


def calculate_s(a, b, c):
    return (a + b + c) / 2


def main():
    a, b, c = eval(input("Vilka sidor har triangelen? Skriv med kommatecken emellan."))
    area = calculate_area(a, b, c)
    print(area)


main()
