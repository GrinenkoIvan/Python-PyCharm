# import math
#
# print("Введите номер фигуры согласно предложенному варианту: 1-прямоугольник, 2-треугольник, 3-круг")
# squar_figure = input("Выберите фигуру: ")
#
# if squar_figure == '1':
#     print("Длины сторон прямоугольника:")
#     a = float(input("a = "))
#     b = float(input("b = "))
#     print("Площадь прямоугольника = ", (a * b))
# elif squar_figure == '2':
#     print("Длины сторон треугольника:")
#     a = float(input("a = "))
#     b = float(input("b = "))
#     s = (a * b) / 2
#     print("Площадь треугольника = ", s)
# elif squar_figure == '3':
#     r = float(input("Радиус круга R = "))
#     s = (math.pi * r ** 2)
#     print("Площадь круга = ", s)
# else:
#     print("Ошибка ввода")


import telegram
# from telegram.ext()
#
# TOKEN = "7369277499:AAFT-sbPbCWJh15kCjvFwTMycuVamKGcFic"
#
#
# def start(update, context):
#     update.message.reply_text("Привет! напиши мне help и узнай что я могу..")
#
#
# def help_command(update, context):

from copy import copy
from typing import Union, cast, List, Callable, Optional, Tuple, TypeVar, TYPE_CHECKING, Sequence


