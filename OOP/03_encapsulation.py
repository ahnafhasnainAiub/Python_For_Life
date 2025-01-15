class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):  # Get Method
        return self.__brand
    
    def set_brand(self, brand): # Set Method
        self.__brand = brand
    
    def display(self):
        return f"Brand Name: {self.__brand}, Model Name: {self.model}"
    
class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize

    def showDetails(self):
        return f"{super().display()}, Battery Size: {self.batterySize}."


car1 = ElectricCar("Honda", "FielderX", "65Kwh")

#Using Get method
print("Brand name Using Get Method: ",car1.get_brand())

# Using Set Method
car1.set_brand("Toyota")
print("Updating Brand Value using Set Method : ",car1.get_brand())

print(car1.showDetails())