class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_info(self):
        print(f"ماشین: {self.brand} {self.model}")

    def start(self):
        print(f"{self.brand} روشن شد!")

# ساخت دو شیء از کلاس Car
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

car1.show_info()
car1.start()

car2.show_info()
car2.start()