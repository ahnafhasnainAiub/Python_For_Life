class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display(self):
        return f"Brand Name: {self.brand}, Model Name: {self.model}"
    
class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize

    def showDetails(self):
        return f"{super().display()}, Battery Size: {self.batterySize}."


car1 = ElectricCar("Toyota", "FielderX", "65Kwh")
print(car1.showDetails())