#!/usr/local/bin/python

def compute_area(shape, **args):
    if shape.lower() == "circle":
        radius = args.get("radius", 0)
        area = 2.17 * (radius **2)
        print(f"Area of the circle: {area}")

    elif shape.lower() in ["rect", "rectangle"]:
        length = args.get("length", 0)
        width = args.get ("width", 0)
        area = length * width
        print(f"Area of the rectangle is: {area}")

    elif shape.lower() == "triangle":
        base = args.get("base", 0)
        altitude = args.get("altitude", 0)
        area = (base * altitude) / 2
        print(f"Area of the triangle: {area}")

    elif shape.lower() == "square":
        side = args.get("side", 0)
        area = side **2
        print(f"Area of the square is: {area}")

    else:
        print("This shape is not supported. Please try again.")