
import math

class Shape:
    def __init__(self, length = None, breadth = None, height = None, radius = None):
        self.length = length
        self.breadth = breadth
        self.height = height
        self.radius = radius

    def area(self):                 # not implemented in the class
        raise NotImplementedError("Not Implemented")

class Square(Shape):
    def __init__(self, l, b):
        super().__init__(l, b)

    def area(self):             # implemented in this class but not in the base/parent class. This area() implementation overrides the base/parent class
        print(f"Square Area: {self.length * self. breadth}")

class Circle(Shape):
    def __init__(self, r):
        super().__init__(radius=r)

    def area(self):                 # implemented in this class but not in the base/parent class. This area() implementation overrides the base/parent class
        print(f"Circle Area: {math.pi * self.radius**2}")
s = Square(3, 4)
s.area()
c = Circle(2)
c.area()
