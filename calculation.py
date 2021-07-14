from math import pi

def calc_sq_ft():
    length = float(input("Enter length of house in feet: "))
    width = float(input("Enter width of house in feet: "))
    area = length * width
    if str(area).endswith('.0'):
        return int(area)
    return area

def calc_circ():
    radius = float(input("Enter the radius of the circle: "))
    c = 2 * pi * radius
    return round(c, 2)