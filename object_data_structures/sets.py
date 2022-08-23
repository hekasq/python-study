# Tuples - similar to Dictionary, but immutable. Once an element is inside a tuple it cannot be reassigned
# Useful for passing objects that don't accidently don't get change - data integrity

def basic():
    print("BASIC :")
    this_set = set()
    this_set.add(1)
    this_set.add(2)
    this_set.add(1)
    print(this_set)


def listvsset():
    print("LIST V SET :")
    this_list = [1, 1, 1, 1, 2, 2, 2, 1]
    this_set = set(this_list)
    print(this_set)
    print(set('Mississipi'))


if __name__ == '__main__':
    basic()
    listvsset()
