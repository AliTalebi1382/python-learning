class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")


car1 = Car("BMW", "M4")
car2 = Car("Toyota", "Camry")

car1.show_info()
car2.show_info()
