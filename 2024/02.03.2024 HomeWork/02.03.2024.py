# import geometric
#
# from abc import ABC, abstractmethod
#
#
#
#
# class Table(ABC):
#     def __init__(self, table_type, width=None, height=None, radius=None):
#         self.table_type = table_type
#         self.width = width
#         self.height = height
#         self.radius = radius
#
#     def __str__(self):
#         if self.table_type == 'прямоугольный':
#             return f'Форма стола: {self.table_type}\nШирина стола: {self.width}\nВысота стола: {self.height}'
#         else:
#             return f'Форма стола: {self.table_type}\nРадиус стола: {self.radius}'
#
#     @abstractmethod
#     def square(self):
#         pass
#
#
# class RectangleTable(Table):
#     def __init__(self, width, height):
#         super().__init__(table_type='прямоугольный', width=width, height=height)
#
#     def square(self):
#         return self.width * self.height
#
#
# class CircleTable(Table):
#     def __init__(self, radius):
#         super().__init__(table_type='круглый', radius=radius)
#
#     def square(self):
#         return round(self.radius ** 2 * 3.14, 2)
#
#
# tables = [
#     RectangleTable(20, 10),
#     RectangleTable(20, 20),
#     CircleTable(20)
# ]
#
# for table in tables:
#     print(table)
#     print(f'Площадь стола: {table.square()}\n')
