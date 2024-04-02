import math

def area_calc(r):
    return 2*math.pow(r, 2)*math.pi
    
def circumference_calc(r):
    return 2*math.pi*r
    
def diameter_calc(r):
    return r*2
    
def circle_calc(r):
    return (round(area_calc(r), 2), round(circumference_calc(r), 2), round(diameter_calc(r), 2))

radius = int(input('Please enter a radius: \n'))
print(circle_calc(radius))