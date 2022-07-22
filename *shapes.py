class Rectangle:
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
        # pass

    def perimeter(self):
        return (self.length * 2) + (self.width * 2)
        # pass


class Square(Rectangle):
    def __init__(self, length=0, width=0):
        super().__init__(length, width)


rect = Rectangle(3, 5)
print(rect.perimeter())
print(rect.area())

square = Square(2, 2)
print(square.area())
print(square.perimeter())


