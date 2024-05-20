# class Point3D:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __str__(self):
#         return f"{self.x}, {self.y}, {self.z}"
#
#     def __add__(self, other):
#         if not isinstance(other, Point3D):
#             raise ArithmeticError("Правый операнд должен быть типом Point3D")
#         return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)
#
#     def __sub__(self, other):
#         if not isinstance(other, Point3D):
#             raise ArithmeticError("Правый операнд должен быть типом Point3D")
#         return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)
#
#     def __mul__(self, other):
#         if not isinstance(other, Point3D):
#             raise ArithmeticError("Правый операнд должен быть типом Point3D")
#         return Point3D(self.x * other.x, self.y * other.y, self.z * other.z)
#
#     def __truediv__(self, other):
#         if not isinstance(other, Point3D):
#             raise ArithmeticError("Правый операнд должен быть типом Point3D")
#         if other.x == 0 or other.y == 0 or other.z == 0:
#             raise ValueError("Деление на 0 не допустимо")
#         return Point3D(self.x / other.x, self.y / other.y, self.z / other.z)
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y and self.z == other.z
#
#     def __getitem__(self, key):
#         if key == "x":
#             return self.x
#         elif key == "y":
#             return self.y
#         elif key == "z":
#             return self.z
#         else:
#             raise KeyError(f"Недопустимый ключ: {key}")
#
#     def __setitem__(self, key, value):
#         if key == "x":
#             self.x = value
#         elif key == "y":
#             self.y = value
#         elif key == "z":
#             self.z = value
#         else:
#             raise KeyError(f"Недопустимый ключ: {key}")
#
#
# coord1 = Point3D(12, 15, 18)
# coord2 = Point3D(6, 3, 9)
# print(f"Координаты 1-й точки: {coord1}\nКоординаты 2-й точки: {coord2}")
#
# coord3_add = coord1 + coord2
# print(f"Сложение координат: ({coord3_add})")
#
# coord3_sub = coord1 - coord2
# print(f"Вычитание координат: ({coord3_sub})")
#
# coord3_mul = coord1 * coord2
# print(f"Умножение координат: ({coord3_mul})")
#
# coord3_truediv = coord1 / coord2
# print(f"Деление координат: ({coord3_truediv})")
#
# print(f"Равенство координат: ({coord1 == coord2})")
#
# print(f"x = {coord1['x']} x1 = {coord2['x']}")
# print(f"y = {coord1['y']} y1 = {coord2['y']}")
# print(f"z = {coord1['z']} z1 = {coord2['z']}")
#
# coord1["x"] = 20
# print(f"Запись значения в координату x: {coord1['x']}")
