def area_of_a_trapezoid(h, a, b):
    area = 0.5*h*(a+b)
    return area

h, a, b = float(input()), float(input()), float(input())

print(area_of_a_trapezoid(h,a,b))