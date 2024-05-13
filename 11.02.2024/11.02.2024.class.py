# class Point:
#     x = 1
#     y = 1
#
#
# p1 = Point()
# print(p1.x)  # Получаем доступ/значение к переменной
# print(p1.y)
# p1.x = 5
# p1.y = 24
# print(p1.x)
# print(p1.y)
# print(p1.__dict__)
# print(id(p1))
#
# p2 = Point()
# p2.x = 10
# p2.y = 25
# print(p2.x)
# print(p2.y)
# print(p2.__dict__)
# print(id(p2))
# print(id(Point))
#
# print(isinstance(p1, Point))
# print(isinstance(p2, Point))

# ----------------------------------------------------------------------------------------------------------------

# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#         print(self.__dict__)
#
#
# p1 = Point()
# # p1.x = 5
# # p1.y = 24
# p1.set_coord(5, 24)  # {'x': 5, 'y': 24}
# Point.set_coord(p1, 6, 27)  # {'x': 6, 'y': 27}
#
# p2 = Point()
# # p2.x = 10
# # p2.y = 30
# p2.set_coord(10, 30)  # {'x': 10, 'y': 30}
# Point.set_coord(p2, 11, 33)  # {'x': 11, 'y': 33}

# ---------------------------------------------------------------------------------------------------------------

# class Human:
#     name = "name"
# birthday = "00.00.0000"
# phone = "00-00-00"
# country = "country"
# city = "city"
# address = "street, house"
#
# def print_info(self):
#     print(" Персональные данные ".center(40, "*"))
#     print(f"Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\n"
#           f"Страна: {self.country}\nГород: {self.city}\nДомашний адрес: {self.address}")
#     print("=" * 40)
#
# def input_info(self,first_name, birthday,phone, country, city, address):
#     self.name = first_name
#     self.birthday = birthday
#     self.phone = phone
#     self.country = country
#     self.city = city
#     self.address = address
#
# def set_address(self, address):
#     self.address = address

#     def get_address(self):
#         return self.address
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Aveliya", "25.12.2009", "525-29-05", "Russia", "Moscow", "Билибина 6")
# h1.print_info()
# h1.set_address("ул. Московская, 1")
# print(h1.get_address())
# h1.set_name("Авелия")
# print(h1.get_name())

# --------------------------------------------------------------------------------------------------------------

# class Person:
#     skill = 10  # статическое свойство
#     count = 0
#
#     # name = ""
#     # surname = ""
#
#     def __init__(self, name, surname):  # __init__ магический или дендер метод
#         self.name = name  # динамические свойства
#         self.surname = surname
#         self.count += 1
#
#     # def __del__(self):
#     #     print("Удаление экземпляра", self)
#     #
#     # def print_info(self):
#     #     print("Данные сотрудника:", self.name, self.surname)
#     #
#     # def add_skill(self, k):
#     #     self.skill += k
#     #     print("Квалификация сотрудника:", self.skill, end="\n\n")
#
#
# p1 = Person("Виктор", "Резник")
# # p1.print_info()
# # p1.add_skill(3)
# # del p1
# print(p1.count)
#
# p2 = Person("Анна", "Долгих")
# # p2.print_info()
# # p2.add_skill(2)
# print(p2.count)

#--------------------------------------------------------------------------------------------------------------

# Задача

# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота: ", self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "выключается")
#
#         Robot.k -= 1
#
#         if Robot.k == 0:
#             print(self.name, "был последним")
#         else:
#             print(self.name, "был последним")
#
#     def sey_hi(self):
#         print("Приветствую! Меня зовут: ", self.name)
#
#
# droid1 = Robot('R2-D2')
# droid1.sey_hi()
# print("Численность роботов: ", Robot.k)
#
# droid2 = Robot('C-3PO')
# droid2.sey_hi()
# print("Численность роботов: ", Robot.k)
#
# droid3 = Robot('S-9PO')
# droid3.sey_hi()
# print("Численность роботов: ", Robot.k)
#
# print("\nЗдесь роботы могут проделать какую-то работу\n")
#
# print("Роботы закончили свою работу. Давайте их выключим.")
# del droid1
# del droid2
# del droid3
#
# print("Численность роботов: ", Robot.k)