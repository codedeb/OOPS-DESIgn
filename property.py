#use case of properties
from math import pi
class Circle:
    def __init__(self, radius, area = None):
        self._radius = radius
        self._area = area

    @property
    def radius(self):
        return self._radius
    @radius.setter
    def radius(self, value):
        self._area = None
        self._radius  = value
    @property
    def area(self):
        if self._area is None:
            print('calculating area....')
            self._area = pi * (self.radius**2)
      
        return self._area

circle = Circle(1)
print(circle.area)
print(circle.area)

circle.radius = 2
print(circle.area)
print(circle.area)

