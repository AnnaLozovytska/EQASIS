class Shape:
    def area(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Приклад використання класів
square = Square(5)
print(f"Area of square: {square.area()}")

circle = Circle(3)
print(f"Area of circle: {circle.area()}")
