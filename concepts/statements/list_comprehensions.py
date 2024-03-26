# Indentation matters
def basic():
    print("BASIC: ")
    my_string = 'hello'
    my_list = []

    for lettr in my_string:
        my_list.append(lettr)
    print(my_list)
    # FLAT FOR LOOP
    my_list_2 = [lettr for lettr in 'strng']
    print(my_list_2)

    my_list_3 = [num + 1 for num in range(10)]
    print(my_list_3)

    my_list_4 = [x ** 2 for x in range(1, 11) if x % 2 == 0]
    print(my_list_4)

    celsius = [0, 10, 30, 40.5]
    fahrenheight = [((9 / 5) * temp + 32) for temp in celsius]
    print(fahrenheight)

    my_list_5 = [x * y for x in [2, 4, 6] for y in [1, 2]]
    print(my_list_5)


if __name__ == '__main__':
    basic()
