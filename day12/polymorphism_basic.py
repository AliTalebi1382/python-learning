class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name} صدایی تولید می‌کنه.")

class Dog(Animal):
    def make_sound(self):  # override کردن متد پدر
        print(f"{self.name} می‌گه: واق واق!")

class Cat(Animal):
    def make_sound(self):  # override کردن متد پدر
        print(f"{self.name} می‌گه: میو میو!")

# لیستی از حیوانات مختلف
animals = [Dog("رکس"), Cat("میشا"), Animal("موجود ناشناس")]

for animal in animals:
    animal.make_sound()