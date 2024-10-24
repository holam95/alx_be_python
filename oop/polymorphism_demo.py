import math
class Shape:
    def __init__(self):

    def area(self):
        raise NotImplementedError

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self,pie,radius):
        self.pie = pie
        self.radius =  raadius

    def area(self):
        return math.pi * (radius ** 2)
        

