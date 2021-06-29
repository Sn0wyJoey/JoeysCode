import sys
import math
import colors

if len(sys.argv) <=1:
    Radius = float(input("What is the radius? >"))
else:
    Radius = float(sys.argv[1])
area = math.pi * math.pow(Radius, 2)
diameter = 2 * Radius
circum = 2 * Radius * math.pi
print ("""With a circle with a radius of {},
The Area is {},
The Diameter is {}, 
The Circumference is {}""".format(round(Radius , 1), round(area , 2), round(diameter , 2), round(circum , 2)))