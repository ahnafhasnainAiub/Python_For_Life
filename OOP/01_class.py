class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display(self):
        return f"{self.brand} {self.model}"

# car1 = Car("Honda", "Vezel")
# print(car1.brand, car1.model)

car2 = Car("Toyota", "FielderX")
print(car2.display())