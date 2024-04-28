class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)

  

class Car:
  def __init__(self, color, brand, year ):
    self.color = color
    self.brand = brand
    self.year = year
  
  def __str__(self) -> str:
    return f"{self.brand} Car: {self.color} color."  
  
  def describe_car(self):
    return f"Color:{self.color}, Brand: {self.brand}, Year: {self.year}"

c1 = Car("red", "Honda", 2022)
c2 = Car("yellow", "Toyota", 2021)


print(c1.describe_car())

