# implement variable function argument and find the area of a rectangle

def calculate_area(*args):
    if len(args) == 1:
        return args[0] ** 2
    elif len(args) == 2:
        return args[0] * args[1]
    else:
        return 0

area_square = calculate_area(5)
area_rectangle = calculate_area(3, 4)
print("Area of Square:", area_square)
print("Area of Rectangle:", area_rectangle)
