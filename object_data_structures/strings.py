# Strings are immutable - str object doesn't support item assignment name = "Sam" str[0]="P" => fail
#

def basic_strings():
    print("Basic String: ")
    string1 = 'hello'
    string2 = "hey"
    string3 = " spaces"
    print(string1, string2, string3)


def escapes():
    print("Escapes: ")
    print("upper \nlower")
    print("hello \t-tab-world")


def length():
    print("Length: ")
    print("Length of Racoon is", len("racoon"))


def indices():
    print("Indices: ")
    string1 = 'squirrel'
    print(string1[0])
    print(string1[-1])


# slice is like custom index
def slicing():
    print("Slicing: ")
    string1 = 'opossums are cool'
    print(string1[0:9])
    print(string1[:9])
    print(string1[9:])
    print(string1[13:17])
    print(string1[::])
    print(string1[::2])
    print(string1[0:17:3])
    print(string1[::-1])


def concat():
    print("Concat: ")
    x = "rats"
    print(x)
    x = x + " are smart "
    print(x)
    print(x * 10)
    print('2' + '3')


def manipulation():
    print("Manipulation: ")
    bird = "parrot"
    # not in place
    print(bird.upper())
    print(bird.endswith('t'))
    print(bird.find('r'))
    print(bird.split("o"))


def formatting():
    print("Format: ")
    whale = "Whales are large and impressive {}"
    print(whale.format("MAMMALS"))
    print('The {} {} {}'.format("fox", "brown", "quick"))
    print('The {2} {1} {0}'.format("fox", "brown", "quick"))
    print('The {0} {0} {0}'.format("fox", "brown", "quick"))
    print('The {f} {f} {b}'.format(f='fox', b='brown'))
    result = 10 / 93
    print(result)
    print("The result was {r}".format(r=result))
    # float formatting follows "{value:width.precision f}"
    print("The result was {r:10.3f}".format(r=result))
    print("The result was {r:1.4f}".format(r=result))


def fstrings():
    print("Fstrings: ")
    name = 'Al'
    age =3
    print(f'My hamster\'s name is {name}')
    print(f'{name} was {age} years old')


if __name__ == '__main__':
    basic_strings()
    escapes()
    length()
    indices()
    slicing()
    concat()
    manipulation()
    formatting()
    fstrings()
