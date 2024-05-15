# class Clock:
#     DAY = 86400
#
#     def __init__(self, sec):
#         if not isinstance(sec, int):
#             raise ValueError('Секунды должны быть целим числом')
#         self.sec = sec % self.DAY
#
#     @staticmethod
#     def get_form(x):
#         return str(x) if x > 9 else '0' + str(x)
#
#     @staticmethod
#     def check_instance(value):
#         if not isinstance(value, Clock):
#             raise ArithmeticError('Правый операнд должен быть типом Clock')
#
#     def __str__(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f'{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}'
#
#     def __add__(self, other):
#         self.check_instance(other)
#         return Clock(self.sec + other.sec)
#
#     def __sub__(self, other):
#         self.check_instance(other)
#         return Clock(self.sec - other.sec)
#
#     def __isub__(self, other):
#         self.check_instance(other)
#         another = self.sec - other.sec
#         return Clock(another)
#
#     def __mul__(self, other):
#         self.check_instance(other)
#         return Clock(self.sec * other.sec)
#
#     def __imul__(self, other):
#         self.check_instance(other)
#         another = self.sec * other.sec
#         return Clock(another)
#
#     def __floordiv__(self, other):
#         self.check_instance(other)
#         return Clock(self.sec // other.sec)
#
#     def __ifloordiv__(self, other):
#         self.check_instance(other)
#         another = self.sec // other.sec
#         return Clock(another)
#
#     def __mod__(self, other):
#         self.check_instance(other)
#         return Clock(self.sec % other.sec)
#
#     def __imod__(self, other):
#         self.check_instance(other)
#         another = self.sec % other.sec
#         return Clock(another)
#
#
# c1 = Clock(600)
# print(f'c1: {c1}')
# c2 = Clock(200)
# print(f'c1 - c2: {c1 - c2}')
# print(f'c1 * c2: {c1 * c2}')
# print(f'c1 // c2: {c1 // c2}')
# print(f'c1 % c2: {c1 % c2}')
# c1 -= c2
# print(f'c1 -= c2: {c1}')
# c1 *= c2
# print(f'c1 *= c2: {c1}')
# c1 //= c2
# print(f'c1 //= c2: {c1}')
# c1 %= c2
# print(f'c1 %= c2: {c1}')
