# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# cat = [Cat("Пушок")]
# print(cat)  # вывод - [<class '__main__.Cat'>: Пушок]


# class Point:
#     def __init__(self, *args):  # дендер или магический метод
#         self.__coord = args
#
#     def __len__(self):  # дендер или магический метод
#         return len(self.__coord)
#
#
# p = Point(1, 2) # вывод - len = 2
# p = Point(2, 3, 4, 5, 6) #  вывод - len = 5
# print(len(p))

import math
class Point:
    __slots__ = ('x', 'y', '__length')


    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = math.sqrt(x * x + y * y)

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = value



p = Point(1, 2)
print(p.length)
p.length = 20
print(p.x)

