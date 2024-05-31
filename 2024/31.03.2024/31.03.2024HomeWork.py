import json
from pprint import pprint


class Student:
    def __init__(self, name, marks):
        self.name: str = name
        self.marks: list = marks

    def __repr__(self):
        marks = ', '.join(map(str, self.marks))
        return f'Студент: {self.name}: {marks}'

    def add_mark(self, mark):
        self.marks.append(mark)

    def delete_mark(self, index):
        return self.marks.pop(index)

    def edit_mark(self, index, new_mark):
        self.marks[index] = new_mark

    def average_mark(self):
        return round(sum(self.marks) / len(self.marks), 2)

    def get_file_name(self):
        return self.name + '.json'

    def dump_to_json(self):
        data = {
            'Name': self.name,
            'Marks': self.marks
        }
        with open(self.get_file_name(), 'w') as file:
            json.dump(data, file)

    def load_from_file(self):
        with open(self.get_file_name(), 'r') as file:
            pprint(json.load(file), indent=2)


class Group:
    def __init__(self, students: list[Student], group: str):
        self.students: list[Student] = students
        self.group: str = group

    def __repr__(self):
        return f'Группа: {self.group}\n' + ',\n'.join(map(str, self.students))

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, index):
        return self.students.pop(index)

    @staticmethod
    def change_group(group_1, group_2, index):
        group_2.add_student(group_1.remove_student(index))

    @property
    def get_file_name(self):
        return self.group.lower().replace(' ', '-') + '.json'

    @property
    def data(self):
        return ({
            'Group': self.group,
            'Students': [
                {'Name': student.name, 'Marks': student.marks} for student in self.students
            ]
        })

    def dump_to_json(self):
        data = [{'Name': student.name, 'Marks': student.marks} for student in self.students]
        with open(self.get_file_name, 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=2)

    def load_from_file(self):
        with open(self.get_file_name, 'r') as file:
            pprint(json.load(file), indent=2)

    @staticmethod
    def dump_groups_to_json(*args):
        data = {'Groups': []}
        names = []
        for _ in args:
            group = _.data
            data['Groups'].append(group)
            names.append(group['Group'].lower().replace(' ', '_'))
        file_name = '-'.join(names) + '.json'

        with open(file_name, 'w', encoding='UTF-8') as file:
            json.dump(data, file, indent=2)

    @staticmethod
    def load_groups_from_file(file_name):
        with open(file_name, 'r') as file:
            pprint(json.load(file), indent=2)


st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
st2 = Student('Nikolaenko', [2, 3, 5, 4, 2])
st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])

sts1 = [st1, st2]

group1 = Group(sts1, 'ГК Python')
sts2 = [st3]
group2 = Group(sts2, 'ГК Web')

Group.dump_groups_to_json(group1, group2)
Group.load_groups_from_file('гк_python-гк_web.json')

