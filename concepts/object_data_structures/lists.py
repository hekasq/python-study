def basic():
    print("Basic: ")
    list_1 = [1, 2, 3]
    list_2 = ['one', 2, '3ss']
    print(list_1)
    print(list_2)


def idxs():
    print("Indexing: ")
    animals = ['sqrl', 'possum', 'racoon']
    insects = ['bee', 'mantis', 'wasp']
    living = animals + insects
    print(animals[1])
    print(animals[::])
    print(living)
    animals[0] = 'stevus'
    print(animals)
    print(living)
    animals.append('ratster')
    print(animals)
    print(animals)
    animals.pop(-1)
    print(animals)
    new_animal = animals.pop(1)
    print(animals)
    print(new_animal)


def sorting():
    print("Sorting: ")
    # natural order
    animals = ['sqrl', 'possum', 'racoon', 'hamster']
    print(animals)
    new_list = animals.sort()
    print(animals)
    # because sorting doesn't return anything
    print(type(new_list))
    print(animals.reverse())

    print(animals)


if __name__ == '__main__':
    basic()
    idxs()
    sorting()
