# file_name = 'basket.txt'
#
# shop_list = {
#     'фрукты': ['яблоки', 'манго',],
#     'овощи': ['морковь',],
#     'бюджет': 1000
# }
#
# with open(file_name, 'wb') as fh:
#     pickle.dump(shop_list, fh)
#
# with open(file_name, 'rb') as fh:
#     shop_list_2 = pickle.load(fh)
#
# print(shop_list_2)


# class Test:
#     num = 35
#     str = 'привет'
#     lst = [1, 2, 3]
#     tpl = (22, 23)
#
#     def __str__(self):
#         return f'Число: {Test.num}\nСтрока: {Test.str}\nСписок: {Test.lst}\nКортеж: {Test.tpl}'
#
#
# obj = Test()
# obj1 = pickle.dumps(obj)
# print(f'Сериализация в строку:\n{obj1}')
# obj2 = pickle.loads(obj1)
# print(f'Десериализация из строки:\n{obj2}')

# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = 'test'
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f'{self.a} {self.b} {self.c(2)}'
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# print(item1)
# item2 = pickle.dumps(item1)
# print(item2)
# item3 = pickle.loads(item2)
# print(item3)
# # print(item3.__dict__)


# data = {
#     'name': 'Olga',
#     'age': 35,
#     20: None,
#     'hobbies': ('running', 'singing',),
#     'children': [
#         {
#             'firstname': 'Alice',
#             True: 1
#         }
#     ]
# }
#
# # file_name = 'data_file.json'
# #
# # with open(file_name, 'w') as fw:
# #     json.dump(data, fw, indent=4)
# #
# # with open(file_name, 'r') as fw:
# #     data1 = json.load(fw)
# #
# # print(data1)
#
# json_string = json.dumps(data)
# print(json_string)
# print(type(json_string))
# data1 = json.loads(json_string)
# print(data1)
# print(type(data1))

# x = {
#     'name': 'Виктор'
# }
#
# print(json.dumps(x))
# print(json.loads(json.dumps(x)))
# print(json.dumps(x, ensure_ascii=False))

# from random import choice


# def gen_person():
#     name = ''
#     tel = ''
#
#     letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'e']
#     num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#
#     while len(name) != 7:
#         name += choice(letter)
#     print(name)
#
#     while len(tel) != 10:
#         tel += choice(num)
#     print(tel)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#     return person


# person = []
# for i in range(5):
#     person.append(gen_person())
#
# with open('persons.json', 'w') as f:
#     json.dump(person, f, indent=2)


# def write_json(person_dict):
#     try:
#         data = json.load(open('persons.json'))
#     except FileNotFoundError:
#         data = []
#
#     data.append(person_dict)
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(gen_person())
# import json
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         a = ', '.join(map(str, self.marks))
#         return f'Студент: {self.name}: {a}'
#
#     def add_mark(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#         def average_mark(self):
#             return round(sum(self.marks) / len(self.marks), 2)
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.groups = group
#
#     def __str__(self):
#         a = "\n".join(map(str, self.students))
#         return f'\nГруппа: {self.groups}\n{a}'
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         return self.students.pop(index)
#
#     @staticmethod
#     def charge_group(group_1, group_2, index):
#         group_2.add_student(group_1.remove_student(index))
#
#     def dump_to_json(self, file_name):
#         data = {"name": self.name, "marks": self.marks}
#         with open(file_name, "w") as f:
#             json.dump(data, f)
#
#
#     def load_from_file(self, file_name):
#         with open(file_name, "r") as f:
#             print(json.load(f))
#
#
#     def get_file_name(self ):
#         return self.name + ".json"
#
#
#
#
#
#
# st1 = Student("Bjdnya", [5, 4, 3, 4, 5, 3])

# st1.dump_to_json("student1.json")
#
# st1.load_from_file("student1.json")
# st2 = Student("Nikolaenko", [2, 3, 5, 4, 2])
# st3 = Student("Birukov", [3, 5, 3, 2, 5, 4])
# sts1 = [st1, st2]
# group1 = Group(sts1, " GK Python")
# # print(group1)
# group1.add_student(st3)
# # print(group1)
# group1.remove_student(1)
# #print(group1)
# st2 = [st2]
# group2 = Group(st2, " GK Web")
# #print(group2)
# Group.charge_group(group1, group2, 0)
# print(group1)
# print(group2)

# st1.add_mark(4)
# print(st1)
# st1.delete_mark(2)
# print(st1)
# st1.edit_mark(4, 5)
# print(st1)
# st1.delete_mark()
