# from random import choice, randint
#
#
# class Clock:
#     DAY = 86400
#     time_key = {}
#
#     def __init__(self, sec):
#         if not isinstance(sec, int):
#             raise ValueError('Секунды должны быть целим числом')
#         self.sec = sec % self.DAY
#         self.values_init()
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f'{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}'
#
#     def values_init(self):
#         self.time_key['hour'], self.time_key['min'], self.time_key['sec'] = self.get_format_time().split(':')
#
#     @staticmethod
#     def get_form(x):
#         return str(x) if x > 9 else '0' + str(x)
#
#     @staticmethod
#     def check_clock_type(value):
#         if not isinstance(value, Clock):
#             raise ArithmeticError('Правый операнд должен быть типом Clock')
#
#     def __add__(self, other):
#         self.check_clock_type(other)
#         return Clock(self.sec + other.sec)
#
#     def __eq__(self, other):
#         self.check_clock_type(other)
#         return self.sec == other.sec
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#     def __lt__(self, other):
#         self.check_clock_type(other)
#         return self.sec < other.sec
#
#     def __le__(self, other):
#         self.check_clock_type(other)
#         return self.sec <= other.sec
#
#     def __gt__(self, other):
#         self.check_clock_type(other)
#         return self.sec > other.sec
#
#     def __ge__(self, other):
#         self.check_clock_type(other)
#         return self.sec >= other.sec
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError('Ключ должен быть строкой')
#         return self.time_key[item]
#
#     def __setitem__(self, key, value):
#         lst = tuple(zip((key, value), (str, int)))
#         if not map(isinstance, **lst):
#             raise ValueError('Ключ должен быть строкой, а значение целым числом')
#         self.time_key[key] = value


# c1 = Clock(100)
# c2 = Clock(200)
# print(c1.get_format_time())
# print(c2.get_format_time())
#
# print(f'c1 < c2: { c1 < c2}')
# print(f'c2 > c1: { c2 > c1}')
# print(f'c1 > c2: { c1 > c2}')
# print(f'c2 < c1: { c2 < c1}')


# class Student:
#     def __init__(self, name, *marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         raise IndexError('Неверный индекс')
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError('Индекс должен быть целым положительным числом')
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)  # 6
#             self.marks.extend([None] * off)
#
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError('Индекс должен быть целым положительным числом')
#         if key not in range(len(self.marks)):
#             raise IndexError('Индекс за пределами')
#         del self.marks[key]
#
#
# s1 = Student('Сергей', 5, 5, 3, 4, 5,)
# print(s1.name)
# print(s1.marks)
# print(s1.marks[2])
# s1[2] = 9
# print(s1.marks)
# s1[10] = 5
# print(s1.marks)
# del s1[0]

# ----------------------------------------------------------------------------------------------------------

# c1 = Clock(80000)
# print(c1.get_format_time())
# print(c1['hour'], c1['min'], c1['sec'])
# c1['hour'] = 11
# c1['hour'] = '11'
#
# print(c1['hour'], c1['min'], c1['sec'])


# class Cat:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def __str__(self):
#         if self.gender == 'M':
#             return f'{self.name} is good boy!!!'
#         return f'{self.name} is good girl!!!'
#
#     def __repr__(self):
#         return f"Cat('{self.name}', age={self.age}, pol={self.gender})"
#
#     def __add__(self, other):
#         if self.gender != other.gender:
#             return [Cat('No name', 0, choice(['M', 'F'])) for _ in range(0, randint(2, 7))]
#         raise TypeError('Пропаганда ЛГБТ запрещена')
#
#
# cat1 = Cat('Tom', 4, 'M')
# cat2 = Cat('Elsa', 5, 'F')
# print(cat1)
# print(cat2)
# print(cat1 + cat2)

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(1, 2)
# s1 = Square(10)
# s2 = Square(10)
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# shapes = [r1, r2, s1, s2, t1, t2]
#
# for shape in shapes:
#     print(f'Периметр: {shape.get_perimetr()}')