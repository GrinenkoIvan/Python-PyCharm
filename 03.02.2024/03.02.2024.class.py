# Class Work -----------------------------------------------------------------

# f = open('xyz.txt', 'w')
# lst = [str(i) for i in range(1, 20)] # в файл можно сохранить только строковое значение
# print(lst)
# for index in lst:
#     f.write(index + "\t")
# f.close()

# ----------------------------------------------------------------------------------

# f = open("text3.txt", "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список ф файл;\n")
# f.close()
#
# f = open("text3.txt", "r")
# rl = f.readlines()
# f.close()
#
# print(rl)
# rl[1] = "Hello World\n"
# print(rl)
# f = open("text3.txt", "w")
# f.writelines(rl)
# f.close()

# ------------------------------------------------------------------------------------

# filename = "text3.txt"
# f = open(filename, "r")
# rl = f.readlines()
# f.close()
# print(rl)
# pos = int(input("Введите индекс строки для удаления от 1 до 3 :"))
# if 0 <= pos < len(rl):
#     rl.pop(pos)
# else:
#      print("Индекс введён неверно")
# print(rl)
# f = open(filename, "w")
# f.writelines(rl)
# f.close()

# Вариант 2---------------------------------------------------------------------------------------------------

# def input_index():
#     file = open('text3.txt', 'r')
#     read_text = file.readlines()
#     file.close()
#     index = int(input('Введите номер строки: '))
#     if index not in range(1, len(read_text) + 1) or index < 1:
#         print('Убедитесь что введен корректный номер строки и повторите попытку.')
#         return input_index()
#     else:
#         return read_text, index - 1
#
#
# t, i = input_index()
#
# f = open('text3.txt', 'w')
# del t[i]
# f.writelines(t)
# f.close()

# --------------------------------------------------------------------------------------------------------------

# f = open("test.txt", "r")
# print(f.read(3))  # считывает указанное число символов
# print(f.tell())  # возвращает текущую позицию условного курсора в файле
# print(f.seek(1))  # переставляет курсор на указанную позицию
# print(f.read())  # проверяем где стоит курсор
# print(f.tell())
# f.close()

# -------------------------------------------------------------------------------------------------------------

# f = open('test.txt', 'r+')   # r+ для чтения и записи существующего файла
# print(f.write("I am learning Python"))
# print(f.tell())
# print(f.seek(3))
# print(f.write("-new string-"))
# print(f.tell())
# f.close()

# -------------------------------------------------------------------------------------------------------------

# with open('test.txt', 'w+') as f:
#     print(f.write('01234\n56789'))
#
# with open("test.txt", 'r') as f:
#     for line in f:
#         print(line[:3])

# -------------------------------------------------------------------------------------------------------------

# file_name = "res_1.txt"
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     print(lt)
#     return " ".join(lt)
#
#
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))
#
# with open(file_name, 'r') as f:
#     nums = f.read()
#
# print(nums)
#
# nums_list = list(map(float, nums.split()))
# print(nums_list)
# print(sum(nums_list))
# print(len(nums_list))
#
# print('Done !')

# -------------------------------------------------------------------------------------------------------------

# def longest_worlds(file):
#     with open(file, 'r', encoding='utf-8') as text:
#         w = text.read().split()
#         max_length = len(max(w, key=len)) # выявили самое длянное слово,а len посчитало кол-во символов
#         res = [word for word in w if len(word) == max_length]  # где word переменная счетчик
#         if len(res) == 1:  # условие для вывода одного длинного слова----
#             return res[0]  # ---, если их несколько тогда сл.return выведет их кол-во
#         return res
#
#
# print(longest_worlds('words.txt'))

# -------------------------------------------------------------------------------------------------------------
# Работа с двумя файлами, замена слова.
# one = 'one.txt'
# two = 'two.txt'
# # text = "Строка № 1\nСтрока № 2\nСтрока № 3\nСтрока № 4\nСтрока № 5\nСтрока № 6\nСтрока № 7\nСтрока № 8\nСтрока № 9\nСтрока № 10\n"
# # with open(one, 'w') as f:
# #     f.write(text)
#
# with open(one, 'r') as fr, open(two, 'w') as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия -")
#         fw.write(line)

