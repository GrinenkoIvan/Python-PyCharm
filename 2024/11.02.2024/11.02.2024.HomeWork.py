import math


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def print_info(self):
        print("Длинна прямоугольника:", self.length, '\n'
              "Ширина прямоугольника:", self.width,)

    def set_square(self):
        print("Площадь прямоугольника:", self.length * self.width)

    def set_perimeter(self):
        print("Периметр прямоугольника", 2 * (self.length + self.width))

    def set_hypotenuse(self):
        res = round(math.sqrt(self.length**2 + self.width**2), 2)
        print("Гипотенуза прямоугольника", res, "\n")

    def rectangle_image(self):
        for i in range(self.width):
            print('* ' * self.length,)


pr = Rectangle(9, 3)
pr.print_info()
pr.set_square()
pr.set_perimeter()
pr.set_hypotenuse()
pr.rectangle_image()
