# text = ("Замена строки в текстовом файле;\n"
#         "Записать список в файл;\n"
#         "Изменить строку в списке;\n")
#
#
# def file_w(one, text):
#     with open(one, "w") as f:
#         f.write(text)
#
#
# def input_index(two):
#     with open(two, 'r') as f:
#         read_text = f.readlines()
#     while True:
#         index1 = int(input('Введите номер первой строки: '))
#         index2 = int(input('Введите номер второй строки: '))
#
#         if 0 < index1 <= len(read_text) and 0 < index2 <= len(read_text):
#             read_text[index1 - 1], read_text[index2 - 1] = read_text[index2 - 1], read_text[index1 - 1]
#             break
#         else:
#             print('Введите число согласно требованиям')
#
#     with open(two, "w") as f:
#         f.writelines(read_text)
#
#
# file_w("text3.txt", text)
# input_index("text3.txt")
