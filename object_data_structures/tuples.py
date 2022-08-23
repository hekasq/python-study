# Tuples - similar to Dictionary, but immutable. Once an element is inside a tuple it cannot be reassigned
# Useful for passing objects that don't accidently don't get change - data integrity

def basic():
    print("BASIC :")
    tpl = ('one', 2, 3, 2)
    print(type(tpl))
    print(tpl[1])
    print(tpl[-1])
    print(tpl.count(2))
    print(tpl.index('one'))


def listvtuple():
    print("MUTABILITY :")
    tpl = ('one', 2, 'three', 2)
    list = ['one', 2, 'three', 2]
    print(list)
    list[0] = 'NEW'
    print(list)

    # throws an error - 'tuple' object does not support item assignment
    # tpl[0]= 'NEW'


if __name__ == '__main__':
    basic()
    listvtuple()
