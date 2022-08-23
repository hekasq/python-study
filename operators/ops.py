# Tuples - similar to Dictionary, but immutable. Once an element is inside a tuple it cannot be reassigned
# Useful for passing objects that don't accidently don't get change - data integrity

def comparing():
    print("COMPARING :")
    print('b' == 'B')
    print(2 == '2')
    print(2.0 == 2)


def chaining():
    print("CHAINING :")
    print(1 < 2 < 3)
    print(1 < 2 > 3)
    print(1 < 2 and 2 > 3)
    print(1 < 2 or 2 > 3)


if __name__ == '__main__':
    comparing()
    chaining()
