# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split("."))
#         date1 = cls(day, month, year)
#         return date1
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count(".") == 2:
#             day, month, year = map(int, date_as_string.split("."))
#             return day <= 31 and month <= 12 and year <= 3999
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#
# dates = [
#     '30.12.2023',
#     '30-12-2020',
#     '01.01.2024',
#     '12.31.2020'
# ]
# for string_date in dates:
#     if Date.is_date_valid(string_date):
#         date = Date.from_string(string_date)
#         print(date.string_to_db())
#
#     else:
#         print("Неправильная дата или формат строки с датой")

# date2 = Date.from_string("23.10.2024")
# print(date2.string_to_db())
# date3 = Date.from_string("31.08.2024")
# print(date3.string_to_db())

# string_date = "23.10.2024"
# day, month, year = map(int, string_date.split("."))
# print(day, month, year)
# date = Date(day, month, year)
# print(date.string_to_db())

# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, surname, num, percent, value=0):
#         self.surname = surname
#         self.num = num
#         self.percent = percent
#         self.value = value
#         print(f"Счет #{self.num} принадлежащий {self.surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт.")
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def add_money(self, val):
#         self.value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}")
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percent(self):
#         self.value += self.value * self.percent
#         print("Проценты были успешно начислены")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у Вас нет {val} {Account.suffix}")
#         else:
#             self.value -= val
#             print(f"{val} {Account.suffix} было успешно снято !")
#         self.print_balance()
#
#     def print_info(self):
#         print("Информация о счёте:")
#         print('\n', "-" * 20, '\n')
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()  # print(f"Текущий баланс {self.value}")
#         print(f"Проценты: {self.percent:.0%}")
#         print('\n', "-" * 20, '\n')
#
#
# acc = Account("Долгих", "12345", 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# Account.set_usd_rate(2)
# Account.set_eur_rate(3)
# acc.convert_to_usd()
# acc.convert_to_eur()
# acc.edit_owner("Дюма")
# acc.print_info()
# acc.add_percent()
# acc.withdraw_money(100)
# acc.withdraw_money(3000)
# acc.add_money(5000),
# acc.withdraw_money(3000)


class UserData:
    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)

        self.__fio = fio
        self.__old = old
        self.__ps = ps
        self.__weight = weight


    @staticmethod
    def verify_fio(fio):
        if not isinstance(fio, str):
            raise TypeError("fio must be a string(фио должно быть строкой)")


p1 = UserData("Волков Игорь Николаевич", 26, "1234 567890", 80.8)


