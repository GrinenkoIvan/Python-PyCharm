# class Integer:
#
#     @staticmethod
#     def verify_cord(coord):
#         if not isinstance(coord, int):
#             raise TypeError(f'Координата {coord} должна быть целым числом')
#
#     def __set_name__(self, owner, name):
#         self.__name = "coord_" + name
#
#     def __get__(self, instance, owner):
#         # return instance.__dict__[self.__name]
#         return getattr(instance, self.__name)
#
#     def __set__(self, instance, value):
#         instance.__dict__[self.__name] = value
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()

# Метаклассы

# a = 5
# print(type(a))
# print(type(int))

# class MyList(list):
#     def get_length(self):
#         return len(self)
#
#
# lst = MyList()
# lst.append(5)
# lst.append(8)
# print(lst, lst.get_length())
#
# MyList1 = type(
#     "MyList",
#     (list,),
#     dict(get_length=lambda self: len(self))
# )
#
# lst1 = MyList1()
# lst1.append(5)
# lst1.append(8)
# print(lst1, lst1.get_length())
#
# print(lst.__dict__)
# print(lst1.__dict__)
#
# print(MyList.__dict__)
# print(MyList1.__dict__)


# from geometry import sq, trian, rect
# # import
# # from geometry import *
#
#
# def run():
#     r1 = rect.Rectangle(1, 2)
#     r2 = rect.Rectangle(3, 4)
#
#     s1 = sq.Square(10)
#     s2 = sq.Square(20)
#
#     t1 = trian.Triangle(1, 2, 3)
#     t2 = trian.Triangle(4, 5, 6)
#
#     shape = [r1, r2, s1, s2, t1, t2]
#
#     for g in shape:
#         print(g.get_perimetr())
#
#
# if __name__ == '__main__':
#     run()