# کلاس پدر (Parent class)
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} داره غذا می‌خوره.")

    def sleep(self):
        print(f"{self.name} داره می‌خوابه.")

# کلاس فرزند که از Animal ارث می‌بره
class Dog(Animal):
    def bark(self):
        print(f"{self.name} پارس می‌کنه: واق واق!")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} میو میو می‌کنه.")

# تست
dog = Dog("رکس")
dog.eat()      # از کلاس پدر (Animal) میاد
dog.bark()     # مخصوص کلاس Dog

cat = Cat("میشا")
cat.sleep()    # از کلاس پدر (Animal) میاد
cat.meow()     # مخصوص کلاس Cat