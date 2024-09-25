class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(4, 5)
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")

class Car:
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year

    def drive(self):
        print(f"The {self.color} {self.model} built in {self.year} is driving")

    def stop(self):
        print(f"The {self.color} {self.model} built in {self.year} is stopped")

car1 = Car("Red", "Toyota", 2020)
car2 = Car("Black", "BMW", 2019)

car1.drive()
car1.stop()
car2.drive()
car2.stop()