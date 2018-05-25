#Write a Python class named Circle.
Use the radius as a constructor.
Create two methods which will compute the AREA and the PERIMETER of a circle. 

A = π r^2 (pi * r squared) 

Perimeter = 2πr 

class Circle:
  def area(self):
    return self.pi * self.radius ** 2
  def __init__(self, pi, radius):
    self.pi = pi 
    self.radius = radius

x = Circle(3.14,5)
print('The area is' ,x.area())

class Perimeter():
  def perm(self):
    return 2 * self.pi * self.radius
  def __init__(self, pi, radius):
    self.pi = pi
    self.radius = radius
    
i = Perimeter(3.14,5)
print('Ther perimeter is', i.perm())
