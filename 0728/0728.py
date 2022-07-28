# homework
# class Circle:
#   pi = 3.14
  
#   def __init__(self, r, x, y):
#     self.r = r
#     self.x = x
#     self.y = y
  
#   def area(self):
#     return Circle.pi * self.r * self.r
  
#   def circumference(self):
#     return 2 * Circle.pi * self.r
  
#   def center(self):
#     return (self.x, self.y)

# one = Circle(3, 2, 4)
# print(round(one.area(), 2), one.circumference())
#-------------------------------------
# class Animal:
#   def __init__(self, name):
#     self.name = name  
#   def walk(self):
#     print(f'{self.name}! 걷는다!')
#   def eat(self):
#     print(f'{self.name}! 먹는다!')

# class Dog(Animal):

#     def run(self):
#         print(f'{self.name}! 달린다!')

#     def bark(self):
#         print(f'{self.name}! 짖는다!')

# class Bird(Animal):

#     def fly(self):
#         print(f'{self.name}! 푸드덕!')


# dog = Dog('꼽이')
# dog.run() # 꼽이! 달린다! 
# dog.bark() # 꼽이! 짖는다!

# bird = Bird('구구')
# bird.walk() # 구구! 걷는다! 
# bird.eat() # 구구! 먹는다! 
# bird.fly() # 구구! 푸드덕!
#-------------------------------------
# from fibo import fibo_recursion as recursion

# print(recursion(4))
#---------------------------
# workshop

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __int__(self):
        return self.x, self.y

class Rectangle:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        # self.width = abs(p1.x - p2.x) / abs(self.p1.x - self.p2.x)
        # self.heigth = abs(p1.y - p2.y) / abs(self.p1.y - self.p2.y)

    def get_area(self):
        return abs((self.p2.x - self.p1.x) * (self.p1.y - self.p2.y))
        # return self.width * self.heigth
    def get_perimeter(self):
        return 2*(abs(self.p2.x-self.p1.x) + abs(self.p1.y- self.p2.y))
        # return 2 * (self.width + self.heigth)
    def is_square(self):
        return abs(self.p2.x-self.p1.x) == abs(self.p1.y-self.p2.y)
        # return self.width == self.height

p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())

p5 = Point(-1, -2)
p6 = Point(-2, -1)
r3 = Rectangle(p5, p6)
print(r3.get_area())
print(r3.get_perimeter())
print(r3.is_square())
