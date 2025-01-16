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
    
#Using Static Methods
    @staticmethod
    def description():
        return "Car is a four wheeler"

class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize

    def showDetails(self):
        return f"{super().display()}, Battery Size: {self.batterySize}."
     
    def fuel_type(self):
        return "Electric Charge"
    



car1 = Car("Toyota", "FielderX")
car2 = ElectricCar("Honda", "CRV", "75kwh")

print(car1.display())
print(car2.showDetails())


print(Car.description())
print(ElectricCar.description())


print(Car.car_counter)