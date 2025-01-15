class Car:
    
    car_counter = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.car_counter += 1
    
    def display(self):
        return f"Brand Name: {self.brand}, Model Name: {self.model}"
    
    def fuel_type(self):
        return "Diesel Or Petrol"
    
class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize

    def showDetails(self):
        return f"{super().display()}, Battery Size: {self.batterySize}."
     
    def fuel_type(self):
        return "Electric Charge"



car1 = ElectricCar("Toyota", "FielderX", "65Kwh")
print(car1.showDetails())
print(car1.fuel_type())

car2 =  Car("Haval", "Jolion")
print(car2.display())
print(car2.fuel_type())


print(Car.car_counter)