class Animal:
    def speak(self):
        print("Some generic sound")

    def move(self):
        print("Animal is moving")

class Dog:
    def __init__(self):
        self.animal = Animal()

    def speak(self):
        self.animal.speak()

    def move(self):
        self.animal.move()

# Приклад використання класів
dog = Dog()
dog.speak()
dog.move()

