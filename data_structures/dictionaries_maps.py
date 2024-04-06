# Unordered mappings that store an object
# k-v: {'k1':'v1', 'k2':'v2'} - unordered, unsortable
# insertion order preserved in Python 3.7

import json


def basic():
    print("BASIC :")
    animals = {'rodent': 'sqrl', 'insect': 'bee'}
    print(animals)
    print(animals['rodent'])

    prices = {'apple': 1.5, 'grapes': {'green': 12, 'red': 15}, 'noodles': [8, 7, 9]}
    print(prices['grapes']['green'])
    print(prices['noodles'][2])
    print(animals.items())


def manipulation():
    print("MANIPULATION :")
    fruit = {'apple': 'tasty', 'grapes': {'green': 'sour', 'red': 'sweet'}, 'plums': ['pretty', 'low_sugar']}
    print(fruit['grapes']['green'].upper())
    print(fruit)
    fruit['peach'] = 'filling'
    print(fruit)


def key_value_methods():
    print("USEFUL METHODS :")
    fruit = {'apple': 'tasty', 'grapes': {'green': 'sour', 'red': 'sweet'}, 'plums': ['pretty', 'low_sugar']}
    print(fruit.keys())
    print(fruit.values())
    print(fruit.values().mapping)


def default_methods():
    print("DEFAULT METHODS :")
    fruit = {'apple': 'tasty', 'grapes': {'green': 'sour', 'red': 'sweet'}, 'plums': ['pretty', 'low_sugar']}
    # just returns
    print(fruit.get("applez", "galas"))
    # returns and inserts
    fruit.setdefault('apples', 'healthy')
    print(fruit.get('apples'))


def manipulation_queues():
    print("MANIPULATION QUEUES :")
    fruit = {'apple': 'tasty', 'grapes': {'green': 'sour', 'red': 'sweet'}, 'plums': ['pretty', 'low_sugar']}
    pop_val = fruit.pop('apple', 'default')
    print(pop_val)
    print(fruit)

    pop_val = fruit.popitem()
    print(pop_val)
    print(fruit)


def merging():
    print("MERGING METHODS :")
    fruit1 = {'apple': 'tasty', 'grapes': {'green': 'sour', 'red': 'sweet'}, 'plums': ['pretty', 'low_sugar']}
    fruit2 = {'peach': 'juicy', 'banana': 'yellow'}

    fruit3 = fruit1 | fruit2
    print(fruit3)

    fruit4 = {**fruit1, **fruit2}
    print(fruit4)


def construction():
    print("CONSTRUCTION :")
    x = {x: x * x for x in range(10)}
    print(x)

    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    dictionary = dict(zip(keys, values))
    print(dictionary)


def filtering():
    fruit1 = {'apple': 'tasty', 'grapes': {'green': 'sour', 'red': 'sweet'}, 'plums': ['pretty', 'low_sugar']}
    filtered = {k: v for k, v in fruit1.items() if 'a' in k}
    print(filtered)


def iterating():
    fruit1 = {'apple': 'tasty', 'grapes': {'green': 'sour', 'red': 'sweet'}, 'plums': ['pretty', 'low_sugar']}
    for fruit in fruit1.items():
        print(fruit)

    for key in fruit1.keys():
        print(key)

    for value in fruit1.values():
        print(value)


def json_loads():
    person = json.loads('{"name": "John", "age": 30}')
    dumped_string = json.dumps(person)
    print(person.keys())
    print(person.values())
    print(dumped_string)

if __name__ == '__main__':
    json_loads()
