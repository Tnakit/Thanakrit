""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"


class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors

    def get_info(self):
        return f"{super().get_info()}, Number of doors: {self.number_of_doors}"


vehicle1 = Vehicle("Toyota", "Corolla", 2022)
car1 = Car("Honda", "Civic", 2024, 4)

print(vehicle1.get_info())
print(car1.get_info())