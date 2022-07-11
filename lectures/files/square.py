# CREATING OUR OWN MODULE 
# for calculating square of rectangle, area of circle and triangle 

from math import pi, pow

def rectangle(a, b): 
    return round(a * b, 2)
    # square of our rectangle with round up to 2 digits after comma 

def triangle(a, h): 
    return round(0.5 * a * h, 2)

def circle(r): 
    return round(pi * pow(r, 2), 2)