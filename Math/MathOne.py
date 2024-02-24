import math

def degrees_to_rad(degrees):
    radians = degrees * math.pi / 180
    return radians

degrees = float(input())
print(degrees_to_rad(degrees))