import json
from random import choice


def gen_person():
    name = ''
    tel = ''

    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'e']
    num = ['1', '1', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letter)

    while len(tel) != 10:
        tel += choice(num)

    person = {
        'name': name,
        'tel': tel
    }
    return person


def write_json(person_dict):
    try:
        with open('persons.json') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    key = tel_key(person_dict['tel'])
    data[key] = person_dict

    with open('persons.json', 'w') as f:
        json.dump(data, f, indent=2)


def tel_key(tel):
    return tel[:3] + tel[-4:]


for i in range(5):
    write_json(gen_person())