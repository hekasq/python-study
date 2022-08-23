# Unordered mappings that store an object
# k-v: {'k1':'v1', 'k2':'v2'} - unordered, unsortable

def basic():
    print("BASIC :")
    animals = {'rodent': 'sqrl', 'insect': 'bee'}
    print(animals)
    print(animals['rodent'])

    prices = {'apple': 1.5, 'grapes': {'green': 12, 'red': 15}, 'noodles': [8, 7, 9]}
    print(prices['grapes']['green'])
    print(prices['noodles'][2])


def manipulation():
    print("MANIPULATION :")
    fruit = {'apple': 'tasty', 'grapes': {'green': 'sour', 'red': 'sweet'}, 'plums': ['pretty', 'low_sugar']}
    print(fruit['grapes']['green'].upper())
    print(fruit)
    fruit['peach'] = 'filling'
    print(fruit)


def useful_methods():
    print("USEFUL METHODS :")
    fruit = {'apple': 'tasty', 'grapes': {'green': 'sour', 'red': 'sweet'}, 'plums': ['pretty', 'low_sugar']}
    print(fruit.keys())
    print(fruit.values())
    print(fruit.values().mapping)


if __name__ == '__main__':
    basic()
    manipulation()
    useful_methods()
