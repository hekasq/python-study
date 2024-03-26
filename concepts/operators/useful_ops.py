# Tuples - similar to Dictionary, but immutable. Once an element is inside a tuple it cannot be reassigned
# Useful for passing objects that don't accidently don't get change - data integrity
from random import shuffle
from random import randint


def range_func():
    print("RANGE FUNC :")
    mylist = [1, 2, 3]
    for num in range(3):
        print(num)
    print("RANGE FUNC + IDX :")
    for num in range(1, 4):
        print(num)
    print("RANGE FUNC + IDX + STEP:")
    for num in range(1, 10, 2):
        print(num)
    print("RANGE FUNC + IDX + STEP +TOLIST:")
    print(list(range(1, 10, 2)))


def enumerator():
    print("ENUMERATOR :")
    # returns index and value
    word = 'abcde'
    for letter in enumerate(word):
        print(letter)


def zipper():
    print("ZIPPER :")
    mylist1 = [1, 2, 3, 4, 5]
    mylist2 = ['a', 'b', 'c']
    mylist3 = [100, 200, 300]
    for item in zip(mylist1, mylist2, mylist3):
        print(item)
    print(list(zip(mylist1, mylist2, mylist3)))


def access():
    print("ACCESS :")
    mylist1 = [1, 2, 3, 4, 5]
    diction = {'k1': 1, 'k2': 2}
    print(1 in mylist1)
    print('k' in diction)
    print('k1' in diction)
    print(1 in diction)
    print(1 in diction.values())


def min_max():
    print("MIN_MAX :")
    mylist1 = [1, 2, 3, 4, 5]
    print(min(mylist1))
    print(max(mylist1))


def randomz():
    print("RANDOM :")
    mylist1 = [1, 2, 3, 4, 5]
    shuffle(mylist1)
    print(f'Shuffled: {mylist1}')
    print(f'Randomint: ', randint(0, 10))


def inputANum():
    print("INPUT :")
    inpt = input('Gimme a number: ')
    print(f'Input is {inpt}')


if __name__ == '__main__':
    range_func()
    enumerator()
    zipper()
    access()
    min_max()
    randomz()
    inputANum()
