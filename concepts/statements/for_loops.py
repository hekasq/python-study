def basic():
    print("BASIC: ")
    animals = ["hamster", "squirrel", "racoon"]
    for animal in animals:
        if len(animal) == 6:
            print(f'6 letters: {animal}')
        elif len(animal) == 7:
            print(f'7 letters: {animal}')


def string_iterator():
    print("STRING ITER: ")
    animal = "sqrl"
    for letter in animal:
        print(letter)

    for _ in animal:
        print('walnut')


def tuple_iterator():
    print("TUPLE ITER: ")
    tuple_list = [(1, 2), (3, 4), (5, 6), (7, 8)]
    len(tuple_list)
    for tpl in tuple_list:
        print(tpl)

    # tuple unpacking
    for a, b in tuple_list:
        print(a)
    tuple_list = [(1, 2, 3), (3, 4, 8), (5, 6, 2), (1, 7, 3)]
    for a, b, c in tuple_list:
        print(a)


def dict_iterator():
    diction = {'k1': 1, 'k2': 2, 'k3': 3}
    for key1 in diction:
        print(key1)
    for items in diction.items():
        print(items)
    for key2, value in diction.items():
        print(f'key is {key2}, value is {value}')
    for value in diction.values():
        print(f'value is {value}')


if __name__ == '__main__':
    basic()
    string_iterator()
    tuple_iterator()
    dict_iterator()
