import math
class Shape:

    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return f"The area of the Rectangle is: self.length * self.width"

class Circle(Shape):
    def __init__(self,pie,radius):
        self.pie = pie
        self.radius =  raadius

    def area(self):
        return f"The area of the Circle is: math.pi * (radius ** 2)"
        

