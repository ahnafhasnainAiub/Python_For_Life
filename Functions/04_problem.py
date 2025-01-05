# Create a function that returns both the area and circumstance of a circle given its radius.

import math

def circle(r):
    area = round(math.pi * (r**2), 2)
    circumference = round(2 * math.pi * r, 2)

    return area, circumference    

a, c = circle(4)

print("Area of the circle:",a, "and Circumference :",c)
