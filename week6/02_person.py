class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def drive(self):
        print(f"The {self.color} {self.model} ")

    def stop(self):
        print(f"The {self.color} {self.model} ")


car1 = Car("RED", "TOYOTA")
car2 = Car("GREEN", "HONDA")

car1.drive()
car2.stop()